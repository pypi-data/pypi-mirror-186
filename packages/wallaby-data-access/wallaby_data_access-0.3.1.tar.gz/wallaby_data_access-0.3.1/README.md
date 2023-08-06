# WALLABY data access

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
