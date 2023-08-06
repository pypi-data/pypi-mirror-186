"""
Subpackage for database interface classes (both synchronous and asynchronous)

The interfaces give easy access to functionality from the other modules,
such as query statements, execution and results.

A session manager is also provided from which to acquire connections.

# Usage
---
> **_Note_** The examples below will use the synchronous oracle interface,
but they are equally applicable to the asynchronous interface with the usage of async and await.

---

A simple usage would be to acquire a connection with the session manager and then execute a string of SQL.
## Basic Example
>>> db_iface = geneity_oracle.setup_sync_db_iface()
>>> with db_iface.session_pool_manager:
...     results = db_iface.execute_sql("select * from toperator", tag="get_operators")

## Stored Statement Example
A more common usage in a service with a reusable statement would be to create a statement object,
store it and then use it via its tag/name in the execution.
>>> db_iface.store(DBSQLStatement("select * from toperator where operator_code = :operator_code", tag="get_operators"))
>>> with db_iface.session_pool_manager:
...     results = db_iface.execute("get_operators", {"operator_code": "GLOBAL"})

"""