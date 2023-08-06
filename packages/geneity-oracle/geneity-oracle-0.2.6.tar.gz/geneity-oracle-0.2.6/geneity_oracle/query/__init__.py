"""
Subpackage for query stages: statement, execution and results.

Statements, executors and results are just the sequential parts required to complete and utilise a database query.

A statement is created. It is then given to the executor to make a call to the database with.
After this, the results are returned and used as desired.

# Usage
In large part, this functionality is available by the database interface in the `geneity_oracle.interface` submodule,
but it is sometimes worth using the classes and functions available in this submodule directly when more customisation
is needed.

## Statements
Perhaps the most important part for general use is the statements.

There is a `geneity_oracle.query.statement.DBStatementCacheStore` to manage all of the statements stored by name.
>>> sql_statement = DBStatementCacheStore.create_sql(
...     "select * from toperator where operator_code = :operator_code",
...     tag="get_operators",
... )
>>> statement_store = DBStatementCacheStore()
>>> statement_store.store(sql_statement)

## Execution
There is an execution manager that can take a statement and dispatch to the correct executor,
which in turn makes the DB call.

>>> execution_manager = QueryExecutionManager()
>>> connection = cx_Oracle.connect("sb_admin_dock", "sb_admin_dock", "localhost")
>>> sql_results = execution_manager.execute(connection, sql_statement, params={"operator_code": "GLOBAL"})

## Results
Retrieved from the executor (usually via the interface/execution manager),
the results give access to the results of a DB call (sql/proc/func).
The results are usually retrieved in full and returned as an iterable from the results object.
>>> print("Results:")
... for row in sql_results.results:
...     print(row)
"""
from .statement import (
    DBStatementCacheStore,
    DBStatement,
    DBSQLStatement,
    DBProcStatement,
    DBFuncStatement,
)

from .execution import (
    QueryExecutionManager,
    QueryExecutor,
    DBResultsSQLQuery,
    ProcExecutor,
    FuncExecutor,
)

from .results import (
    DBResults,
    DBResultsSQLQuery,
    DBResultsStoredProc,
    DBResultsStoredFunc,
)
