from sqlalchemy import Column, func
from clickhouse_sqlalchemy import types

PARSE_DATE_COLUMN = (
    "#Exclude #OnInsert:parseDateTimeBestEffortOrZero({column}):EndOnInsert#"
)

CUSTOM_TYPES = {
    "timestamp": "String",
    "timestamp without time zone": "String",
    "timestamp with time zone": "String",
    "time without time zone": "String",
    "date": "String",
    "datetime": "String",
}


def get_timestamp_columns(pg_columns: list) -> list:
    """
    Get timestamp columns,
    :param pg_columns:
    :return:
    """
    return list(c["column_name"] for c in pg_columns if c["data_type"] == "timestamp" or c["data_type"] == "date")


def insert_new_columns(pg_columns: list, columns: list[Column]):
    """
    Insert custom columns to new table
    :param pg_columns:
    :param columns:
    :return:
    """
    timestamp_columns = get_timestamp_columns(pg_columns=pg_columns)
    for column in columns.copy():
        if column.name in timestamp_columns:
            new_column = Column(
                name=column.name + "_dt",
                type_=types.DateTime,
                comment=PARSE_DATE_COLUMN.format(column=column.name),
            )
            columns.insert(columns.index(column) + 1, new_column)
    # ts_captured as last column
    dt = Column("ts_captured", types.DateTime, server_default=func.now())
    columns.append(dt)


def exclude_columns(columns: list) -> list:
    """
    Exclude columns with #Exclude in comments
    :param columns:
    :return:
    """
    for c in columns.copy():
        if "#Exclude" in (c["comment"] or ""):
            columns.remove(c)
