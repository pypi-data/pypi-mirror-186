import typing as _t
import decimal as _decimal
import datetime as _datetime

import sqlalchemy as _sa
import sqlalchemy.engine as _sa_engine
import sqlalchemy.schema as _sa_schema
from tinytim.rows import row_dicts_to_data as _row_dicts_to_data
from tinytim.data import column_names as _column_names

import sqlalchemize.type_convert as _type_convert
import sqlalchemize.features as _features
import sqlalchemize.insert as _insert

_Record = dict[str, _t.Any]


def create_table(
    table_name: str,
    column_names:  _t.Sequence[str],
    column_types:  _t.Sequence,
    primary_key: _t.Sequence[str],
    engine: _sa_engine.Engine,
    schema:  _t.Optional[str] = None,
    autoincrement:  _t.Optional[bool] = False,
    if_exists:  _t.Optional[str] = 'error'
) -> _sa.Table:
    
    cols = []
    
    for name, python_type in zip(column_names, column_types):
        sa_type = _type_convert._type_convert[python_type]
        if type(primary_key) is str:
            primary_key = [primary_key]
        if name in primary_key:
            col = _sa.Column(name, sa_type,
                            primary_key=True,
                            autoincrement=autoincrement)
        else:
            col = _sa.Column(name, sa_type)
        cols.append(col)

    metadata = _sa.MetaData(engine)
    table = _sa.Table(table_name, metadata, *cols, schema=schema)
    if if_exists == 'replace':
        drop_table_sql = _sa_schema.DropTable(table, if_exists=True)
        engine.execute(drop_table_sql)
    table_creation_sql = _sa_schema.CreateTable(table)
    engine.execute(table_creation_sql)
    return _features.get_table(table_name, engine, schema=schema)


def create_table_from_records(
    table_name: str,
    records:  _t.Sequence[_Record],
    primary_key: _t.Sequence[str],
    engine: _sa_engine.Engine,
    column_types:  _t.Optional[ _t.Sequence] = None,
    schema:  _t.Optional[str] = None,
    autoincrement:  _t.Optional[bool] = False,
    if_exists:  _t.Optional[str] = 'error',
    columns:  _t.Optional[ _t.Sequence[str]] = None,
    missing_value:  _t.Optional[_t.Any] = None
) -> _sa.Table:
    data = _row_dicts_to_data(records, columns, missing_value)
    if column_types is None:
        column_types = [_column_datatype(values) for values in data.values()]
    col_names = _column_names(data)
    table = create_table(table_name, col_names, column_types, primary_key, engine, schema, autoincrement, if_exists)
    _insert.insert_records(table, records, engine)
    return table


def _column_datatype(values: _t.Iterable) -> type:
    dtypes = [
        int, str, int | float, _decimal.Decimal, _datetime.datetime,
        bytes, bool, _datetime.date, _datetime.time, 
        _datetime.timedelta, list, dict
    ]
    for value in values:
        for dtype in list(dtypes):
            if not isinstance(value, dtype):
                dtypes.pop(dtypes.index(dtype))
    if len(dtypes) == 2:
        if set([int, float | int]) == {int, float | int}:
            return int
    if len(dtypes) == 1:
        if dtypes[0] == float | int:
            return float
        return dtypes[0]
    return str
    
