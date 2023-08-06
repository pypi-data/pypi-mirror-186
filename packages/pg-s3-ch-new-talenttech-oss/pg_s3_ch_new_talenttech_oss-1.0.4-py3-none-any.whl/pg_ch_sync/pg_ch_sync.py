import logging
import sys
from pg_s3_ch.sql_queries import SQL_CH_TABLES, SQL_PG_TABLES
from pg_s3_ch.pg_s3_ch import PGS3CH


def setup_logging():
    global logger
    logger = logging.getLogger("pg_s3_ch")
    logging.basicConfig(
        stream=sys.stdout,
        level="INFO",
        format="%(asctime)s %(processName)s %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


class Syncer(PGS3CH):

    def __init__(self, ch_config, pg_config):
        super().__init__(
            config={},
            s3_config={},
            ch_config=ch_config,
            pg_config=pg_config
        )

    def sync_tables(self, tables_to_exclude=None):
        """
        :param tables_to_exclude: list of tables shouldn't  being considered
        :return: tuple : (list of tables need to remove, list of tables need to create or recreate)
        """
        logger.info("Get tables from pg")
        cnx = self.connect_to_pg()

        cursor = cnx.cursor()
        tables_to_exclude = (
            ",".join(["'" + item + "'" for item in tables_to_exclude.split(",")])
            if tables_to_exclude
            else "''"
        )

        sql = SQL_PG_TABLES.format(tables_to_exclude=tables_to_exclude)
        cursor.execute(sql)
        tables_pg = [r[0] for r in cursor]
        cursor.close()
        cnx.close()

        logger.info("Get tables from ch")

        sql = SQL_CH_TABLES.format(
            database=self.ch_config["database"], tables_to_exclude=tables_to_exclude
        )
        result = self.ch_client.execute(sql)
        tables_ch = [r[0] for r in result]
        return tables_ch, tables_pg

    def save_sync_tables(self, client_description, save_table_name, tables_to_exclude):
        """

        :param client_description:
        :param save_table_name:
        :param tables_to_exclude:
        :return: None
        """
        tables_ch, tables_pg = self.sync_tables(tables_to_exclude=tables_to_exclude)
        tables_to_remove = [c for c in tables_ch if c not in tables_pg]

        new_tables = []
        for row in tables_pg:
            items = {
                "client_description": client_description,
                "table_name_ch": row,
                "table_name_pg": row,
                "database_pg": self.pg_config["database"],
                "database_ch": self.ch_config["database"],
            }

            new_tables.append(items)

        table_name = f"{save_table_name}"
        if len(tables_pg) > 0:
            columns = list(items.keys())
            columns = ",".join(columns)

        for items in new_tables:

            sql_stat = " SELECT 1 FROM {table_name}" \
                       " WHERE database_pg = '{database_pg}' " \
                       " AND table_name_pg = '{table_name_pg}' " \
                       " AND database_ch = '{database_ch}'".format(
                table_name=table_name,
                database_pg=self.pg_config["database"],
                table_name_pg=items["table_name_pg"],
                database_ch=self.ch_config["database"],
            )

            check_statement = self.ch_client.execute(sql_stat)
            if len(check_statement) == 0:
                logger.info("Add new table %s", table_name)
                self.ch_client.execute(
                    f"INSERT INTO {table_name} ({columns}) VALUES",
                    [items],
                    types_check=True,
                )

        for items in tables_to_remove:
            drop_stat = "DROP TABLE IF EXISTS  {database_ch}.{table_name_pg}".format(
                database_ch=self.ch_config["database"], table_name_pg=items
            )
            logger.info(drop_stat)
