![SQLAlchemize Logo](https://raw.githubusercontent.com/eddiethedean/sqlalchemize/main/docs/sqllogo.png)
-----------------

# SQLAlchemize: Easy to use functions for sql table changes
[![PyPI Latest Release](https://img.shields.io/pypi/v/sqlalchemize.svg)](https://pypi.org/project/sqlalchemize/)
![Tests](https://github.com/eddiethedean/sqlalchemize/actions/workflows/tests.yml/badge.svg)

## What is it?

**SQLAlchemize** is a Python package with easy to use functions for inserting, deleting, updating, selecting sql tables.

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/eddiethedean/sqlalchemize

```sh
# PyPI
pip install sqlalchemize
```

## Dependencies
- [SQLAlchemy - Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL](https://www.sqlalchemy.org/)


## Example
```sh
import sqlalchemy as sa
import sqlalchemize as sz

# Create SqlAlchemy engine to connect to database.
engine = sa.create_engine('sqlite:///foo.db')

# Get a sqlalchemy table to pass to sqlalchemize functions
table = sz.features.get_table('xy', engine)

# Select records
sz.select.select_all_records(table)
[{'id': 1, 'x': 1, 'y': 2}, {'id': 1, 'x': 2, 'y': 3}]

# Insert records
sz.insert.insert_records(table, [{'id': 3, 'x': 3, 'y': 4}, {'id': 4, 'x': 5, 'y': 6}])

# Delete records
sz.delete.delete_records(table, 'id', [1, 3])

# Update records
sz.update.update_records(table, [{'id': 1, 'x': 11, 'y': 22}, {'id': 1, 'x': 23, 'y': 34}], 'id')
```