import click
import requests
from cgc.commands.cgc_cmd_utils import print_user_resources

from cgc.commands.compute.compute_cmd import compute_delete
from cgc.telemetry.basic import increment_metric
from cgc.utils.click_group import CustomCommand
from cgc.utils.config_utils import get_namespace
from cgc.utils.consts.message_consts import TIMEOUT_ERROR
from cgc.utils.message_utils import prepare_error_message
from cgc.utils.prepare_headers import get_api_url_and_prepare_headers
from cgc.utils.response_utils import response_precheck


@click.command("rm", cls=CustomCommand)
@click.argument("name", type=click.STRING)
def cgc_rm(name: str):
    """
    Delete an app in user namespace
    """
    compute_delete(name)


@click.command("status", cls=CustomCommand)
def cgc_status():
    """Lists available and used resources"""
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/compute/status"
    metric_ok = f"{get_namespace()}.compute.status.ok"
    metric_error = f"{get_namespace()}.compute.status.error"
    try:
        res = requests.get(
            url=url,
            headers=headers,
            timeout=10,
        )

        response_precheck(res, metric_error)
        if res.status_code != 200:
            increment_metric(metric_error)
            message = "Error occuerd while fetching available resources. Try again or contact us at support@comtegra.pl"
            if res.status_code == 404:
                message = f"No resource quota defined for namespace {get_namespace()}."
            click.echo(prepare_error_message(message))
            return

        data = res.json()
        print_user_resources(data, metric_error)

        increment_metric(metric_ok)
    except requests.exceptions.ReadTimeout:
        increment_metric(metric_error)
        click.echo(prepare_error_message(TIMEOUT_ERROR))
