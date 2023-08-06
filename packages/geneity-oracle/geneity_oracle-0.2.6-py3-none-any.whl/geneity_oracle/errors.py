from typing import TypeVar

from cx_Oracle import Error as CxOraError

T = TypeVar("T")


class DBStatementStoreError(Exception):
    pass


class StatementNotExistsError(DBStatementStoreError):

    def __init__(self, name: str):
        self.name = name
        super(StatementNotExistsError, self).__init__(
            f"Attempted to retrieve statement which didn't exist: {name}"
        )


class StatementDuplicateError(DBStatementStoreError):

    def __init__(self, name: str, existing_sql: str, attempted_sql: str):
        self.name = name
        self.existing_sql = existing_sql
        self.attempted_sql = attempted_sql
        super(StatementDuplicateError, self).__init__(
            f"Attempted to store statement over existing statement with the same name: {name}"
        )


class DBResultsManagerError(Exception):
    pass


class ResultRowFactoryDuplicateError(DBResultsManagerError):

    def __init__(self, name: str):
        self.name = name
        super(ResultRowFactoryDuplicateError, self).__init__(
            f"Attempted to register row factory over existing row factory with the same name: {name}"
        )


class GenOracleError(Exception):
    pass


class OracleConnectionError(Exception):

    def __init__(self, username: str, instance: str, cx_ora_error: CxOraError) -> None:
        self.username = username
        self.instance = instance
        self.cx_ora_error = cx_ora_error
        super().__init__(self._error_msg)

    @property
    def _error_msg(self) -> str:
        return f"Unable to connect to oracle for {self.username}@{self.instance}, because {self.cx_ora_error}"


class NoDBInterfaceInstanceError(GenOracleError):

    def __init__(self, db_iface_cls: type) -> None:
        self.db_iface_cls = db_iface_cls
        super().__init__(self._error_msg)

    @property
    def _error_msg(self) -> str:
        return f"No DB interface registered for {self.db_iface_cls}"


class InvalidSessionPoolError(GenOracleError):

    def __init__(self, session_pool: T) -> None:
        self.session_pool = session_pool
        super().__init__(self._error_msg)

    @property
    def _error_msg(self) -> str:
        return f"No session pool registered. Currently set as {self.session_pool}"


class InvalidDBConnection(GenOracleError):

    def __init__(self) -> None:
        super().__init__(self._error_msg)

    @property
    def _error_msg(self) -> str:
        return f"No connection registered."


class QueryExecutionError(GenOracleError):

    def __init__(self, cx_ora_error: CxOraError) -> None:
        self.cx_ora_error = cx_ora_error
        super().__init__(self._error_msg)

    @property
    def _error_msg(self) -> str:
        return f"Query failed to execute, because: {self.cx_ora_error}"


class DBResultsUnavailableError(GenOracleError):

    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(self._error_msg)

    @property
    def _error_msg(self) -> str:
        return f"Query results are not available, because: {self.reason}"
