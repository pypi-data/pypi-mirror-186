from contextlib import closing
from dataclasses import dataclass
from importlib import resources
from pathlib import Path
from typing import Optional, Dict, Iterator

import pkg_resources
import toml

from geneity_config.config import load_dict

PKG_NAME = "geneity_oracle"
CONFIG_FOLDER_NAME = "config"
LIBRARY_CONFIG_FILENAME = "oracle_config.toml"
ORA_USERS_CONFIG_FOLDER_NAME = "oracle_users"
ORA_USERS_CONFIG_SUFFIX = "_dsn.toml"


class BaseConfig(object):

    @classmethod
    def _load_raw_config(cls, config_relative_path) -> dict:
        try:
            return cls._load_config_from_package(config_relative_path)
        except:
            return cls._load_config_from_filesystem(config_relative_path)

    @staticmethod
    def _load_config_from_package(config_relative_path: str) -> dict:
        try:
            resources.files
        except AttributeError:
            new_style_load = False
        else:
            new_style_load = True

        if new_style_load:
            resource_path = resources.files(PKG_NAME) / config_relative_path
            with resource_path.open() as config_file:
                return toml.load(config_file)
        else:
            # TODO: Deprecate this way of loading after we upgrade past python3.9
            with closing(pkg_resources.resource_stream(PKG_NAME, config_relative_path)) as config_file:
                return toml.loads(config_file.read().decode('UTF-8'))

    @staticmethod
    def _load_config_from_filesystem(config_relative_path: str) -> dict:
        library_config_file_path = Path(__file__).parent / config_relative_path
        with library_config_file_path.open() as config_file:
            return toml.load(config_file)

    @staticmethod
    def _load_raw_override_config(config_override_absolute_path: str) -> dict:
        try:
            with Path(config_override_absolute_path).open() as override_config_file:
                return toml.load(override_config_file)
        except FileNotFoundError:
            return {}

    @classmethod
    def _get_file_identifiers(cls, config_relative_dir_path: str, suffix: str) -> Iterator[str]:
        try:
            file_identifiers = cls._get_file_identifiers_from_package(config_relative_dir_path, suffix)
        except:
            file_identifiers = None

        if file_identifiers is None:
            file_identifiers = cls._get_file_identifiers_from_filesystem(config_relative_dir_path, suffix)

        return file_identifiers

    @staticmethod
    def _get_file_identifiers_from_package(config_relative_dir_path: str, suffix: str) -> Optional[Iterator[str]]:
        try:
            resources.files
        except AttributeError:
            new_style_load = False
        else:
            new_style_load = True

        if new_style_load:
            ora_users_config_base_path = resources.files(PKG_NAME) / config_relative_dir_path
            if ora_users_config_base_path.is_dir():
                def _file_identifiers_load_with_new_style():
                    for ora_user_config_filename in ora_users_config_base_path.glob(f"*{suffix}"):
                        # strips suffix off the end,
                        # so with a "_dsn.toml" suffix "sb_admin_dsn.toml" becomes "sb_admin"
                        yield ora_user_config_filename.name[:-len(suffix)]
                return _file_identifiers_load_with_new_style()
            else:
                return None
        else:
            if (
                    pkg_resources.resource_exists(PKG_NAME, config_relative_dir_path) and
                    pkg_resources.resource_listdir(PKG_NAME, config_relative_dir_path)
            ):
                def _file_identifiers_load_with_old_style():
                    for ora_user_config_filename in pkg_resources.resource_listdir(PKG_NAME, config_relative_dir_path):
                        if ora_user_config_filename[-len(suffix):] == suffix:
                            # strips suffix off the end,
                            # so with a "_dsn.toml" suffix "sb_admin_dsn.toml" becomes "sb_admin"
                            yield ora_user_config_filename[:-len(suffix)]
                return _file_identifiers_load_with_old_style()
            else:
                return None

    @staticmethod
    def _get_file_identifiers_from_filesystem(config_relative_dir_path: str, suffix: str) -> Iterator[str]:
        ora_users_config_base_path = Path(__file__).parent / config_relative_dir_path
        for ora_user_config_filename in ora_users_config_base_path.glob(f"*{suffix}"):
            # strips suffix off the end, so "sb_admin_dsn.toml" becomes "sb_admin"
            yield ora_user_config_filename.name[:-len(suffix)]


@dataclass
class Config(BaseConfig):
    """
    Base config for this geneity_oracle library.

    Defined in 'config/oracle_config.toml' and overridden if needed by '/etc/config/oracle_override.toml'.
    """

    ORA_INST: str
    """The instance of the oracle database (e.g. 'localhost' in 'sb_admin_dock/***@localhost')"""

    ORA_POSTFIX: str
    """The postfix of the oracle database (e.g. '_dock' in 'sb_admin_dock/***@localhost')"""

    MAX_SESSIONS: int
    """Used as the default value of how many sessions (connections) the session pool manages"""

    ORACLE_TIMEOUT: int
    """
    The amount of time before giving up on acquiring a session connection\n
    (translates to wait_timeout with respect to cx_Oracle)
    """

    @classmethod
    def load_raw_config(cls):
        return cls._load_raw_config(f"{CONFIG_FOLDER_NAME}/{LIBRARY_CONFIG_FILENAME}")

    @classmethod
    def load_raw_override_config(cls):
        return cls._load_raw_override_config("/etc/config/oracle_override.toml")


def _raw_library_config_from_package_resources():
    with resources.files(PKG_NAME) / CONFIG_FOLDER_NAME / LIBRARY_CONFIG_FILENAME as library_config_file:
        raw_library_config = toml.load(library_config_file)

    try:
        with Path("/etc/config/oracle_override.toml").open() as library_override_config_file:
            raw_library_override_config = toml.load(library_override_config_file)
    except FileNotFoundError:
        raw_library_override_config = {}

    return raw_library_config, raw_library_override_config


@dataclass
class OraUserConfig(BaseConfig):
    """
    Config for connection details of individual oracle users (1 per user - 1 for sb_admin, 1 for sportsbook, etc.).

    Defined in 'config/oracle_users/*_dsn.toml' and overridden by '/etc/config/*_dsn_override.toml' (* must match).

    For example: 'config/oracle_users/sb_admin_dsn.toml' is overridden by '/etc/config/sb_admin_dsn_override.toml'.
    """

    ORA_USER: str
    """
    String identifying the 'user' of the oracle user - combined with postfix to create full username.
    (e.g. 'sb_admin' in 'sb_admin_dock/***@localhost')
    """

    ORA_PASS: str
    """Password for the oracle user."""

    ORA_INST: Optional[str] = None
    """Instance for the oracle user (by default the main config instance is used)"""

    ORA_POSTFIX: Optional[str] = None
    """Postfix for the oracle user (by default the main config postfix is used)"""

    @classmethod
    def get_user_identifiers(cls):
        return cls._get_file_identifiers(
            f"{CONFIG_FOLDER_NAME}/{ORA_USERS_CONFIG_FOLDER_NAME}",
            ORA_USERS_CONFIG_SUFFIX,
        )

    @classmethod
    def load_raw_config(cls, user_identifier: str):
        return cls._load_raw_config(
            f"{CONFIG_FOLDER_NAME}/{ORA_USERS_CONFIG_FOLDER_NAME}/{user_identifier}{ORA_USERS_CONFIG_SUFFIX}"
        )

    @classmethod
    def load_raw_override_config(cls, user_identifier: str):
        return cls._load_raw_override_config(f"/etc/config/{user_identifier}_dsn_override.toml")


config = load_dict(Config, Config.load_raw_config(), Config.load_raw_override_config())


def _populate_ora_user_config() -> Dict[str, OraUserConfig]:
    ora_user_config_dict = {}
    for user_identifier in OraUserConfig.get_user_identifiers():
        ora_user_config_dict[user_identifier] = load_dict(
            OraUserConfig,
            OraUserConfig.load_raw_config(user_identifier),
            OraUserConfig.load_raw_override_config(user_identifier),
        )

    return ora_user_config_dict


ora_user_config = _populate_ora_user_config()
