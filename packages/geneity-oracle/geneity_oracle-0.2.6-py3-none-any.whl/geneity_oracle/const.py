from enum import Enum

# The length of time (in seconds) after which the query is considered long running
LONG_QUERY_THRESHOLD = 0.5


class SQLType(Enum):
    SQL = "SQL"
    PROC = "PROC"
    FUNC = "FUNC"


class ODBActionType(Enum):
    STORE = "STORE"
    EXECUTE = "EXECUTE"


DEFAULT_ROW_FACTORY = "DEFAULT"
DICT_ROW_FACTORY = "Dict"
RESULTS_ROW_FACTORY = "DBResultsRow"
