import os
import sys
import math
from datetime import datetime, timedelta, time
from typing import Optional
from enum import Enum

import logging
import gzip
import psycopg2
import clickhouse_driver
import psycopg2.extras
from s3.client import Client as s3_client
from clickhouse_driver import Client
from pg_s3_ch.sql_queries import (
    SQL_HISTORY,
    SQL_HISTORY_RANGE,
    SQL_HISTORY_RANGE_NO_INT,
    SQL_HISTORY_NO_INT,
    SQL_CH_SCHEMA,
    SQL_PARTS,
)
from pg_s3_ch.temp_table_creator_ch import TempTableCreatorCH

PG_HISTORY_STEP_DEFAULT = 500000
FILE_PATH = "./csv/{entity_name}_{range_from}.csv.gz"
S3_FILE_FORMAT = "{endpoint_url}/{bucket}/{upload_path}/{entity_name}_*.csv.gz"
EXPORT_PATH = "./csv"


def setup_logging():
    global logger
    logger = logging.getLogger("pg_s3_ch")
    logging.basicConfig(
        stream=sys.stdout,
        level="INFO",
        format="%(asctime)s %(processName)s %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def create_files_dir():
    try:
        logging.info("Working directory is {getcwd}".format(getcwd=os.getcwd()))
        os.makedirs(EXPORT_PATH)
    except OSError:
        logging.info(
            "Can't create directory {export_path}".format(export_path=EXPORT_PATH)
        )
    else:
        logging.info(
            "{export_path} was successfully created".format(export_path=EXPORT_PATH)
        )


def drop_files_dir():
    if os.path.isdir(EXPORT_PATH):
        for file in os.listdir(EXPORT_PATH):
            logging.info("Remove file %s", file)
            os.remove(EXPORT_PATH + "/" + file)
        os.removedirs(EXPORT_PATH)


def sql_to_file(cnx, file_path, sql):
    """
    Save result of sql to file
    :param cnx:
    :param file_path:
    :param sql:
    :return:
    """
    with gzip.open(file_path, "wt") as fa:
        cursor = cnx.cursor()
        cursor.copy_to(fa, "({sql})".format(sql=sql), null="")
        cursor.close()

    # with gzip.open(file_path, 'wt') as fa:
    #     cursor = cnx.cursor()
    #     sql_copy = "COPY ({sql}) TO STDOUT WITH NULL AS '' csv DELIMITER '\t' "
    #     cursor.copy_expert(sql_copy.format(sql=sql), file=fa)
    #
    #     cursor.close()


def file_to_s3(s3_client_, file_path, s3_path):
    """
    Save result of sql to file
    :param s3_path:
    :param s3_client_:
    :param file_path:
    :return:
    """
    logging.info(os.path.basename(file_path))
    s3_client_.upload_file(file_path, s3_path)


def tmp_table_wrapper(f):
    def wrapper(*args):
        with TempTableCreatorCH(
                ch_client=args[0].ch_client,
                table_name=args[0].ch_name,
                table_name_tmp=args[0].temp_table_prefix + args[0].ch_name,
                database=args[0].ch_config["database"],
                staging_database=args[0].ch_config["staging_database"],
                sorting_key=args[0].sorting_key,
                partition_key=args[0].partition_key,
                ttl=args[0].ttl
        ) as tmp_creator:
            f(*args)
            if not args[0].by_date:
                tmp_creator.exchange()

    return wrapper


def check_ch_config(ch_config: dict):
    for param in ["host", "port", "user", "password", "database", "staging_database"]:
        if param not in ch_config:
            raise BaseException(
                "Error. You must specify {} param in ch_config".format(param)
            )


def check_pg_config(pg_config: dict):
    for param in ["host", "port", "user", "password", "database"]:
        if param not in pg_config:
            raise BaseException(
                "Error. You must specify {} param in ch_config".format(param)
            )


def check_s3_config(s3_config: dict):
    for param in [
        "S3_ENDPOINT_URL",
        "S3_TOPMIND_CLIENT_DATA_BUCKET",
        "S3_FOLDER",
        "S3_ACCESS_KEY",
        "S3_ACCESS_SECRET",
        "UPLOAD_PATH",
    ]:
        if param not in s3_config:
            raise BaseException(
                "Error. You must specify {} param in s3_config".format(param)
            )


def check_config(config: dict):
    for param in ["name"]:
        if param not in config:
            raise BaseException(
                "Error. You must specify {} param in config".format(param)
            )


def set_bool_value(config, key, default_value):
    if config.get(key, default_value) is None:
        return default_value
    else:
        return bool(int(config.get(key, default_value)))


class TypeUpload(Enum):
    BATCH = 0
    BY_DATE = 1
    INCREMENTAL = 2


class PGS3CH:
    """
      Represents class realizing the logic of transferring data from PostgreSQL to click house
      :param config:
      :param s3_config:
      :param ch_config:
      :param pg_config:
      """

    def __init__(self, config, s3_config, ch_config, pg_config):

        setup_logging()

        check_config(config)
        check_s3_config(s3_config)
        check_ch_config(ch_config)

        self.config = config
        self.s3_config = s3_config
        self.pg_config = pg_config
        self.ch_config = ch_config

        self.execution_date = os.getenv("execution_date")

        self.entity_name: str = ""  # table name in pg
        self.ch_name: str = ""  # table name in ch
        self.partition_key: str = "tuple()"
        self.sorting_key: str = "id"
        self.key_field: str = "id"
        self.pg_history_step: int = PG_HISTORY_STEP_DEFAULT
        self.temp_table_prefix: str = "_temp_"
        self.ttl: Optional[str] = ""

        self.where_condition: Optional[str] = None
        self.incremental: Optional[bool] = None
        self.incremental_field: Optional[str] = None
        self.range_parts_per_day: Optional[
            int
        ] = None  # Optional if incremental or by date
        self.by_date: Optional[bool] = None  # Optional if download by date
        self.date_field: Optional[str] = None  # Optional
        self.need_clear_s3: Optional[bool] = None  #
        self.need_optimize: Optional[bool] = None

        self.ch_exclude_columns_str: str = ""
        self.ch_exclude_columns: Optional[
            list[str]
        ] = None  # Columns we should ignore in clickhouse table

        self.type_upload: TypeUpload = TypeUpload.BATCH  # Type upload,  default Batch
        self.transform_params()  # get transformed params from the config

        self.ch_client = None
        self.connect_to_ch()

        self.schema_ch_insert_fields = []
        self.schema_ch_insert_names = []
        self.schema_pg_select_fields = {}
        self.ch_fields = {}
        self.key_field_is_int = True

    def transform_params(self):

        self.entity_name = self.config.get("name")
        self.ch_name = self.config.get("ch_name", self.entity_name) or self.entity_name
        self.key_field = self.config.get("key_field", "id") or "id"
        self.pg_history_step = int(
            self.config.get("pg_history_step", PG_HISTORY_STEP_DEFAULT)
            or PG_HISTORY_STEP_DEFAULT
        )
        self.need_optimize = set_bool_value(self.config, "need_optimize", True)
        self.incremental = set_bool_value(self.config, "incremental", False)
        self.need_clear_s3 = set_bool_value(self.config, "need_clear_s3", False)
        self.by_date = set_bool_value(self.config, "by_date", False)

        self.partition_key = self.config.get("partition_key", "tuple()") or "tuple()"
        self.sorting_key = self.config.get("sorting_key", "id") or "id"
        self.ttl = self.config.get("ttl", "") or ""
        self.temp_table_prefix = self.ch_config.get("temp_table_prefix", "_temp_") or "_temp_"

        if self.by_date:
            self.type_upload = TypeUpload.BY_DATE
            self.temp_table_prefix += self.execution_date[0:10].replace("-", "")
            self.date_field = self.config.get("date_field", "created_at") or "created_at"
            self.incremental_field = self.date_field
            self.range_parts_per_day = int(self.config.get("range_parts_per_day", 24) or 24)

        elif self.incremental:
            self.type_upload = TypeUpload.INCREMENTAL
            self.range_parts_per_day = int(self.config.get("range_parts_per_day", 24) or 24)
            self.incremental_field = str(
                self.config.get("incremental_field", "updated_at") or "updated_at"
            )

        self.ch_exclude_columns_str = self.ch_config.get(
            "ch_exclude_columns", "ts_captured"
        ) or "ts_captured"

        self.ch_exclude_columns = ",".join(
            ["'" + item + "'" for item in self.ch_exclude_columns_str.split(",")]
        )

        self.where_condition = str(self.config.get("where_condition", "") or "")

    def get_table_schema_ch(self):
        sql = SQL_CH_SCHEMA.format(
            database=self.ch_config["database"],
            table=self.ch_name,
            exclude_columns=self.ch_exclude_columns,
        )

        logger.info(sql)
        result = self.ch_client.execute(sql)
        try:
            type_key_field = [r[1] for r in result if r[0] == self.key_field][0]
        except IndexError as E:
            logging.error('Can not find key field. Even "id" is not in schema')
            raise IndexError(E)

        if "int" not in type_key_field.lower():
            self.key_field_is_int = False

        for row in result:
            if row[0].replace("_dt", "") in self.ch_exclude_columns_str.split(","):
                continue
            if row[2].find("Exclude") == -1:
                self.schema_pg_select_fields[row[0]] = row[1]

            if row[2].find("#OnInsert:") > -1:
                start = row[2].find("#OnInsert:") + 10
                end = row[2].find(":EndOnInsert#")
                self.schema_ch_insert_fields.append(row[2][start:end])
            else:
                self.schema_ch_insert_fields.append(row[0])
            self.schema_ch_insert_names.append(row[0])

        if len(self.schema_pg_select_fields) < 1:
            logger.info("CH schema error: %s ", self.schema_pg_select_fields)
            sys.exit(1)

        if len(self.schema_ch_insert_fields) < 1:
            logger.info(
                "CH schema error: %s. Have you already created the table?", self.ch_name
            )

            sys.exit(1)

        logger.info(
            "CH schema for %s.%s - OK", self.ch_config["database"], self.ch_name
        )

    def connect_to_ch(self):

        settings = {"insert_quorum": 3}

        self.ch_client = Client(
            host=self.ch_config["host"],
            user=self.ch_config["user"],
            password=self.ch_config["password"],
            database=self.ch_config["database"],
            settings=settings,
        )

    def clear_s3_folder(self):
        """Clear all data from s3 folder"""
        client = s3_client(
            aws_access_key_id=self.s3_config["S3_ACCESS_KEY"],
            aws_secret_access_key=self.s3_config["S3_ACCESS_SECRET"],
            endpoint_url=self.s3_config["S3_ENDPOINT_URL"],
            bucket=self.s3_config["S3_TOPMIND_CLIENT_DATA_BUCKET"],
        )

        s3_file_path = S3_FILE_FORMAT.format(
            endpoint_url=self.s3_config["S3_ENDPOINT_URL"],
            bucket=self.s3_config["S3_TOPMIND_CLIENT_DATA_BUCKET"],
            upload_path=self.s3_config["UPLOAD_PATH"],
            entity_name=self.entity_name,
        )

        if client.path_exists(s3_file_path):
            for file in self.s3_client.get_file_list(self.s3_client.root_dir):
                self.logger.info("Delete %s from s3", file)
                self.s3_client.delete_file(path=file)
            self.s3_client.delete_dir(self.s3_client.root_dir)  # remove directory

    def connect_to_pg(self):
        cnx = psycopg2.connect(
            user=self.pg_config["user"],
            password=self.pg_config["password"],
            host=self.pg_config["host"],
            port=self.pg_config["port"],
            database=self.pg_config["database"],
            sslmode="disable",
            connect_timeout=10,
        )

        cnx.set_client_encoding("UTF8")
        return cnx

    def extract_to_s3(self):
        logger.info("Starting extract to s3")
        cnx = self.connect_to_pg()
        cursor = cnx.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        sql_history_local = SQL_HISTORY

        if self.key_field_is_int:
            sql = SQL_HISTORY_RANGE.format(
                key_field=self.key_field,
                name=self.entity_name,
                where_condition="WHERE " + self.where_condition
                if self.where_condition
                else "",
            )
        else:
            logger.info("Change logic of extracting data")
            sql = SQL_HISTORY_RANGE_NO_INT.format(
                key_field=self.key_field,
                name=self.entity_name,
                where_condition="WHERE " + self.where_condition
                if self.where_condition
                else "",
            )

            sql_history_local = SQL_HISTORY_NO_INT

        cursor.execute(sql)

        for row in cursor:
            min_id = row["min_id"]
            max_id = row["max_id"]
        cursor.close()

        logger.info("Min ID: %d", min_id)
        logger.info("Max ID: %d", max_id)

        if min_id is None or max_id is None:
            logger.info("Max_id or min_id is None. Process is stopped.")
            sys.exit(0)

        step = self.pg_history_step

        end = math.ceil(max_id / step)
        logger.info("Range from 0 to %s, multiply by %s", end, step)

        client = s3_client(
            aws_access_key_id=self.s3_config["S3_ACCESS_KEY"],
            aws_secret_access_key=self.s3_config["S3_ACCESS_SECRET"],
            endpoint_url=self.s3_config["S3_ENDPOINT_URL"],
            bucket=self.s3_config["S3_TOPMIND_CLIENT_DATA_BUCKET"],
        )
        create_files_dir()

        for _id in range(0, end):
            range_from = min_id + _id * step
            range_to = min_id + _id * step + step - 1

            sql = sql_history_local.format(
                key_field=self.key_field,
                name=self.entity_name,
                fields='"' + '","'.join(self.schema_pg_select_fields.keys()) + '"',
                range_from=range_from,
                range_to=range_to,
                where_condition="WHERE " + self.where_condition
                if self.where_condition
                else "",
            )

            logger.info(sql)
            file_path = FILE_PATH.format(
                entity_name=self.entity_name, range_from=range_from
            )
            logger.info("Saving local: %s", file_path)
            sql_to_file(cnx, file_path, sql)

            path = "{upload_path}/{filename}".format(
                upload_path=self.s3_config["UPLOAD_PATH"],
                filename=os.path.basename(file_path),
            )
            logger.info(
                "Copying to S3: %s", self.s3_config["S3_ENDPOINT_URL"] + "/" + path
            )
            file_to_s3(client, file_path, path)

        cnx.close()
        drop_files_dir()
        logger.info("Full extract finished")

    def optimize(self):
        """
        Optimize table
        :return: None
        """
        sql = SQL_PARTS.format(database=self.ch_config["database"], table=self.ch_name)
        result = self.ch_client.execute(sql)

        for row in result:
            logger.info("Partition %s has %s parts", row[0], row[1])

            sql_optimize = """OPTIMIZE TABLE {database}.{table} ON CLUSTER '{{cluster}}' PARTITION {partition} """.format(
                database=self.ch_config["database"],
                table=self.ch_name,
                partition=row[0],
            )
            logger.info(sql_optimize)
            try:
                self.ch_client.execute(sql_optimize)
            except clickhouse_driver.errors.ServerException as E:
                logging.info(str(E))

            logger.info("OK")

    def s3_to_temp(self):
        """

        :return:
        """

        schema = []
        schema_insert = []

        for k in self.schema_pg_select_fields:
            schema.append(k + " " + self.schema_pg_select_fields[k])

        for k in self.schema_ch_insert_fields:
            schema_insert.append(k)

        logger.info(
            "Copying from %s/%s to %s.%s%s",
            self.s3_config["S3_ENDPOINT_URL"],
            self.s3_config["S3_TOPMIND_CLIENT_DATA_BUCKET"],
            self.ch_config["database"],
            self.temp_table_prefix,
            self.ch_name,
        )
        s3_file_path = S3_FILE_FORMAT.format(
            endpoint_url=self.s3_config["S3_ENDPOINT_URL"],
            bucket=self.s3_config["S3_TOPMIND_CLIENT_DATA_BUCKET"],
            upload_path=self.s3_config["UPLOAD_PATH"],
            entity_name=self.entity_name,
        )

        sql = """
            INSERT INTO {staging_database}.{temp_table_prefix}{table}  ({schema_insert_name})
            SELECT 
                {schema_insert}, NOW()
            FROM s3('{s3_file_path}', 
                    '{S3_ACCESS_KEY}',
                    '{S3_ACCESS_SECRET}',
                    'TSV', 
                    '{schema}',
                    'gzip'
                    );
            """.format(
            s3_file_path=s3_file_path,
            schema_insert_name='"'
                               + '","'.join(self.schema_ch_insert_names + ["ts_captured"])
                               + '"',
            staging_database=self.ch_config["staging_database"],
            table=self.ch_name,
            temp_table_prefix=self.temp_table_prefix,
            S3_ACCESS_KEY=self.s3_config["S3_ACCESS_KEY"],
            S3_ACCESS_SECRET=self.s3_config["S3_ACCESS_SECRET"],
            entity_name=self.entity_name,
            schema=", ".join(schema),
            schema_insert=", ".join(schema_insert),
        )
        logger.info(sql)

        self.ch_client.execute(sql)

        logger.info("Loading from S3 successful")

    def upload_temp_to_prod(self):
        """

        :return:
        """
        "INSERT INTO "
        sql = f"INSERT INTO {self.ch_config['database']}.{self.ch_name} SELECT * FROM {self.ch_config['staging_database']}.{self.temp_table_prefix}{self.ch_name}"
        logger.info(sql)
        self.ch_client.execute(sql)

    def check_date_exists(self):
        sql = """
                SELECT COUNT(*)
                FROM {database}.{table}   
                WHERE toDate({date_field}) = '{date}'
              """.format(
            database=self.ch_config["database"],
            table=self.ch_name,
            date_field=self.date_field + "_dt",
            date=self.execution_date[0:10],
        )
        logging.info(sql)
        return self.ch_client.execute(sql)[0][0]

    def extract_updated_to_s3(self):
        """
        Extract incremental data
        :return: None
        """
        cnx = self.connect_to_pg()
        cursor = cnx.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        range_from = datetime.combine(
            datetime.strptime(self.execution_date[0:10], "%Y-%m-%d").date(), time()
        )

        parts = self.range_parts_per_day

        client = s3_client(
            aws_access_key_id=self.s3_config["S3_ACCESS_KEY"],
            aws_secret_access_key=self.s3_config["S3_ACCESS_SECRET"],
            endpoint_url=self.s3_config["S3_ENDPOINT_URL"],
            bucket=self.s3_config["S3_TOPMIND_CLIENT_DATA_BUCKET"],
        )

        create_files_dir()

        for _ in range(0, parts):
            range_to = range_from + timedelta(seconds=3600 * 24 / parts - 0.000001)
            if range_from > datetime.now() + timedelta(hours=3):
                break

            sql = SQL_HISTORY.format(
                key_field=self.incremental_field,
                name=self.entity_name,
                fields='"' + '","'.join(self.schema_pg_select_fields.keys()) + '"',
                range_from=range_from,
                range_to=range_to,
            )
            logger.info(sql)
            file_path = FILE_PATH.format(
                entity_name=self.entity_name, range_from=range_from
            )
            logger.info("Saving local: %s", file_path)
            sql_to_file(cnx, file_path, sql)

            path = "{upload_path}/{filename}".format(
                upload_path=self.s3_config["UPLOAD_PATH"],
                filename=os.path.basename(file_path),
            )
            logger.info(
                "Copying to S3: %s", self.s3_config["S3_ENDPOINT_URL"] + "/" + path
            )
            file_to_s3(client, file_path, path)

            range_from = range_from + timedelta(hours=24 / parts)

        drop_files_dir()
        cursor.close()
        cnx.close()

        logging.info("extract_updated finished")

    def copy_prod_to_temp(self):
        """
        Insert all data except incrememtal to temp table
        :return: None
        """
        sql = """
                INSERT INTO {staging_database}.{temp_table_prefix}{table} 
                SELECT * FROM {database}.{table}   
                WHERE {primary_key_field} 
                   NOT IN (SELECT {primary_key_field} 
                           FROM {staging_database}.{temp_table_prefix}{table})
              """.format(
            staging_database=self.ch_config["staging_database"],
            temp_table_prefix=self.temp_table_prefix,
            database=self.ch_config["database"],
            table=self.ch_name,
            primary_key_field=self.key_field,
        )

        logging.info(sql)
        self.ch_client.execute(sql)

    @tmp_table_wrapper
    def transfer_data_incremental(self):
        """
        Transfer data incremental
        :return: None
        """
        if not self.incremental:
            raise ValueError("Incremental parameter have to set True or 1")

        self.get_table_schema_ch()
        self.extract_updated_to_s3()
        self.s3_to_temp()
        self.copy_prod_to_temp()

    @tmp_table_wrapper
    def transfer_data_full(self):
        """
        Transfer full data
        :return: None
        """
        self.get_table_schema_ch()
        self.extract_to_s3()
        self.s3_to_temp()

    @tmp_table_wrapper
    def transfer_data_by_date(self):
        """
        Transfer data by date
        :return: None
        """
        if self.check_date_exists() > 0:
            raise BaseException(
                f"Date {self.execution_date[0:10]} is already exists in the table"
            )

        self.get_table_schema_ch()
        self.extract_updated_to_s3()
        self.s3_to_temp()
        self.upload_temp_to_prod()

    def transfer(self):
        if self.incremental:
            self.transfer_data_incremental()
        elif self.by_date:
            self.transfer_data_by_date()
        else:
            self.transfer_data_full()

        if self.need_optimize:
            self.optimize()
