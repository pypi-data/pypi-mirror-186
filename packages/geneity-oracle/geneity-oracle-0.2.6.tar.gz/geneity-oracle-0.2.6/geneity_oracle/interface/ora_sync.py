from __future__ import annotations

import logging
from typing import Optional, cast

from cx_Oracle import (
    SessionPool,
    Connection,
)

from .ora_base import (
    BaseSessionPoolManager,
    DatabaseInterface,
)
from ..query.statement import (
    DBStatement,
)
from ..query.results import (
    DBResults,
    DBResultsSQLQuery,
    DBResultsStoredProc,
    DBResultsStoredFunc,
)

logger = logging.getLogger(__name__)


class SyncSessionPoolManager(BaseSessionPoolManager):

    def __init__(self, session_pool: SessionPool) -> None:
        super(SyncSessionPoolManager, self).__init__(session_pool=session_pool)

    def __enter__(self) -> Connection:
        connection = self.get_current_connection()
        if connection is None:
            connection = self.acquire()
            self.set_current_connection(connection)
        else:
            logger.warning("Connection was previously not released correctly. Returning current connection.")
        return connection

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        connection = self.get_current_connection()
        if connection is not None:
            self.release(connection)
            self.clear_current_connection()
        else:
            logger.warning("No connection registered. Can't release.")


class SyncDatabaseInterface(DatabaseInterface):

    def _execute(
        self,
        statement: DBStatement,
        params: Optional[dict],
        results: DBResults,
        connection: Optional[Connection] = None,
    ):
        with self.ensure_connection(connection) as connection:
            cursor = connection.cursor()
            results.set_cursor(cursor)
            return self.executor_manager.execute(connection, statement, params, results, cursor=cursor)

    def execute(
        self,
        name: str,
        params: Optional[dict] = None,
        connection: Optional[Connection] = None,
    ) -> DBResults:
        sql_statement = self.statement_store.get_stored_statement(name)
        results = self.results_manager.get_standard_results_for_statement(sql_statement)
        return self._execute(sql_statement, params, results, connection=connection)

    def execute_sql(
        self,
        sql: str,
        tag: Optional[str] = None,
        params: Optional[dict] = None,
        connection: Optional[Connection] = None,
    ) -> DBResultsSQLQuery:
        sql_statement = self.statement_store.create_sql(sql, tag=tag)
        results = self.results_manager.get_standard_results_for_statement(sql_statement)
        results = self._execute(sql_statement, params, results, connection=connection)
        results = cast(DBResultsSQLQuery, results)
        return results

    def execute_proc(
        self,
        proc: str,
        tag: Optional[str] = None,
        params: Optional[dict] = None,
        connection: Optional[Connection] = None,
    ) -> DBResultsStoredProc:
        sql_statement = self.statement_store.create_proc(proc, tag=tag)
        results = self.results_manager.get_standard_results_for_statement(sql_statement)
        results = self._execute(sql_statement, params, results, connection=connection)
        results = cast(DBResultsStoredProc, results)
        return results

    def execute_func(
        self,
        func: str,
        return_type: type,
        tag: Optional[str] = None,
        params: Optional[dict] = None,
        connection: Optional[Connection] = None,
    ) -> DBResultsStoredFunc:
        sql_statement = self.statement_store.create_func(func, return_type, tag=tag)
        results = self.results_manager.get_standard_results_for_statement(sql_statement)
        results = self._execute(sql_statement, params, results, connection=connection)
        results = cast(DBResultsStoredFunc, results)
        return results

    def cursor(self):
        pass
