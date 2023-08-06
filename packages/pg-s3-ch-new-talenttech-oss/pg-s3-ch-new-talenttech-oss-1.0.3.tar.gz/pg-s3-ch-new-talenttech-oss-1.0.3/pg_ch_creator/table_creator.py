import logging

from sqlalchemy.sql.ddl import CreateTable

from pg_ch_creator.table_transformer import (
    insert_new_columns,
    exclude_columns,
    CUSTOM_TYPES
)
from pg_ch_creator.compile_dialect import Compiler
from converter.pg_ch_converter.schemas_checker import SchemaChecker, ChangeEvent


def format_config(config: dict) -> dict:
    columns = ["host", "user", "password", "port", "database"]
    return {item: value for item, value in config.items() if item in columns}


def create_or_update(
        table_name_pg: str,
        table_name_ch: str,
        config: dict,
        pg_config: dict,
        ch_config: dict,
):
    _sql_credentials = {
        "pg": format_config(pg_config),
        "ch": format_config(ch_config),
    }
    checker = SchemaChecker(
        sql_credentials=_sql_credentials,
        table_name_pg=table_name_pg,
        table_name_ch=table_name_ch,
        sorting_key=config["sorting_key"] + ' ' + config.get('ttl', ''),
        partition_key=config["partition_key"],
        custom_types=CUSTOM_TYPES,
        exclude_columns_ch=config["ch_exclude_columns"],
    )
    if not checker.db_worker_to.is_table_exists(table_name_ch):
        new_table = checker.create_table(insert_func=insert_new_columns)
        new_table.create()
        test_class = Compiler(checker.db_worker_to)
        logging.info(test_class.compile(CreateTable(new_table)))

    else:
        events = checker.get_difference_events(exclude_function=exclude_columns)
        if len(events):
            for event in events:
                if event.change_event != ChangeEvent.TYPE_UPDATE:
                    checker.db_worker_to.execute(checker.alter_statement(event))
                logging.info(checker.alter_statement(event))

