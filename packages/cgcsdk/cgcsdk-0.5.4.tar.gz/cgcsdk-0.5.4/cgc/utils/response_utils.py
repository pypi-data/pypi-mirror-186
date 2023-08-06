import sys
import click
import requests

from cgc.utils.message_utils import prepare_error_message
from cgc.utils.consts.message_consts import (
    UNAUTHORIZED_ERROR,
    INTERNAL_SERVER_ERROR,
    DISABLED_ERROR,
)
from cgc.telemetry.basic import increment_metric


def response_precheck(response: requests.Response, telemetry: str):
    """Checks if server is available and user is authorized

    :param response: dict object from API response.
    :type response: requests.Response
    """
    if response.status_code == 500:
        message = INTERNAL_SERVER_ERROR
        click.echo(prepare_error_message(message))
        increment_metric(telemetry)
        sys.exit()
    if response.status_code == 401:
        message = UNAUTHORIZED_ERROR
        click.echo(prepare_error_message(message))
        increment_metric(telemetry)
        sys.exit()
    if response.status_code == 403:
        message = DISABLED_ERROR
        click.echo(prepare_error_message(message))
        increment_metric(telemetry)
        sys.exit()
