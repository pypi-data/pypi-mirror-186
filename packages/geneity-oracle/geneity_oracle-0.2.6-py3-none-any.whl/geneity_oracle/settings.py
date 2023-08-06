"""
The settings module contains a collection of classes that allow for overriding default behaviour,
such as a timeout for connection settings, or amount of prefetch rows on a cursor.
"""

from __future__ import annotations

from dataclasses import dataclass, replace, asdict
from typing import Optional, ClassVar, Dict, List, Set

from cx_Oracle import (
    SPOOL_ATTRVAL_TIMEDWAIT,
)

from .config import config, ora_user_config

CxOraGetMode = int


@dataclass
class BaseSettings(object):
    """
    This is the base class for settings and simply provides a way to display the public fields for that class.
    """

    def get_public_fields(self) -> dict:
        """
        Returns:
            dict: A dictionary of the public fields, excluding private fields such as passwords or other sensitive data
        """
        return asdict(self)

    def __str__(self) -> str:
        return f"{self.__class__}({self.get_public_fields()})"

    @classmethod
    def merge(cls, *settings_objs: Optional[BaseSettings]) -> BaseSettings:
        """
        Creates an instance of the settings class, by merging multiple instances:
        prioritising values that aren't `None` from the later instances (similar to `dict.update()`).

        Example:
            >>> @dataclass
            ... class MockSettings(BaseSettings):
            ...     a = Optional[int]
            ...     b = Optional[int]
            ...     c = Optional[int]

            >>> example_merged = MockSettings.merge(
            ...     MockSettings(1, 2, 3),
            ...     MockSettings(None, 4, None),
            ...     MockSettings(5, None, None),
            ... )
            >>> print(example_merged)
            >>> # MockSettings(5, 4, 3)

        Args:
            settings_objs: Collection of settings class instances to merge together (prioritising later instances)

        Returns:
            SettingsWithDefault: The settings object with overridden values for the fields.
        """
        def _exclude_nones(k_v_pairs: List[tuple]) -> dict:
            return {
                k: v
                for k, v in k_v_pairs
                if v is not None
            }

        fields_dict = {}
        for s in settings_objs:
            if s is not None:
                fields_without_nones = asdict(s, dict_factory=_exclude_nones)
                fields_dict.update(fields_without_nones)

        return cls(**fields_dict)


@dataclass
class SettingsWithDefault(BaseSettings):
    """
    This is an extension on the base class and provides a basic default for the settings.
    Upon first trying to retrieve the default,an instance will be created and set and
    returned on that and all future calls.
    """

    DEFAULT: ClassVar[Optional[BaseSettings]] = None

    @classmethod
    def new_from_defaults(cls, **kwargs) -> SettingsWithDefault:
        """
        Creates an instance of the settings class, using a default value if none is given,
        but using the overriding value if one is provided.

        Args:
            **kwargs: Each kwarg should match a field in the settings dataclass
                and will override the default in the returned object.

        Returns:
            SettingsWithDefault: The settings object with overridden values for the fields.
        """
        return replace(cls.default(), **kwargs)

    @classmethod
    def _create_default(cls) -> SettingsWithDefault:
        """
        Should be overridden for subclasses and provide an instance with default values for that class.
        Returns:
             SettingsWithDefault: Newly created instance of class from default values
        """
        raise NotImplementedError()

    @classmethod
    def default(cls):
        """
        If a default instance already exists then it is returned, else one is created then assigned and returned.
        Returns:
            SettingsWithDefault: Default instance of class
        """
        if cls.DEFAULT is None:
            cls.set_default(cls._create_default())

        return cls.DEFAULT

    @classmethod
    def set_default(cls, default: SettingsWithDefault) -> None:
        """
        Takes an instance of the class and assigns it as the default
        Args:
            default: The instance of the settings class that should be assigned as the default
        """
        cls.DEFAULT = default


@dataclass
class OracleDSNSettings(BaseSettings):
    """
    DSN settings to be used by connections and session managers for a specific oracle user.
    """

    DEFAULT_FOR_USER: ClassVar[Dict[str, OracleDSNSettings]] = {}

    user: str
    """
    String identifying the 'user' of the oracle user - combined with postfix to create full username.
    (e.g. 'sb_admin' in 'sb_admin_dock/***@localhost')
    """

    postfix: str
    """The postfix of the oracle database (e.g. '_dock' in 'sb_admin_dock/***@localhost')"""

    password: str
    """Password for the oracle user."""

    instance: str
    """The instance of the oracle database (e.g. 'localhost' in 'sb_admin_dock/***@localhost')"""

    @property
    def username(self) -> str:
        """
        The username is the combination of the user (e.g. 'sb_admin')
        and the postfix for the environment (e.g. '_moint')
        Returns:
            The full username (e.g. 'sb_admin_moint')
        """
        return self.user + self.postfix

    @classmethod
    def new_from_defaults_for_user(cls, user: str, **kwargs) -> OracleDSNSettings:
        return replace(cls.default_for_user(user), **kwargs)

    @classmethod
    def default_for_user(cls, user: str) -> OracleDSNSettings:
        if cls.DEFAULT_FOR_USER.get(user) is None:
            if user in ora_user_config:
                if ora_user_config[user].ORA_POSTFIX is not None:
                    ora_postfix = ora_user_config[user].ORA_POSTFIX
                else:
                    ora_postfix = config.ORA_POSTFIX

                if ora_user_config[user].ORA_INST is not None:
                    ora_inst = ora_user_config[user].ORA_INST
                else:
                    ora_inst = config.ORA_INST

                cls.DEFAULT_FOR_USER[user] = cls(
                    user=ora_user_config[user].ORA_USER,
                    postfix=ora_postfix,
                    password=ora_user_config[user].ORA_PASS,
                    instance=ora_inst,
                )

        return cls.DEFAULT_FOR_USER[user]

    @classmethod
    def set_default_for_user(cls, user: str, default: BaseSettings) -> None:
        cls.DEFAULT_FOR_USER[user] = default

    def get_public_fields(self):
        settings_dict = asdict(self)
        del settings_dict["password"]
        return settings_dict


@dataclass
class ConnectionSettings(SettingsWithDefault):
    """
    The configurable connection settings that are used generally across all oracle users
    for connections and session managers.
    """

    DEFAULT: ClassVar[Optional[ConnectionSettings]] = None

    min_sessions: Optional[int] = None
    """The max value of how many sessions (connections) the session pool manages"""

    max_sessions: Optional[int] = None
    """
    The minimum value of how many sessions (connections) the session pool manages,
    and by extension the number of sessions created upon creation of the manager
    """

    threaded: Optional[bool] = None
    """Used (true) if the connection is being used over multiple threads (wraps with a mutex for thread safety)"""

    wait_timeout: Optional[int] = None
    """The amount of time before giving up on acquiring a session connection"""

    get_mode: CxOraGetMode = None
    """
    Defines the behaviour of cx_Oracle if no free sessions are available at the time of requesting
    (using SPOOL_ATTRVAL_TIMEDWAIT by default for wait_timeout)
    """

    @classmethod
    def _create_default(cls) -> ConnectionSettings:
        return cls(
            min_sessions=1,
            max_sessions=config.MAX_SESSIONS,
            threaded=True,
            wait_timeout=config.ORACLE_TIMEOUT,
            get_mode=SPOOL_ATTRVAL_TIMEDWAIT,
        )


@dataclass
class CursorSettings(SettingsWithDefault):
    """
    Cursor settings used upon execution of a database query
    """

    DEFAULT: ClassVar[Optional[CursorSettings]] = None

    array_size: Optional[int] = None
    """
    The number of rows internally fetched and buffered by internal calls to the database.
    Used by cx_Oracle.cursor and defaults to 100 if no value is provided.
    """

    prefetch_rows: Optional[int] = None
    """
    The number of rows that the Oracle Client library fetches when a SELECT statement is executed.
    Used by cx_Oracle.cursor and defaults to 100 if no value is provided.
    """

    row_factory: Optional[str] = None
    """
    By default, the rows of a query result are returned as a tuple of all the values selected.

    If a specific structured return is desired then a row_factory should be registered and set using this setting.
    'DEFAULT' or an excluded value is equivalent to the tuple described at the start.
    To register a row_factory, see: geneity_oracle.query.results
    """

    @classmethod
    def _create_default(cls) -> CursorSettings:
        return cls()
