import typing as _typing

import sqlalchemy as _sa
import sqlalchemy.orm.session as _sa_session
import sqlalchemy.engine as _sa_engine

import sqlalchemize.records as _records
import sqlalchemize.types as _types
import sqlalchemize.features as _features
import sqlalchemize.exceptions as _ex


def update_matching_records_session(
    sa_table: _sa.Table,
    records: _typing.Sequence[_types.Record],
    match_column_names: _typing.Sequence[str],
    session: _sa_session.Session
) -> None:
    match_values = [_records.filter_record(record, match_column_names) for record in records]
    for values, record in zip(match_values, records):
        stmt = _make_update_statement(sa_table, values, record)
        session.execute(stmt)


def update_matching_records(
    sa_table: _sa.Table,
    records: _typing.Sequence[_types.Record],
    match_column_names: _typing.Sequence[str],
    engine: _sa_engine.Engine
) -> None:
    session = _sa_session.Session(engine)
    try:
        update_matching_records_session(sa_table, records, match_column_names, session)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def update_records_session(
    sa_table: _sa.Table,
    records: _typing.Sequence[_types.Record],
    session: _sa_session.Session,
    match_column_names: _typing.Optional[_typing.Sequence[str]] = None,
) -> None:
    if _features.missing_primary_key(sa_table):
        if match_column_names is None:
            raise ValueError('Must provide match_column_names if table has no primary key.')
        update_matching_records_session(sa_table, records, match_column_names, session)
    else:
        update_records_fast_session(sa_table, records, session)


def update_records_fast_session(
    sa_table: _sa.Table,
    records: _typing.Sequence[_types.Record],
    session: _sa_session.Session
) -> None:
    """Fast update needs primary key."""
    table_name = sa_table.name
    table_class = _features.get_class(table_name, session, schema=sa_table.schema)
    mapper = _sa.inspect(table_class)
    session.bulk_update_mappings(mapper, records)


def _make_update_statement(table, record_values, new_values):
    up = _sa.update(table)
    for col, val in record_values.items():
        up = up.where(table.c[col]==val)
    return up.values(**new_values)


def update_records(
    sa_table: _sa.Table,
    records: _typing.Sequence[_types.Record],
    engine: _typing.Optional[_sa_engine.Engine] = None,
    match_column_names: _typing.Optional[_typing.Sequence[str]] = None,
) -> None:
    engine = _ex.check_for_engine(sa_table, engine)
    session = _sa_session.Session(engine)
    try:
        update_records_session(sa_table, records, session, match_column_names)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def _make_update_statement_column_value(
    table: _sa.Table,
    column_name: str,
    value: _typing.Any
):
    new_value = {column_name: value}
    return _sa.update(table).values(**new_value)


def set_column_values_session(
    table: _sa.Table,
    column_name: str,
    value: _typing.Any,
    session: _sa_session.Session
) -> None:
    stmt = _make_update_statement_column_value(table, column_name, value)
    session.add(stmt)


def set_column_values(
    table: _sa.Table,
    column_name: str,
    value: _typing.Any,
    engine: _sa_engine.Engine
) -> None:
    session = _sa_session.Session(engine)
    try:
        set_column_values_session(table, column_name, value, session)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e