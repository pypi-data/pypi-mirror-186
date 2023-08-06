<h1 align="center">WALLABY data access</h1>

[![Tests](https://github.com/AusSRC/WALLABY_data_access/actions/workflows/tests.yml/badge.svg)](https://github.com/AusSRC/WALLABY_data_access/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/AusSRC/WALLABY_data_access/branch/main/graph/badge.svg?token=W8NYIB48T1)](https://codecov.io/gh/AusSRC/WALLABY_data_access)

Python module with tools for accessing internal release data from the WALLABY database

## Configuration

There are two requirements for accessing data via the module. They are:

1. Clone of [WALLABY_database](https://github.com/AusSRC/WALLABY_database) repository
2. Environment file with database credentials.

The `.env` file requires:

```
DATABASE_HOST
DATABASE_NAME
DATABASE_USER
DATABASE_PASS
```

Once these files are in your working directory you can specify them in the `connect()` function

```
import wallaby_data_access as wallaby
wallaby.connect(db='<PATH_TO_WALLABY_database>', env='<PATH_TO_.env>')
```

## Release

[Official PyPI package](https://pypi.org/project/wallaby-data-access/)

We can release to PyPI manually or automatically through our [action](.github/workflows/pypi.yml). To release manually:

```
export RELEASE_VERSION=<version>
python setup.py sdist
twine upload dist/*
```

## Coverage

<img src="https://codecov.io/gh/AusSRC/WALLABY_data_access/branch/main/graphs/tree.svg?token=W8NYIB48T1" />
