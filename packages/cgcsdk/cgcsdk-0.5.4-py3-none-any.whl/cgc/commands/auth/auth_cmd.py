import os
import shutil
import click
import requests

from cgc.utils.config_utils import (
    get_config_path,
    get_namespace,
    read_from_cfg,
    add_to_config,
)
from cgc.utils.prepare_headers import get_api_url_and_prepare_headers_register
from cgc.telemetry.basic import increment_metric
from cgc.utils.message_utils import prepare_error_message, prepare_success_message
from cgc.commands.auth import auth_utils
from cgc.utils.cryptography import rsa_crypto
from cgc.utils.click_group import CustomCommand
from cgc.utils.consts.message_consts import TIMEOUT_ERROR
from cgc.utils.consts.env_consts import TMP_DIR

TMP_DIR_PATH = os.path.join(get_config_path(), TMP_DIR)


@click.command("register", cls=CustomCommand)
@click.option("--user_id", "-u", "user_id", prompt=True)
@click.option("--access_key", "-k", "access_key", prompt=True)
def auth_register(user_id: str, access_key: str):
    """Register a user in system using user id and access key.
    \f
    :param user_id: username received in invite
    :type user_id: str
    :param access_key: access key received in invite
    :type access_key: str
    """

    url, headers = get_api_url_and_prepare_headers_register(user_id, access_key)
    pub_key_bytes, priv_key_bytes = rsa_crypto.key_generate_pair()
    payload = pub_key_bytes

    try:
        res = requests.post(
            url,
            data=payload,
            headers=headers,
            allow_redirects=True,
            timeout=10,
        )

        if res.status_code != 200:
            increment_metric("auth.register.error")
            if res.status_code == 401:
                message = "Could not validate user id or access key."
                click.echo(prepare_error_message(message))
                return

            message = "Could not register user. Please try again or contact support at support@comtegra.pl."
            click.echo(prepare_error_message(message))
            return

        unzip_dir = auth_utils.save_and_unzip_file(res)
        aes_key, passwd = auth_utils.get_aes_key_and_passwd(unzip_dir, priv_key_bytes)

        add_to_config(user_id=user_id, passwd=passwd, aes_key=aes_key)
        auth_utils.auth_create_api_key()

        message = f"Register successful! You can now use the CLI. Config file is saved in {get_config_path()}"
        click.echo(prepare_success_message(message))
        increment_metric(f"{get_namespace()}.auth.register.ok")
        shutil.rmtree(TMP_DIR_PATH)
    except requests.exceptions.ReadTimeout:
        click.echo(prepare_error_message(TIMEOUT_ERROR))


@click.command("login", cls=CustomCommand)
@click.option("--user_id", "-u", "user_id", prompt=True)
@click.option("--password", "-p", "password", prompt=True, hide_input=True)
def auth_login(user_id: str, password: str):
    """Login a user in system using user id and password.
    \f
    :param user_id: username received in invite
    :type user_id: str
    :param password: password for the user
    :type password: str
    """
    read_from_cfg("user_id")
    read_from_cfg("passwd")
    add_to_config(user_id=user_id, passwd=password)
    auth_utils.auth_create_api_key()
