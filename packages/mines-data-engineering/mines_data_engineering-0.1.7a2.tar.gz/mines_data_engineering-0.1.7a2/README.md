# Mines Data Engineering

This package simplifies the process of starting common database systems in the background on Singularity Hub.

## Supported Databases

- MongoDB
- TimescaleDB (and Postgres)

## Examples

### MongoDB

```python
from mines_data_engineering import start_mongo
import pymongo

# will need wait a couple minutes the first time this happens
# while Singularity downloads and converts the Docker image
connection_string = start_mongo()

client = pymongo.MongoClient(connection_string)
client.my_db.my_col.insert_one({'finally': 'working'})
```

### Postgres/TimescaleDB

```python
from mines_data_engineering import start_postgres
import psycopg2


# will need wait a couple minutes the first time this happens
# while Singularity downloads and converts the Docker image
connection_string = start_postgres()

conn = psycopg2.connect(connection_string)
cur = conn.cursor()
cur.execute("SELECT 1")
assert next(cur) == (1,)
```
