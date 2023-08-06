import os
import subprocess
import sys
import requests
import click
from cgc.utils.prepare_headers import get_api_url_and_prepare_headers_version_control
from cgc.utils.message_utils import (
    prepare_error_message,
    prepare_warning_message,
)
from cgc.utils.consts.env_consts import MAJOR_VERSION, MINOR_VERSION, RELEASE
from cgc.utils.consts.message_consts import (
    TIMEOUT_ERROR,
    UNEXPECTED_ERROR,
    OUTDATED_MAJOR,
    OUTDATED_MINOR,
)

def get_server_version():
    """Queries the server about its current version

    :return: server version data
    :rtype: dict
    """
    try:
        url, headers = get_api_url_and_prepare_headers_version_control() 
        res = requests.get(
            url,
            headers=headers,
            timeout=10,
        )
    except requests.exceptions.ReadTimeout:
        click.echo(prepare_error_message(TIMEOUT_ERROR))
        sys.exit()

    if res.status_code != 200:
        print(res.text)
        click.echo(prepare_error_message(UNEXPECTED_ERROR))
        sys.exit()
    return res.json()

def check_version():
    """Checks if Client version is up to date with Server version."""
    data = get_server_version()
    if data["server_version"]["major"] > MAJOR_VERSION:
        click.echo(prepare_error_message(OUTDATED_MAJOR))
        while True:
            anwser = input("Update now? (Y/N): ").lower()
            if anwser in ("y", "yes"):
                update_file_path = os.path.join(os.path.dirname(__file__), "update.py")
                try:
                    subprocess.Popen([sys.executable, update_file_path])
                    sys.exit()
                except subprocess.SubprocessError:
                    click.echo(
                        prepare_error_message(
                            "Could not initiate update, try again or install update manually with: pip install --upgrade cgcsdk"
                        )
                    )
            if anwser in ("n", "no"):
                sys.exit()
    elif data["server_version"]["minor"] > MINOR_VERSION:
        click.echo(prepare_warning_message(OUTDATED_MINOR))


def get_version():
    """Returns version of cgcsdk."""
    return f"{RELEASE}.{MAJOR_VERSION}.{MINOR_VERSION}"
