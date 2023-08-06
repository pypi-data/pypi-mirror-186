import typing as _t


def filter_record(
    record: _t.Mapping[str, _t.Any],
    column_names: _t.Sequence[str]
) -> dict[str, _t.Any]:
    return {column_name: record[column_name] for column_name in column_names}