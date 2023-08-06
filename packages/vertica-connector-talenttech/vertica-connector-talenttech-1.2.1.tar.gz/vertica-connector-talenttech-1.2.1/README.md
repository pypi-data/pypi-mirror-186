Customized vertica connector 
==========

The Python Wrapper to vertica_python lib for reconnectiong across server nodes


Usage
```sh
pip3 install vertica-connector-talenttech
```

```python
import os
import json
from vconnector.vertica_connector import VerticaConnector

user = "test_user",
password = "test_password"
database = "test_database"
vertica_configs = json.loads(os.getenv("VERTICA_CONFIGS"))


with VerticaConnector(user=user, 
                      password=password, 
                      database=database, 
                      vertica_configs=vertica_configs) as v_connector:
      cur = v_connector.cnx.cursor()
      sql = "SELECT 1"
      cur.execute(sql)
```

VERTICA_CONFIGS variable structure
-------------
```sh
{"host": <VERTICA_HOST>,
 "port": <VERTICA_PORT>,
 "backup_server_node": [<SERVER_NODE_1>, <SERVER_NODE_2>, <SERVER_NODE_3>}
```


INSERT TABLE  EXAMPLE
-----------------------------
```
   with VerticaConnector(
            user=os.getenv("VERTICA_USER"),
            password=os.getenv("VERTICA_PASSWORD"),
            database=os.getenv("DATABASE"),
            vertica_configs=json.loads(os.getenv("VERTICA_CONFIGS")),
    ) as v_connector:
        cursor = v_connector.cnx.cursor("dict")
        cursor.execute("drop table if exists test_staging.test cascade")
        cursor.execute(
            """create table netology_staging.test
                             (
                              a int,
                              b varchar(10),
                              c long varbinary(1000),
                              d long varchar default MAPTOSTRING(c)
                             )"""
        )
        v_connector.insert(
            table_name="test",
            schema="test_staging",
            data=list(
                [
                    {
                        "a": 1,
                        "b": "test2",
                        "c": '[{"x": 1, "y": 2}, {"x": 1, "y": 2}]',
                        "d": "fuck",
                    }
                ]
            ),
        )
```