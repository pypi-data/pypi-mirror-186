import json
import requests
import click
from tabulate import tabulate

from cgc.commands.compute.compute_responses import (
    compute_create_filebrowser_response,
    compute_create_response,
    compute_delete_response,
    compute_restart_response,
)
from cgc.commands.compute.data_model import (
    compute_create_payload_validator,
    compute_delete_payload_validator,
)
from cgc.commands.compute.compute_utills import list_get_app_list_to_print
from cgc.utils.prepare_headers import get_api_url_and_prepare_headers
from cgc.telemetry.basic import increment_metric, setup_gauge
from cgc.utils.message_utils import prepare_error_message, prepare_success_message
from cgc.utils.config_utils import get_namespace
from cgc.utils.response_utils import response_precheck
from cgc.utils.click_group import CustomGroup, CustomCommand
from cgc.utils.consts.message_consts import TIMEOUT_ERROR, UNEXPECTED_ERROR

AVAILABLE_TEMPLATES = [
    "datascience-jupyter",
    "tensorflow-jupyter",
    "nvidia-tensorflow",
    "nvidia-rapids",
    "nvidia-pytorch",
]


@click.group(name="compute", cls=CustomGroup)
@click.option("--debug", "debug", is_flag=True, default=False, hidden=True)
@click.pass_context
def compute_group(ctx, debug):
    """
    Management of compute resources.
    """
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug


@click.group(name="template", cls=CustomGroup)
def template_group():
    """
    Management of templates.
    """


@template_group.command("list", cls=CustomCommand)
def template_list():
    """Lists all available templates"""
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/compute/list_available_templates"
    metric_ok = f"{get_namespace()}.compute.template.list.ok"
    metric_error = f"{get_namespace()}.compute.template.list.error"
    try:
        res = requests.get(
            url=url,
            headers=headers,
            timeout=10,
        )
        response_precheck(res, metric_error)
        if res.status_code != 200:
            increment_metric(metric_error)
            message = "Error occuerd while listing templates. Try again or contact us at support@comtegra.pl"
            click.echo(prepare_error_message(message))
            return

        data = res.json()
        available_templates_list = data["details"]["available_templates_list"]
        message = f"Available templates: {', '.join(available_templates_list)}"
        click.echo(prepare_success_message(message))
        increment_metric(metric_ok)
    except KeyError:
        increment_metric(metric_error)
        click.echo(prepare_error_message(UNEXPECTED_ERROR))
    except requests.exceptions.ReadTimeout:
        increment_metric(metric_error)
        click.echo(prepare_error_message(TIMEOUT_ERROR))


@template_group.command("get_start_path", cls=CustomCommand)
@click.argument("template", type=click.Choice(AVAILABLE_TEMPLATES))
def template_get_start_path(template: str):
    """Displays start path of specified template"""
    api_url, headers = get_api_url_and_prepare_headers()

    url = f"{api_url}/v1/api/compute/get_template_start_path?template_name={template}"
    metric_ok = f"{get_namespace()}.compute.template.get_start_path.ok"
    metric_error = f"{get_namespace()}.compute.template.get_start_path.error"
    try:
        res = requests.get(
            url=url,
            headers=headers,
            timeout=10,
        )
        response_precheck(res, metric_error)
        if res.status_code != 200:
            increment_metric(metric_error)
            message = "Error occuerd while displaying template start path. Try again or contact us at support@comtegra.pl"
            click.echo(prepare_error_message(message))
            return

        data = res.json()
        start_path = data["details"]["start_path"]
        message = f"Start path for {template}: {start_path}"
        click.echo(prepare_success_message(message))
        increment_metric(metric_ok)

    except requests.exceptions.ReadTimeout:
        increment_metric(metric_error)
        click.echo(prepare_error_message(TIMEOUT_ERROR))


@click.group(name="filebrowser", cls=CustomGroup)
def filebrowser_group():
    """
    Management of filebrowser.
    """


@filebrowser_group.command("create", cls=CustomCommand)
def compute_filebrowser_create():
    """Create a filebrowser service"""
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/compute/filebrowser_create"
    payload = {"puid": 0, "pgid": 0}
    try:
        res = requests.post(
            url=url,
            headers=headers,
            data=json.dumps(payload),
            timeout=10,
        )
        click.echo(compute_create_filebrowser_response(res))
    except requests.exceptions.ReadTimeout:
        increment_metric(f"{get_namespace()}.compute.create_filebrowser.error")
        click.echo(prepare_error_message(TIMEOUT_ERROR))


@filebrowser_group.command("delete", cls=CustomCommand)
def compute_filebrowser_delete():
    """Delete a filebrowser service"""
    compute_delete("filebrowser")


@compute_group.command("create", cls=CustomCommand)
@click.argument("entity", type=click.Choice(AVAILABLE_TEMPLATES))
@click.option("-n", "--name", "name", type=click.STRING, required=True)
@click.option("-g", "--gpu", "gpu", type=click.INT, default=0)
@click.option(
    "-gt",
    "--gpu-type",
    "gpu_type",
    type=click.Choice(["A100", "V100", "A5000"], case_sensitive=False),
    default="V100",
)
@click.option("-c", "--cpu", "cpu", type=click.INT, default=1)
@click.option("-m", "--memory", "memory", type=click.INT, default=2)
@click.option("-v", "--volume", "volumes", multiple=True)
def compute_create(
    entity: str,
    gpu: int,
    gpu_type: str,
    cpu: int,
    memory: int,
    volumes: list[str],
    name: str,
):
    """
    Create an app in user namespace.
    \f
    :param entity: name of entity to create
    :type entity: str
    :param gpu: number of gpus to be used by app
    :type gpu: int
    :param cpu: number of cores to be used by app
    :type cpu: int
    :param memory: GB of memory to be used by app
    :type memory: int
    :param volumes: list of volumes to mount
    :type volumes: list[str]
    :param name: name of app
    :type name: str
    """
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/compute/create"

    payload = compute_create_payload_validator(
        name=name,
        entity=entity,
        cpu=cpu,
        memory=memory,
        gpu=gpu,
        volumes=volumes,
        gpu_type=gpu_type,
    )

    try:
        res = requests.post(
            url,
            data=json.dumps(payload),
            headers=headers,
            timeout=10,
        )
        click.echo(compute_create_response(res))
    except requests.exceptions.ReadTimeout:
        increment_metric(f"{get_namespace()}.compute.create.error")
        click.echo(prepare_error_message(TIMEOUT_ERROR))


@compute_group.command("delete", cls=CustomCommand)
@click.argument("name", type=click.STRING)
def compute_delete_cmd(name: str):
    """
    Delete an app from user namespace.
    \f
    :param name: name of app to delete
    :type name: str
    """
    compute_delete(name)


def compute_delete(name: str):
    """
    Delete an app using backend endpoint.
    \f
    :param name: name of app to delete
    :type name: str
    """
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/compute/delete"
    payload = compute_delete_payload_validator(name=name)
    try:
        res = requests.delete(
            url,
            data=json.dumps(payload),
            headers=headers,
            timeout=10,
        )
        click.echo(compute_delete_response(res))
    except requests.exceptions.ReadTimeout:
        increment_metric(f"{get_namespace()}.compute.delete.error")
        click.echo(prepare_error_message(TIMEOUT_ERROR))


@compute_group.command("list", cls=CustomCommand)
@click.option(
    "-d", "--detailed", "detailed", type=click.BOOL, is_flag=True, default=False
)
@click.pass_context
def compute_list(ctx, detailed: bool):
    """
    List all apps for user namespace.
    """
    metric_ok = f"{get_namespace()}.compute.list.ok"
    metric_error = f"{get_namespace()}.compute.list.error"
    api_url, headers = get_api_url_and_prepare_headers()

    url = f"{api_url}/v1/api/compute/list"
    try:
        response = requests.get(
            url=url,
            headers=headers,
            timeout=10,
        )
        response_precheck(response, metric_error)

        if response.status_code != 200:
            increment_metric(metric_error)
            message = "Error occuerd while listing apps. Try again or contact us at support@comtegra.pl"
            click.echo(prepare_error_message(message))
            return

        data = response.json()
        app_list = data["details"]["pods_list"]

        setup_gauge(f"{get_namespace()}.compute.count", len(app_list))
        increment_metric(metric_ok)

        if not app_list:
            click.echo("No apps to list.")
            return

        app_list_to_print = list_get_app_list_to_print(app_list, detailed)

        list_headers = [
            "name",
            "type",
            "status",
            "volumes mounted",
            "CPU cores",
            "RAM",
            "GPU type",
            "GPU count",
            "URL",
            "App token",
        ]
        if not detailed:
            list_headers.remove("App token")

        if ctx.obj["DEBUG"]:
            print(app_list_to_print)
        else:
            click.echo(tabulate(app_list_to_print, headers=list_headers))
    except KeyError:
        increment_metric(metric_error)
        click.echo(prepare_error_message(UNEXPECTED_ERROR))
    except requests.exceptions.ReadTimeout:
        increment_metric(metric_error)
        click.echo(prepare_error_message(TIMEOUT_ERROR))


@compute_group.command("restart", cls=CustomCommand)
@click.argument("name", type=click.STRING)
def compute_filebrowser_restart(name: str):
    """Restarts the specified app"""
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/compute/restart"
    payload = {"name": name}
    try:
        res = requests.post(
            url=url,
            headers=headers,
            data=json.dumps(payload),
            timeout=10,
        )
        click.echo(compute_restart_response(res))
    except requests.exceptions.ReadTimeout:
        increment_metric(f"{get_namespace()}.compute.restart.error")
        click.echo(prepare_error_message(TIMEOUT_ERROR))


compute_group.add_command(filebrowser_group)
compute_group.add_command(template_group)
