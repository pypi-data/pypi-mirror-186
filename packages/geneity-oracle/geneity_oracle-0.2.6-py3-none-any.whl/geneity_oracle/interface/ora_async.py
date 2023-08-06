"""
Asynchronous interface is an asyncio layer over cx_Oracle call to the oracle DB.
It allows for awaiting calls instead of blocking the main thread until results are returned.

The asynchronicity is achieved by executing calls in a separate thread, with a single connection.
See `asyncio.events.AbstractEventLoop.run_in_executor`.

Whilst it is possible to secure a DB connection each time it is needed,
it is recommended that a connection is acquired using the session manager (`AsyncSessionPoolManager`)
at the start of each concurrent process in the asyncio event loop.

# Usage
## Example
>>> db_iface = geneity_oracle.setup_async_db_iface()
>>> async with db_iface.session_pool_manager:
...     results = await db_iface.execute_sql("select * from toperator", tag="get_operators")
"""
from __future__ import annotations

import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from typing import Optional, cast

from cx_Oracle import (
    SessionPool,
    Connection,
)

from .ora_base import (
    BaseSessionPoolManager,
    DatabaseInterface,
)
from ..const import SQLType
from ..query.statement import (
    DBStatement,
)
from ..query.results import (
    DBResults,
    DBResultsSQLQuery,
    DBResultsStoredProc,
    DBResultsStoredFunc,
)
from ..utils import (
    run_in_executor_with_context,
)

logger = logging.getLogger(__name__)


class AsyncSessionPoolManager(BaseSessionPoolManager):

    def __init__(self, session_pool: SessionPool) -> None:
        super(AsyncSessionPoolManager, self).__init__(session_pool=session_pool)

        if session_pool.busy > 0:
            logger.warning(
                "Session pool for AsyncSessionPoolManager is already busy. "
                "This could affect the internal async semaphore lock count"
            )

        self.async_connection_semaphore = asyncio.Semaphore(session_pool.max)

    async def acquire(self) -> Connection:
        await self.async_connection_semaphore.acquire()
        connection = self.cx_oracle_spool.acquire()
        return connection

    def release(self, connection: Connection) -> None:
        self.async_connection_semaphore.release()
        self.cx_oracle_spool.release(connection)

    async def __aenter__(self) -> Connection:
        connection = self.get_current_connection()
        if connection is None:
            connection = await self.acquire()
            self.set_current_connection(connection)
        else:
            logger.warning("Connection was previously not released correctly. Returning current connection.")
        return connection

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        connection = self.get_current_connection()
        if connection is not None:
            self.release(connection)
            self.clear_current_connection()
        else:
            logger.warning("No connection registered. Can't release.")


class AsyncDatabaseInterface(DatabaseInterface):

    def __init__(
            self,
            session_pool_manager: Optional[AsyncSessionPoolManager] = None,
            max_execution_threads: Optional[int] = None,
            **kwargs,
    ):
        super(AsyncDatabaseInterface, self).__init__(session_pool_manager=session_pool_manager, **kwargs)

        if max_execution_threads is None or max_execution_threads < 1:
            max_execution_threads = self.session_pool_manager.max_connections

        self.execution_thread_pool = ThreadPoolExecutor(
            max_workers=max_execution_threads,
        )

    async def _execute(
        self,
        statement: DBStatement,
        params: Optional[dict],
        results: DBResults,
        connection: Optional[Connection] = None,
    ) -> DBResults:
        loop = asyncio.get_running_loop()
        with self.ensure_connection(connection) as connection:
            with connection.cursor() as cursor:
                results.set_cursor(cursor)
                results = await run_in_executor_with_context(
                    loop,
                    self.execution_thread_pool,
                    partial(self.executor_manager.execute, connection, statement, params, results, cursor=cursor),
                )
        return results

    async def execute(
        self,
        name: str,
        params: Optional[dict] = None,
        connection: Optional[Connection] = None,
    ) -> DBResults:
        sql_statement = self.statement_store.get_stored_statement(name)
        results = self.results_manager.get_standard_results_for_statement(sql_statement)
        results = await self._execute(sql_statement, params, results, connection=connection)
        return results

    async def execute_sql(
        self,
        sql: str,
        tag: Optional[str] = None,
        params: Optional[dict] = None,
        connection: Optional[Connection] = None,
    ) -> DBResultsSQLQuery:
        sql_statement = self.statement_store.create_sql(sql, tag=tag)
        results = self.results_manager.get_standard_results_for_statement(sql_statement)
        results = await self._execute(sql_statement, params, results, connection=connection)
        results = cast(DBResultsSQLQuery, results)
        return results

    async def execute_proc(
        self,
        proc: str,
        tag: Optional[str] = None,
        params: Optional[dict] = None,
        connection: Optional[Connection] = None,
    ) -> DBResultsStoredProc:
        sql_statement = self.statement_store.create_proc(proc, tag=tag)
        results = self.results_manager.get_standard_results_for_statement(sql_statement)
        results = await self._execute(sql_statement, params, results, connection=connection)
        results = cast(DBResultsStoredProc, results)
        return results

    async def execute_func(
        self,
        func: str,
        return_type: type,
        tag: Optional[str] = None,
        params: Optional[dict] = None,
        connection: Optional[Connection] = None,
    ) -> DBResultsStoredFunc:
        sql_statement = self.statement_store.create_func(func, return_type, tag=tag)
        results = self.results_manager.get_standard_results_for_statement(sql_statement)
        results = await self._execute(sql_statement, params, results, connection=connection)
        results = cast(DBResultsStoredFunc, results)
        return results

    async def cursor(self):
        pass
