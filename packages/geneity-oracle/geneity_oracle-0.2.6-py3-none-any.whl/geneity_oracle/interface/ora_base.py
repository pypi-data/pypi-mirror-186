from __future__ import annotations

import logging
from contextvars import ContextVar
from typing import Optional, ClassVar, Callable

from cx_Oracle import (
    SessionPool,
    Connection,
    connect,
    Error as CxOraError,
)

from ..const import ODBActionType, DICT_ROW_FACTORY, RESULTS_ROW_FACTORY
from ..errors import (
    NoDBInterfaceInstanceError,
    InvalidDBConnection,
    StatementDuplicateError,
    OracleConnectionError,
)
from ..query.execution import QueryExecutionManager
from ..query.results import (
    ResultsManager,
    DBResults,
    DBResultsSQLQuery,
    DBResultsStoredProc,
    DBResultsStoredFunc,
)
from ..query.statement import (
    DBStatementCacheStore,
    DBStatement,
    DBSQLStatement,
    DBProcStatement,
    DBFuncStatement,
)
from ..settings import ConnectionSettings, OracleDSNSettings, CursorSettings
from ..utils import Timer

logger = logging.getLogger(__name__)


def create_connection_with_default_settings(user: str = "sb_admin"):
    connection_defaults = ConnectionSettings.default()
    ora_dsn_defaults = OracleDSNSettings.default_for_user(user)
    try:
        return connect(
            ora_dsn_defaults.username,
            ora_dsn_defaults.password,
            ora_dsn_defaults.instance,
            threaded=connection_defaults.threaded,
        )
    except CxOraError as e:
        raise OracleConnectionError(
            username=ora_dsn_defaults.username,
            instance=ora_dsn_defaults.instance,
            cx_ora_error=e,
        )


class BaseSessionPoolManager(object):

    def __init__(self, session_pool: SessionPool):
        self.cx_oracle_spool = session_pool
        self._connection = ContextVar("connection")

    @classmethod
    def create_from_settings(
        cls,
        user: str = "sb_admin",
        settings: Optional[ConnectionSettings] = None,
    ) -> BaseSessionPoolManager:

        if settings is None:
            settings = ConnectionSettings.default()

        ora_dsn_defaults = OracleDSNSettings.default_for_user(user)

        logger.info(
            "Creating session pool for oracle connections",
            extra={"data": {"settings": settings.get_public_fields(), "dsn": ora_dsn_defaults.get_public_fields()}}
        )
        try:
            session_pool = SessionPool(
                ora_dsn_defaults.username,
                ora_dsn_defaults.password,
                ora_dsn_defaults.instance,
                min=settings.min_sessions,
                max=settings.max_sessions,
                threaded=settings.threaded,
                getmode=settings.get_mode,
                waitTimeout=settings.wait_timeout,
            )

        except CxOraError as e:
            raise OracleConnectionError(
                username=ora_dsn_defaults.username,
                instance=ora_dsn_defaults.instance,
                cx_ora_error=e,
            )
        else:
            return cls(session_pool)

    @property
    def max_connections(self) -> int:
        return self.cx_oracle_spool.max

    def get_current_connection(self) -> Connection:
        return self._connection.get(None)

    def set_current_connection(self, connection: Connection) -> None:
        self._connection.set(connection)

    def clear_current_connection(self) -> None:
        self._connection.set(None)

    def acquire(self) -> Connection:
        connection = self.cx_oracle_spool.acquire()
        return connection

    def release(self, connection: Connection) -> None:
        self.cx_oracle_spool.release(connection)

    def close(self) -> None:
        self.cx_oracle_spool.close()


class DBTxnCtx(object):

    def __init__(self, connection: Connection):
        self.connection = connection
        self.transaction_timer = Timer("transaction_timer")
        self.commit_timer = Timer("commit_timer")
        self.rollback_timer = Timer("rollback_timer")
        self.in_txn = False

    def begin(self) -> None:
        if not self.in_txn:
            self.transaction_timer.start()
            self.connection.begin()
            self.in_txn = True
        else:
            logger.warning("Already in transaction context")

    def commit(self) -> None:
        with self.commit_timer:
            try:
                self.connection.commit()
            finally:
                self.in_txn = False

        self.transaction_timer.stop()

        logger.info(
            "Commit transaction",
            extra={"data": {
                "commit_time": f"{self.commit_timer.time_taken:.3f}",
                "transaction_time": f"{self.transaction_timer.time_taken:.3f}",
            }},
        )

    def rollback(self) -> None:
        with self.rollback_timer:
            try:
                self.connection.rollback()
            finally:
                self.in_txn = False

        self.transaction_timer.stop()

        logger.info(
            "Rollback transaction",
            extra={"data": {
                "rollback_time": f"{self.rollback_timer.time_taken:.3f}",
                "transaction_time": f"{self.transaction_timer.time_taken:.3f}",
            }},
        )

    def __enter__(self) -> Connection:
        self.begin()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is None:
            self.commit()
        else:
            self.rollback()


class DatabaseInterface(object):

    INSTANCE: ClassVar[Optional[DatabaseInterface]] = None

    def __init__(self, session_pool_manager: Optional[BaseSessionPoolManager] = None, **kwargs):
        super(DatabaseInterface, self).__init__(**kwargs)
        self.statement_store = DBStatementCacheStore()
        self.executor_manager = QueryExecutionManager()
        self.results_manager = ResultsManager.create_with_standard_row_factories()
        self.session_pool_manager = session_pool_manager
        self._txn_ctx = ContextVar("txn_ctx")

        # Basic connection: only used if session_pool_manager is not set
        self.basic_connection = None

    @classmethod
    def set_instance(cls, instance: DatabaseInterface) -> None:
        cls.INSTANCE = instance

    @classmethod
    def get_instance(cls) -> DatabaseInterface:
        if cls.INSTANCE is not None:
            return cls.INSTANCE
        else:
            raise NoDBInterfaceInstanceError(cls)

    def connect(self, refresh_connection: bool = False) -> Connection:
        if self.basic_connection:
            if refresh_connection:
                self.close()
                self.basic_connection = create_connection_with_default_settings()
        else:
            self.basic_connection = create_connection_with_default_settings()

        return self.basic_connection

    def close(self) -> None:
        try:
            self.basic_connection.close()
        except CxOraError:
            # If there is an error here that is fine - we want to be disconnected regardless
            pass
        finally:
            self.basic_connection = None

    class EnsuredConnection(object):

        def __init__(
            self,
            db_iface: DatabaseInterface,
            connection: Optional[Connection] = None,
            use_fallback: bool = True,
        ):
            self.db_iface = db_iface
            self.connection = connection
            self.use_fallback = use_fallback
            self.close_connection_on_exit = False

        def __enter__(self) -> Connection:
            if self.connection is None:
                # First port of call should be session pool
                try:
                    self.connection = self.db_iface.session_pool_manager.get_current_connection()
                except AttributeError:
                    pass
            else:
                # If a connection was passed through then this can be used
                return self.connection

            if self.connection is None:
                # Fallback to the generic/basic connection
                self.connection = self.db_iface.basic_connection
            else:
                return self.connection

            if self.connection is None:
                if self.use_fallback:
                    # If all else fails, create a temporary connection
                    self.connection = self.db_iface.connect()
                    self.close_connection_on_exit = True
                else:
                    raise InvalidDBConnection()

            return self.connection

        def __exit__(self, exc_type, exc_val, exc_tb) -> None:
            if self.close_connection_on_exit:
                self.db_iface.close()

    def ensure_connection(
        self,
        connection: Optional[Connection] = None,
        use_fallback: bool = True,
    ) -> EnsuredConnection:
        return self.EnsuredConnection(db_iface=self, connection=connection, use_fallback=use_fallback)

    def begin(self, connection: Optional[Connection] = None) -> None:
        db_txn_ctx = self._txn_ctx.get(None)
        if db_txn_ctx is None:
            db_txn_ctx = self.txn_ctx(connection)

        db_txn_ctx.begin()
        self._txn_ctx.set(db_txn_ctx)

    def commit(self, connection: Optional[Connection] = None) -> None:
        db_txn_ctx = self._txn_ctx.get(None)
        if db_txn_ctx is None:
            db_txn_ctx = self.txn_ctx(connection)

        db_txn_ctx.commit()
        self._txn_ctx.set(None)

    def rollback(self, connection: Optional[Connection] = None) -> None:
        db_txn_ctx = self._txn_ctx.get(None)
        if db_txn_ctx is None:
            db_txn_ctx = self.txn_ctx(connection)

        db_txn_ctx.rollback()
        self._txn_ctx.set(None)

    def txn_ctx(self, connection: Optional[Connection] = None) -> DBTxnCtx:
        with self.ensure_connection(connection, use_fallback=False) as connection:
            db_txn_ctx = DBTxnCtx(connection)
        self._txn_ctx.set(db_txn_ctx)
        return db_txn_ctx

    @staticmethod
    def use_named_row_factory(name: str):
        new_cursor_settings = CursorSettings.new_from_defaults(row_factory=name)
        CursorSettings.set_default(new_cursor_settings)

    @staticmethod
    def use_dict_row_factory_as_default():
        DatabaseInterface.use_named_row_factory(DICT_ROW_FACTORY)

    @staticmethod
    def use_results_row_factory_as_default():
        DatabaseInterface.use_named_row_factory(RESULTS_ROW_FACTORY)

    def register_row_factory(self, name: str, row_factory: Callable[[DBResults], Callable]):
        self.results_manager.register_row_factory(name, row_factory)

    def register_and_use_row_factory(self, name: str, row_factory: Callable[[DBResults], Callable]):
        self.register_row_factory(name, row_factory)
        self.use_named_row_factory(name)

    def store(self, statement: DBStatement, name: Optional[str] = None) -> None:
        try:
            name = name if name is not None else statement.tag
            if name is None:
                raise ValueError("name and tag cannot both be None")
            self.statement_store.store(name, statement)
        except StatementDuplicateError as e:
            logger.warning(
                "Can't store duplicated query name",
                extra={"data": {
                    "action": ODBActionType.STORE.name,
                    "name": e.name,
                    "existing_sql": e.existing_sql,
                    "attempted_sql": e.attempted_sql,
                }},
            )
        else:
            logger.info(
                "Stored DB statement",
                extra={"data": {
                    "action": ODBActionType.STORE.name,
                    "name": name,
                    "sql_type": statement.sql_type.name,
                }},
            )

    def store_sql(self, sql: str, name: str) -> DBSQLStatement:
        statement = self.statement_store.create_sql(sql, name)
        self.store(statement)
        return statement

    def store_proc(self, proc: str, name: str) -> DBProcStatement:
        statement = self.statement_store.create_proc(proc, name)
        self.store(statement)
        return statement

    def store_func(self, func: str, name: str, return_type: type) -> DBFuncStatement:
        statement = self.statement_store.create_func(func, return_type, name)
        self.store(statement)
        return statement

    def execute(
        self,
        name: str,
        params: Optional[dict] = None,
        connection: Optional[Connection] = None,
    ) -> DBResults:
        raise NotImplementedError

    def execute_sql(
        self,
        sql: str,
        tag: Optional[str] = None,
        params: Optional[dict] = None,
        connection: Optional[Connection] = None,
    ) -> DBResultsSQLQuery:
        raise NotImplementedError

    def execute_proc(
        self,
        proc: str,
        tag: Optional[str] = None,
        params: Optional[dict] = None,
        connection: Optional[Connection] = None,
    ) -> DBResultsStoredProc:
        raise NotImplementedError

    def execute_func(
        self,
        func: str,
        return_type: type,
        tag: Optional[str] = None,
        params: Optional[dict] = None,
        connection: Optional[Connection] = None,
    ) -> DBResultsStoredFunc:
        raise NotImplementedError

    def cursor(self):
        raise NotImplementedError
