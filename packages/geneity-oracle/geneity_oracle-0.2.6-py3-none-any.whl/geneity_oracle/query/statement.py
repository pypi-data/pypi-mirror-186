from __future__ import annotations

import logging
from typing import Optional

from ..const import SQLType
from ..errors import (
    StatementDuplicateError,
    StatementNotExistsError,
)
from ..settings import CursorSettings

logger = logging.getLogger(__name__)


class DBStatementCacheStore(object):

    def __init__(self):
        self.statements = {}
        self.indexes_by_type = {
            SQLType.SQL: set([]),
            SQLType.PROC: set([]),
            SQLType.FUNC: set([]),
        }

    def store(self, name: str, statement: DBStatement):
        if name not in self.statements:
            self.statements[name] = statement
            self.indexes_by_type[statement.sql_type].add(name)
        else:
            raise StatementDuplicateError(
                name=name,
                existing_sql=self.statements[name].sql,
                attempted_sql=statement.sql,
            )

    @staticmethod
    def create_sql(sql: str, tag: str) -> DBSQLStatement:
        sql_statement = DBSQLStatement(sql, tag=tag)
        return sql_statement

    @staticmethod
    def create_proc(proc: str, tag: Optional[str] = None) -> DBProcStatement:
        if tag is None:
            tag = proc
        sql_statement = DBProcStatement(proc, tag=tag)
        return sql_statement

    @staticmethod
    def create_func(func: str, return_type: type, tag: Optional[str] = None) -> DBFuncStatement:
        if tag is None:
            tag = func
        sql_statement = DBFuncStatement(func, tag=tag, return_type=return_type)
        return sql_statement

    def store_sql(self, name: str, sql: str) -> DBSQLStatement:
        sql_statement = self.create_sql(sql, tag=name)
        self.store(name, sql_statement)
        return sql_statement

    def store_proc(self, name: str, proc: str) -> DBProcStatement:
        sql_statement = self.create_proc(proc, tag=name)
        self.store(name, sql_statement)
        return sql_statement

    def store_func(self, name: str, func: str, return_type: type) -> DBFuncStatement:
        sql_statement = self.create_func(func, tag=name, return_type=return_type)
        self.store(name, sql_statement)
        return sql_statement

    def get_stored_statement(self, name: str) -> DBStatement:
        try:
            return self.statements[name]
        except KeyError:
            raise StatementNotExistsError(name=name)


class DBStatement(object):

    def __init__(
        self,
        sql: str,
        sql_type: SQLType,
        tag: Optional[str] = None,
        cursor_settings: Optional[CursorSettings] = None
    ):
        self.sql = sql
        self.sql_type = sql_type
        self.tag = tag
        self.cursor_settings = cursor_settings


class DBSQLStatement(DBStatement):

    def __init__(self, sql: str, **kwargs):
        super(DBSQLStatement, self).__init__(sql, sql_type=SQLType.SQL, **kwargs)


class DBProcStatement(DBStatement):

    def __init__(self, sql: str, **kwargs):
        super(DBProcStatement, self).__init__(sql, sql_type=SQLType.PROC, **kwargs)

    @property
    def proc_name(self) -> str:
        return self.sql


class DBFuncStatement(DBStatement):

    def __init__(self, sql: str, return_type: type, **kwargs):
        super(DBFuncStatement, self).__init__(sql, sql_type=SQLType.FUNC, **kwargs)
        self.return_type = return_type

    @property
    def func_name(self) -> str:
        return self.sql
