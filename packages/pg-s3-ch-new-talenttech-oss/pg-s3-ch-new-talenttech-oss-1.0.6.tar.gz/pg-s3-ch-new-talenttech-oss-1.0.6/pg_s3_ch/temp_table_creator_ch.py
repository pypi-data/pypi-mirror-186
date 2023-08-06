import logging
from typing import Optional
from clickhouse_driver import Client

logger = logging.getLogger(__name__)


class TempTableCreatorCH(object):
    """create temporary table in clickhouse based on table_name"""

    def __init__(self,
                 ch_client: Client,
                 table_name: str,
                 table_name_tmp: str,
                 database: str,
                 staging_database: str,
                 sorting_key: Optional[str] = 'id',
                 partition_key: Optional[str] = 'tuple()',
                 ttl: Optional[str] = ''):
        """
        :param table_name:
        :param table_name_tmp:
        :param database:
        :param staging_database:
        :param sorting_key:
        :param partition_key:
        :param ttl:
        """
        self.ch_client = ch_client
        self.table_name = table_name
        self.table_name_tmp = table_name_tmp
        self.database = database
        self.staging_database = staging_database
        self.sorting_key = sorting_key
        self.partition_key = partition_key
        self.ttl = ttl

    def create(self):
        statement = f"""CREATE TABLE {self.staging_database}.{self.table_name_tmp} ON CLUSTER '{{cluster}}' AS {self.database}.{self.table_name}
           ENGINE=ReplicatedMergeTree()
           PARTITION BY {self.partition_key} ORDER BY ({self.sorting_key})  {self.ttl}
        """
        logging.info(statement)
        self.ch_client.execute(statement)

    def drop(self):
        statement = f"""DROP TABLE IF EXISTS {self.staging_database}.{self.table_name_tmp} ON CLUSTER '{{cluster}}'"""
        logging.info(statement)
        self.ch_client.execute(statement)

    def exchange(self):
        """
        exchange
        :return:
        """
        statement = f"""EXCHANGE TABLES {self.staging_database}.{self.table_name_tmp} AND {self.database}.{self.table_name} ON CLUSTER '{{cluster}}' """
        logging.info(statement)
        self.ch_client.execute(statement)

    def __enter__(self):
        self.drop()
        self.create()
        return self

    def __exit__(self, type, value, traceback):
        self.drop()
