from __future__ import annotations

import logging
from typing import Any, Dict, Optional, Callable, Type

from cx_Oracle import (
    Cursor
)

from geneity_logger.context import set_context
from .statement import DBStatement
from ..const import SQLType, DEFAULT_ROW_FACTORY, DICT_ROW_FACTORY, RESULTS_ROW_FACTORY
from ..errors import ResultRowFactoryDuplicateError
from ..ora_types import ora_params
from ..settings import CursorSettings

logger = logging.getLogger(__name__)


class ResultsManager(object):

    def __init__(self):
        self.standard_results_by_type: Dict[SQLType, Optional[Type[DBResults]]] = {
            SQLType.SQL: DBResultsSQLQuery,
            SQLType.PROC: DBResultsStoredProc,
            SQLType.FUNC: DBResultsStoredFunc,
        }

        self.cursor_results_by_type: Dict[SQLType, Optional[Type[DBResults]]] = {
            SQLType.SQL: None,
            SQLType.PROC: None,
            SQLType.FUNC: None,
        }

        self.row_factories: Dict[str, Callable[[DBResults], Callable]] = {}
        self.output_types_converters: Dict[type, Callable] = {}

    def get_standard_results_for_statement(self, statement: DBStatement, cursor: Optional[Cursor] = None):
        results_cls = self.standard_results_by_type[statement.sql_type]
        if results_cls is None:
            return None
        else:
            return results_cls(statement, cursor=cursor, results_manager=self)

    def get_cursor_results_for_statement(self, statement: DBStatement, cursor: Optional[Cursor] = None):
        results_cls = self.cursor_results_by_type[statement.sql_type]
        if results_cls is None:
            return None
        else:
            return results_cls(statement, cursor=cursor, results_manager=self)

    @classmethod
    def create_with_standard_row_factories(cls):
        results_manager = cls()
        register_standard_row_factories(results_manager)
        return results_manager

    def register_row_factory(self, name: str, row_factory: Callable[[DBResults], Callable]):
        if name in self.row_factories:
            raise ResultRowFactoryDuplicateError(name)

        self.row_factories[name] = row_factory

    def get_row_factory(self, name: Optional[str], results: DBResults) -> Optional[Callable]:
        if name in (DEFAULT_ROW_FACTORY, None):
            return None

        if name in self.row_factories:
            return self.row_factories[name](results)
        else:
            logger.warning(f"{name} not a registered row factory. Falling back to default")
            return None


def register_standard_row_factories(results_manager: ResultsManager):
    results_manager.register_row_factory(DICT_ROW_FACTORY, dict_row_factory)
    results_manager.register_row_factory(RESULTS_ROW_FACTORY, DBResultsRow.create_row_factory)


def dict_row_factory(results: DBResults):
    def _dict_row_factory_internal(*args):
        columns = [col[0].lower() for col in results.cursor.description]
        return dict(zip(columns, args))
    return _dict_row_factory_internal


class DBResultsRow(object):

    def __init__(
        self,
        data: Dict[str, Any],
        column_ids: Dict[str, int],
        result_set: Optional[DBResults] = None,
    ):
        self.data = data
        self.column_ids = column_ids
        self.result_set = result_set

    @classmethod
    def create_row_factory(cls, results: DBResults):
        def _results_row_factory(*args):
            columns = [col[0].lower() for col in results.cursor.description]
            data = dict(zip(columns, args))
            column_ids = {col: i for i, col in enumerate(columns)}
            return cls(data=data, column_ids=column_ids, result_set=results)
        return _results_row_factory

    def get_col_value(self, col_name: str):
        return self.data[col_name]

    def __getitem__(self, item):
        return self.data[item]

    def __getattr__(self, item):
        try:
            return self.data[item]
        except KeyError:
            try:
                return super(DBResultsRow, self).__getattr__(item)
            except AttributeError:
                pass

            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{item}'. Not in `self.data`"
            )

    def get(self, item, default: Any = None):
        try:
            return self.data[item]
        except KeyError:
            return default


class DBResults(object):

    def __init__(
        self,
        statement: DBStatement,
        cursor: [Cursor] = None,
        results_manager: Optional[ResultsManager] = None,
    ):
        self.statement = statement
        self.cursor = cursor
        self.results_manager = results_manager
        self.results = None
        self.results_available = False

        self.prefetch_rows: Optional[int] = None
        self.array_size: Optional[int] = None
        self.row_factory_name: Optional[str] = None

    def fetch_results(self) -> DBResults:
        raise NotImplementedError()

    def __iter__(self):
        if self.results is not None:
            return iter(self.results)
        else:
            return iter(())

    def __len__(self):
        return len(self.results)

    def __getitem__(self, item):
        return self.results[item]

    def set_results_manager(self, results_manager: ResultsManager):
        self.results_manager = results_manager

    def set_cursor(self, cursor: Cursor):
        self.cursor = cursor

    def update_from_settings(self, settings: CursorSettings):
        self.prefetch_rows = settings.prefetch_rows
        self.array_size = settings.array_size
        self.row_factory_name = settings.row_factory

    def update_cursor_pre_execution(self) -> None:
        if self.prefetch_rows is not None:
            self.cursor.prefetchrows = self.prefetch_rows

        if self.array_size is not None:
            self.cursor.arraysize = self.array_size

    def update_cursor_post_execution(self) -> None:
        self.cursor.rowfactory = self.results_manager.get_row_factory(self.row_factory_name, results=self)


class DBResultsSQLQuery(DBResults):

    def __init__(
        self,
        statement: DBStatement,
        cursor: [Cursor] = None,
        results_manager: Optional[ResultsManager] = None,
    ):
        super(DBResultsSQLQuery, self).__init__(
            statement,
            cursor=cursor,
            results_manager=results_manager,
        )

    @property
    def num_rows(self) -> int:
        return self.cursor.rowcount

    def fetch_results(self) -> DBResults:
        with set_context(sql_tag=self.statement.tag):
            logger.debug("Fetching results")
            if self.results is None and self.cursor.description is not None:
                self.results = self.cursor.fetchall()
                self.results_available = True
            else:
                logger.debug(
                    "Results not fetchable",
                    extra={"data": {"results": self.results, "description": self.cursor.description}},
                )

            return self


class DBResultsStoredProc(DBResults):

    def __init__(
        self,
        statement: DBStatement,
        cursor: [Cursor] = None,
        results_manager: Optional[ResultsManager] = None,
        params: Optional[ora_params] = None,
    ):
        super(DBResultsStoredProc, self).__init__(
            statement,
            cursor=cursor,
            results_manager=results_manager,
        )
        self.params = params

    def fetch_results(self) -> DBResults:
        # proc doesn't fetch results unless it has an explicit refcursor argument as an output param
        # but the refcursor functionality isn't implemented in geneity_oracle yet and so this should be handled manually
        self.results = self.params
        self.results_available = True
        return self

    def set_params(self, params: ora_params):
        self.params = params


class DBResultsStoredFunc(DBResults):

    def __init__(
        self,
        statement: DBStatement,
        cursor: [Cursor] = None,
        results_manager: Optional[ResultsManager] = None,
        params: Optional[ora_params] = None,
    ):
        super(DBResultsStoredFunc, self).__init__(
            statement,
            cursor=cursor,
            results_manager=results_manager,
        )
        self.params = params
        self.return_value = None

    def fetch_results(self) -> DBResults:
        # func doesn't fetch results unless it has an explicit refcursor argument as an output param
        # but the refcursor functionality isn't implemented in geneity_oracle yet and so this should be handled manually
        self.results = self.params
        self.results_available = True
        return self

    def set_params(self, params: ora_params):
        self.params = params

    def set_return_value(self, value) -> Any:
        self.return_value = value


