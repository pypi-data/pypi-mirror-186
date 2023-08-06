import logging
from typing import Optional, Dict, Type, cast

from cx_Oracle import (
    Cursor,
    Connection,
    Error as CxOraError,
    Var,
)

from .results import (
    DBResults,
    DBResultsSQLQuery,
    DBResultsStoredProc,
    DBResultsStoredFunc,
)
from .statement import (
    DBStatement,
    DBSQLStatement,
    DBProcStatement,
    DBFuncStatement,
)
from ..const import SQLType, LONG_QUERY_THRESHOLD
from ..errors import (
    DBResultsUnavailableError,
    QueryExecutionError,
)
from ..ora_types import ora_params, OraCustomType
from ..settings import CursorSettings
from ..utils import Timer

logger = logging.getLogger(__name__)


class QueryExecutionManager(object):

    def __init__(self):
        self.executors_by_type: Dict[SQLType, Optional[Type[QueryExecutor]]] = {
            SQLType.SQL: SQLExecutor,
            SQLType.PROC: ProcExecutor,
            SQLType.FUNC: FuncExecutor,
        }

        self.cursors_by_type: Dict[SQLType, Optional[Type[QueryExecutor]]] = {
            SQLType.SQL: None,
            SQLType.PROC: None,
            SQLType.FUNC: None,
        }

    def execute(
        self,
        connection: Connection,
        statement: DBStatement,
        params: Optional[ora_params],
        results: Optional[DBResults] = None,
        cursor: Optional[Cursor] = None,
        settings: Optional[CursorSettings] = None,
    ) -> Optional[DBResults]:
        executor_cls = self.executors_by_type.get(statement.sql_type)
        if executor_cls is None:
            logger.error(
                "No executor available for type",
                extra={"data": {"sql_type": statement.sql_type}},
            )
            return None
        else:
            cursor_settings = CursorSettings.merge(CursorSettings.default(), statement.cursor_settings, settings)
            results.update_from_settings(cursor_settings)

            executor = executor_cls(connection, statement, params=params, results=results, cursor=cursor)
            return executor.execute()

    def cursor(self):
        pass


class QueryExecutor(object):

    def __init__(
        self,
        connection: Connection,
        statement: DBStatement,
        params: Optional[ora_params] = None,
        results: Optional[DBResults] = None,
        cursor: Optional[Cursor] = None,
    ):
        self.cursor: Cursor = cursor if cursor is not None else connection.cursor()
        self.statement = statement
        self.params = params
        self.query_executed = False
        self.query_failed = False
        self.execute_timer = Timer()

        self._results: Optional[DBResults] = results

    def _execute(self) -> None:
        raise NotImplementedError()

    def _update_cursor_pre_execution(self):
        self._results.update_cursor_pre_execution()

    def _update_cursor_post_execution(self):
        self._results.update_cursor_post_execution()

    def execute(self) -> Optional[DBResults]:
        self._update_cursor_pre_execution()
        try:
            with self.execute_timer:
                log_params = None
                if self.params is not None:
                    log_params = self.params.copy()
                    for k, v in self.params.items():
                        if isinstance(v, type):
                            self.params[k] = self.cursor.var(v)
                            del log_params[k]
                        elif isinstance(v, OraCustomType):
                            cursor_var_kwargs = v.get_as_cursor_var_kwargs()
                            self.params[k] = self.cursor.var(v.ora_type, **cursor_var_kwargs)
                            del log_params[k]

                logger.info("Executing Oracle DB call", extra={"data": {
                    "type": self.statement.sql_type.value,
                    "query_name": self.statement.tag,
                    "params": log_params,
                }})
                self._execute()
                self.query_executed = True
                self._update_cursor_post_execution()
                self.results.fetch_results()
        except CxOraError as e:
            self.query_failed = True
            raise QueryExecutionError(cx_ora_error=e)
        else:
            if self.execute_time > LONG_QUERY_THRESHOLD:
                log_handler_func = logger.warning
            else:
                log_handler_func = logger.info

            log_handler_func("Finished executing Oracle DB call", extra={"data": {
                "type": self.statement.sql_type.value,
                "query_name": self.statement.tag,
                "execution_time": f"{self.execute_time:.3f}"
            }})

        return self.results

    @property
    def execute_time(self) -> Optional[float]:
        return self.execute_timer.time_taken

    @property
    def results(self) -> Optional[DBResults]:
        if not self.query_executed:
            raise DBResultsUnavailableError(
                "query not yet executed"
            )

        if self.query_failed:
            raise DBResultsUnavailableError(
                "query failed execution"
            )

        if self._results is None:
            raise DBResultsUnavailableError(
                "results are NoneType"
            )

        return self._results


class SQLExecutor(QueryExecutor):

    def __init__(
        self,
        connection: Connection,
        statement: DBStatement,
        params: Optional[ora_params] = None,
        results: Optional[DBResults] = None,
        cursor: Optional[Cursor] = None,
    ):
        super(SQLExecutor, self).__init__(
            connection,
            statement,
            params=params,
            results=results,
            cursor=cursor,
        )
        self.statement: DBSQLStatement = cast(DBSQLStatement, self.statement)

        self._results: DBResultsSQLQuery = cast(DBResultsSQLQuery, self._results)

    def _execute(self) -> None:
        if self.params is not None:
            self.cursor.execute(self.statement.sql, self.params)
        else:
            self.cursor.execute(self.statement.sql)


class ProcExecutor(QueryExecutor):

    def __init__(
        self,
        connection: Connection,
        statement: DBStatement,
        params: Optional[ora_params] = None,
        results: Optional[DBResults] = None,
        cursor: Optional[Cursor] = None,
    ):
        super(ProcExecutor, self).__init__(
            connection,
            statement,
            params=params,
            results=results,
            cursor=cursor,
        )
        self.statement: DBProcStatement = cast(DBProcStatement, self.statement)

        self._results: DBResultsStoredProc = cast(DBResultsStoredProc, self._results)

    def _execute(self) -> None:
        self._results.set_params(self.params)
        if self.params is not None:
            self.cursor.callproc(self.statement.proc_name, keywordParameters=self.params)
        else:
            self.cursor.callproc(self.statement.proc_name)


class FuncExecutor(QueryExecutor):

    def __init__(
        self,
        connection: Connection,
        statement: DBStatement,
        params: Optional[ora_params] = None,
        results: Optional[DBResults] = None,
        cursor: Optional[Cursor] = None,
    ):
        super(FuncExecutor, self).__init__(
            connection,
            statement,
            params=params,
            results=results,
            cursor=cursor,
        )
        self.statement: DBFuncStatement = cast(DBFuncStatement, self.statement)

        self._results: DBResultsStoredFunc = cast(DBResultsStoredFunc, self._results)

    def _execute(self) -> None:
        self._results.set_params(self.params)
        if self.params is not None:
            # TODO: refactor parameters
            value = self.cursor.callfunc(
                self.statement.func_name,
                self.statement.return_type,
                keywordParameters=self.params,
            )
        else:
            value = self.cursor.callfunc(self.statement.func_name, self.statement.return_type)

        self._results.set_return_value(value)
