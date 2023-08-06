import json
import os
import shutil
import glob
import base64
import urllib
import click
import requests

from cgc.utils.config_utils import get_config_path, get_namespace
from cgc.telemetry.basic import increment_metric
from cgc.utils.config_utils import add_to_config
from cgc.utils.config_utils import read_from_cfg
from cgc.utils.message_utils import prepare_error_message
from cgc.utils.cryptography import rsa_crypto
from cgc.utils import prepare_headers
from cgc.utils.consts.message_consts import TIMEOUT_ERROR
from cgc.utils.consts.env_consts import API_URL, TMP_DIR

TMP_DIR_PATH = os.path.join(get_config_path(), TMP_DIR)


def get_jwt() -> str:
    """Function to get JWT token and api key for user

    :param username: _description_
    :type username: str
    :param password: _description_
    :type password: str
    """

    user_id = urllib.parse.quote(read_from_cfg("user_id"))
    passwd = urllib.parse.quote(read_from_cfg("passwd"))
    url = f"{API_URL}/v1/api/user/create/token"
    payload = f"grant_type=&username={user_id}&password={passwd}"

    jwt_headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    try:
        res = requests.post(
            url,
            payload,
            headers=jwt_headers,
            timeout=10,
        )

        if res.status_code != 200:
            message = (
                "Could not generate JWT. Try again or contact us at support@comtegra.pl"
            )
            click.echo(prepare_error_message(message))
            increment_metric(f"{get_namespace()}.auth.jwt.error")
            return None
        increment_metric(f"{get_namespace()}.auth.jwt.ok")

        data = json.loads(res.text)
        jwt = data["access_token"]
        return jwt

    except requests.exceptions.ReadTimeout:
        click.echo(prepare_error_message(TIMEOUT_ERROR))


def auth_create_api_key():
    """Function to create API key and API secret for user and save it to config file."""
    url = f"{API_URL}/v1/api/user/create/api-key"
    headers = prepare_headers.prepare_headers_api_key()
    try:
        res = requests.post(
            url,
            headers=headers,
            timeout=10,
        )

        if res.status_code != 200:
            message = "Could not generate API key. Try again or contact us at support@comtegra.pl"
            click.echo(prepare_error_message(message))
            increment_metric(f"{get_namespace()}.auth.api-key.error")
            return
        increment_metric(f"{get_namespace()}.auth.api-key.ok")

        data = json.loads(res.text)

        api_key = data["details"].get("_id")
        secret = data["details"].get("secret")

        add_to_config(api_key=api_key, api_secret=secret)

    except requests.exceptions.ReadTimeout:
        click.echo(prepare_error_message(TIMEOUT_ERROR))


def save_and_unzip_file(res: requests.Response) -> str:
    """Function to save file, unzip it and return path to its directory.

    :param res: API response with file to save and unzip
    :type res: requests.Response
    :return: path to the directory containing the file
    :rtype: str
    """
    zip_file = res.headers.get("content-disposition").split('"')[1]
    namespace = zip_file.split("---")[-1].split(".")[0]
    add_to_config(namespace=namespace)

    if not os.path.isdir(TMP_DIR_PATH):
        os.makedirs(TMP_DIR_PATH)
    zip_file_path = f"{TMP_DIR_PATH}/{zip_file}"
    with open(zip_file_path, "wb") as f:
        f.write(res.content)

    unzip_dir = zip_file_path[:-4]
    shutil.unpack_archive(zip_file_path, unzip_dir)

    return unzip_dir


def get_aes_key_and_passwd(unzip_dir: str, priv_key_bytes: bytes):
    """Function to get AES key and password from the unzipped file.

    :param unzip_dir: path to the directory containing the file
    :type unzip_dir: str
    :param priv_key_bytes: private key bytes
    :type priv_key_bytes: bytes
    :return: AES key and password
    :rtype: str, str
    """
    encrypted_passwd_path = ""
    encrypted_aes_path = ""
    for file in glob.glob(
        f"{unzip_dir}/**/*encrypted*",
        recursive=True,
    ):
        if file.endswith("priv"):
            encrypted_aes_path = f"{file}"
        elif file.endswith("password"):
            encrypted_passwd_path = f"{file}"

    rsa_key = rsa_crypto.import_create_RSAKey(priv_key_bytes)

    with open(encrypted_aes_path, "rb") as aes, open(
        encrypted_passwd_path, "rb"
    ) as pwd:
        aes_key = rsa_crypto.decrypt_rsa(aes.read(), rsa_key).decode("ascii")
        passwd = base64.b64decode(rsa_crypto.decrypt_rsa(pwd.read(), rsa_key)).decode(
            "utf-8"
        )

    return aes_key, passwd
