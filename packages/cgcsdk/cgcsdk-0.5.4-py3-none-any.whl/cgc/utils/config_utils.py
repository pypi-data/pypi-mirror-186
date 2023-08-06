import json
import os
import sys
import click

from cgc.utils.message_utils import prepare_error_message
from cgc.utils.consts.env_consts import CONFIG_FILE_NAME


def get_config_path():
    """Function to get the path to the config file

    :return: path to the config file
    :rtype: str
    """
    try:
        config_path = os.path.join(
            os.environ.get("APPDATA")
            or os.environ.get("XDG_CONFIG_HOME")
            or os.path.join(os.environ["HOME"], ".config"),
            "cgcsdk",
        )
    except KeyError:
        message = "Could not validate config path, try again or contact support at support@comtegra.pl"
        click.echo(prepare_error_message(message))
        sys.exit()

    return config_path


def add_to_config(**kwargs):
    """Function allowing adding a variable number of key-value pairs to the config file.
    If config file does not exist, it is created, otherwise key-value pairs are appended to existing config.
    Values for existing keys are overwritten.

    :param kwargs: key-value pairs to be saved in the config file
    :type kwargs: dict
    """
    config_path = get_config_path()
    user_config_file = os.path.join(config_path, CONFIG_FILE_NAME)
    read_cfg = {}
    if not os.path.isdir(config_path):
        os.makedirs(config_path)
    try:
        f = open(user_config_file, "r+", encoding="UTF-8")
        read_cfg = json.load(f)
    except FileNotFoundError:
        pass

    with open(user_config_file, "w", encoding="UTF-8") as f:
        final_cfg = {**read_cfg, **kwargs}
        json.dump(final_cfg, f)


def read_from_cfg(key: str):
    """Function to read a single value from config

    :param key: key name to read the value from config
    :type key: str
    :return: value for the provided key
    :rtype: _type_
    """
    config_path = get_config_path()
    user_config_file = os.path.join(config_path, CONFIG_FILE_NAME)
    try:
        f = open(user_config_file, "r+", encoding="UTF-8")
        read_cfg = json.load(f)
        return read_cfg[key]
    except FileNotFoundError:
        print("No config file found. Please use cgc register first.")
        sys.exit()
    except KeyError:
        print("Config file is corrupted. Please contact support at support@comtegra.pl")
        sys.exit()


def get_namespace() -> str:
    """Function to get the namespace from the config file

    :return: namespace
    :rtype: str
    """
    return read_from_cfg("namespace")
