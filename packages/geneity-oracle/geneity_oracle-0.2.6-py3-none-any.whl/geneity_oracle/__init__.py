"""
Package for an interface over cx_Oracle database calls.

# Features

- Synchronous DB interface
- Asynchronous DB interface (using asyncio and thread pool)
- Local cache store for DB statements
- Customisable DB statement objects
- Default and configurable settings (mostly for customising cx_Oracle behind the interface)

# Usage

## Setup
Basic setup can be done for either the synchronous or asynchronous interface.
This would be using either `setup_sync_db_iface` or `setup_async_db_iface`

### Example
>>> db_iface = setup_sync_db_iface("sb_admin")
>>> with db_iface.session_pool_manager:
>>>     results = db_iface.execute_sql("select * from toperator", tag="get_operators")

## Connection Settings
Default connection settings would be used when setting up a DB interface.
If alternative settings are desired then there are a couple of options:

- Explicitly set (override) the default settings with a call to `set_default_connection_settings`
- Pass settings through with setup call for the desired interface

See `settings.ConnectionSettings` for more details

### Example
>>> sportsbook_connection_settings = ConnectionSettings.new_from_defaults(
...     threaded=True,
...     min_sessions=1,
...     max_sessions=5,
... )
>>> set_default_connection_settings(sportsbook_connection_settings)
>>> db_iface = setup_sync_db_iface("sb_admin")

## Synchronous vs Asynchronous
Synchronous is based on past usage of the cx_Oracle library.
It blocks code from progressing until a response is available.

Asynchronous is intended for use with asyncio.
It allows for other coroutines to continue, while another thread makes the blocking io call.

## Module components
All of the main components can and mostly should be accessed via the interface.

The diagram roughly shows the interaction between the different components

```
                                +---------------+
               +--------------->|Query          |
               |                |Statement Store|
               |                +---------------+
               |                   |
               v                   v
      +---------------+         +---------+
<---->|DB Interface   |-------->|Query    |
      |(sync or async)|         |Execution|
      +---------------+         +---------+
               ^                   |
               |                   v
               |                +-------+
               +----------------|Query  |
                                |Results|
                                +-------+
```

For more queries that are more complex than the settings this library provides access to,
you may want override and customise:

 - Statement `query.statement.DBStatement`
 - Executor `query.execution.QueryExecutor`
 - Results `query.results.DBResults`

"""
from typing import Optional

from .interface.ora_sync import (
    SyncSessionPoolManager,
    SyncDatabaseInterface,
)

from .interface.ora_async import (
    AsyncSessionPoolManager,
    AsyncDatabaseInterface,
)
from .settings import CursorSettings, ConnectionSettings

__all__ = [
    "set_default_connection_settings",
    "setup_async_db_iface",
    "get_async_db_iface",
    "setup_sync_db_iface",
    "get_sync_db_iface",
]

__pdoc__ = {
    "utils": False,
}


def set_default_connection_settings(connection_settings: Optional[ConnectionSettings] = None):
    ConnectionSettings.set_default(connection_settings)


def setup_async_db_iface(user: str = "sb_admin") -> AsyncDatabaseInterface:
    session_pool_manager = AsyncSessionPoolManager.create_from_settings(user)
    db_iface = AsyncDatabaseInterface(session_pool_manager)
    AsyncDatabaseInterface.set_instance(db_iface)
    return db_iface


def create_async_db_iface(
    user: str = "sb_admin",
    connection_settings: Optional[ConnectionSettings] = None,
) -> AsyncDatabaseInterface:
    session_pool_manager = AsyncSessionPoolManager.create_from_settings(user, connection_settings)
    db_iface = AsyncDatabaseInterface(session_pool_manager)
    return db_iface


def get_async_db_iface() -> AsyncDatabaseInterface:
    return AsyncDatabaseInterface.get_instance()


def setup_sync_db_iface(user: str = "sb_admin") -> SyncDatabaseInterface:
    session_pool_manager = SyncSessionPoolManager.create_from_settings(user)
    db_iface = SyncDatabaseInterface(session_pool_manager)
    SyncDatabaseInterface.set_instance(db_iface)
    return db_iface


def create_sync_db_iface(
    user: str = "sb_admin",
    connection_settings: Optional[ConnectionSettings] = None,
) -> SyncDatabaseInterface:
    session_pool_manager = SyncSessionPoolManager.create_from_settings(user, connection_settings)
    db_iface = SyncDatabaseInterface(session_pool_manager)
    return db_iface


def get_sync_db_iface() -> SyncDatabaseInterface:
    return SyncDatabaseInterface.get_instance()
