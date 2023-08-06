import json
import sys
import click
import requests
from tabulate import tabulate

from cgc.utils.prepare_headers import get_api_url_and_prepare_headers
from cgc.telemetry.basic import increment_metric, setup_gauge
from cgc.commands.volume.data_model import (
    volume_create_payload_validator,
    volume_delete_payload_validator,
    volume_mount_payload_validator,
    volume_umount_payload_validator,
)
from cgc.commands.volume.volume_utils import get_formatted_volume_list_and_total_size
from cgc.commands.volume.volume_responses import (
    volume_mount_response,
    volume_umount_response,
    volume_create_response,
    volume_delete_response,
)
from cgc.utils.message_utils import prepare_error_message
from cgc.utils.config_utils import get_namespace
from cgc.utils.response_utils import response_precheck
from cgc.utils.click_group import CustomGroup, CustomCommand


@click.group("volume", cls=CustomGroup)
@click.option("--debug", "debug", is_flag=True, default=False, hidden=True)
@click.pass_context
def volume_group(ctx, debug):
    """
    Management of volumes.
    """
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug


@volume_group.command("list", cls=CustomCommand)
@click.pass_context
def volume_list(ctx):
    """
    List all volumes for user namespace.
    """
    metric_ok = f"{get_namespace()}.volume.list.ok"
    metric_error = f"{get_namespace()}.volume.list.error"

    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/storage/volume/list"
    try:
        response = requests.get(
            url=url,
            headers=headers,
            timeout=10,
        )

        response_precheck(response, metric_error)

        if response.status_code != 200:
            increment_metric(metric_error)
            message = "Error occuerd while listing volumes. Try again or contact us at support@comtegra.pl"
            click.echo(prepare_error_message(message))
            return

        data = response.json()
        list_of_volumes = data["details"]["volume_list"]

        if not list_of_volumes:
            click.echo("No volumes to list.")
            return

        volume_list_to_print, total_size = get_formatted_volume_list_and_total_size(
            list_of_volumes
        )
        list_headers = ["name", "used", "size", "type", "mounted to"]

        if ctx.obj["DEBUG"]:
            click.echo(volume_list_to_print)
        else:
            click.echo(tabulate(volume_list_to_print, headers=list_headers))

        increment_metric(metric_ok)
        setup_gauge(f"{get_namespace()}.volume.count", len(list_of_volumes))
        setup_gauge(f"{get_namespace()}.volume.totalSizeAccumulated", total_size)

    except requests.exceptions.ReadTimeout:
        message = "Connection timed out. Try again or contact us at support@comtegra.pl"
        increment_metric(metric_error)
        click.echo(prepare_error_message(message))


@volume_group.command("create", cls=CustomCommand)
@click.argument("name")
@click.option("-s", "--size", "size", type=click.IntRange(1, 1000), required=True)
@click.option(
    "-t",
    "--type",
    "disk_type",
    type=click.Choice(["ssd", "nvme", "hdd"]),
    default="ssd",
)
@click.option(
    "-a", "--access", "access", type=click.Choice(["rwx", "rwo"]), default="rwx"
)
@click.option(
    "-g",
    "--host_group",
    "host_group",
    type=click.Choice(["compute", "gpu"]),
    default="compute",
)
def volume_create(name: str, size: int, disk_type: str, access: str, host_group: str):
    """Create volume in user namespace.
    \f
    :param name: name of volume
    :type name: str
    :param size: size of volume in GB
    :type size: int
    :param type: type of volume - SSD or NVMe
    :type type: str
    :param access: access type of volume - RWO or RWX
    :type access: str
    :param host_group: group of hosts - compute or gpu
    :type host_group: str
    """
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/storage/volume/create"
    payload = volume_create_payload_validator(
        name=name, access=access, size=size, disk_type=disk_type, host_group=host_group
    )
    try:
        res = requests.post(
            url,
            data=json.dumps(payload),
            headers=headers,
            timeout=10,
        )
        click.echo(volume_create_response(res))

    except requests.exceptions.ReadTimeout:
        message = "Connection timed out. Try again or contact us at support@comtegra.pl"
        increment_metric(f"{get_namespace()}.volume.create.error")
        click.echo(prepare_error_message(message))


@volume_group.command("delete", cls=CustomCommand)
@click.argument("name")
@click.option("-f", "--force", "force_delete", is_flag=True, default=False)
def volume_delete(name: str, force_delete: bool):
    """Delete specific volume from user namespace.
    \f
    :param name: name of the volume to delete
    :type name: str
    :param force_delete: delete volume even if it is still mounted
    :type force_delete: bool
    """
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/storage/volume/delete"
    payload = volume_delete_payload_validator(
        name=name,
        force_delete=force_delete,
    )
    try:
        res = requests.delete(
            url,
            data=json.dumps(payload),
            headers=headers,
            timeout=10,
        )

        click.echo(volume_delete_response(res))

    except requests.exceptions.ReadTimeout:
        message = "Connection timed out. Try again or contact us at support@comtegra.pl"
        increment_metric(f"{get_namespace()}.volume.delete.error")
        click.echo(prepare_error_message(message))


@volume_group.command("umount", cls=CustomCommand)
@click.argument("name")
@click.option("-t", "--target", "target_template_name", multiple=True, default=None)
def volume_umount(name: str, target_template_name):
    """Umount volume from compute resources.
    \f
    :param name: name of the volume to umount
    :type name: str
    """
    while True:
        click.echo(
            "Unmouting a volume will reload all compute resources it was mounted to."
        )
        anwser = input("Do you want to continue? (Y/N): ").lower()
        if anwser in ("y", "yes"):
            break
        if anwser in ("n", "no"):
            sys.exit()

    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/storage/volume/umount"
    payload = volume_umount_payload_validator(
        name=name, target_template_name=target_template_name
    )

    try:
        res = requests.post(
            url,
            data=json.dumps(payload),
            headers=headers,
            timeout=10,
        )
        click.echo(volume_umount_response(res, target_template_name))

    except requests.exceptions.ReadTimeout:
        message = "Connection timed out. Try again or contact us at support@comtegra.pl"
        increment_metric(f"{get_namespace()}.volume.umount.error")
        click.echo(prepare_error_message(message))


@volume_group.command("mount", cls=CustomCommand)
@click.argument("name")
@click.option("-t", "--target", "target", type=str, required=True)
@click.option("-p", "--mount_path", "mount_path", type=str, default=None)
def volume_mount(
    name: str,
    target: str,
    mount_path: str,
):
    """Mount volume to specific template.
    \f
    :param name: name of the volume to mount
    :type name: str
    :param target_template_type: type of template to mount volume to
    :type target_template_type: str
    :param target: name of the template to mount volume to
    :type target: str
    :param mount_path: path to mount volume to
    :type mount_path: str
    """
    while True:
        click.echo(
            "Mounting a volume will reload the compute resources it will be mounted to."
        )
        anwser = input("Do you want to continue? (Y/N): ").lower()
        if anwser in ("y", "yes"):
            break
        if anwser in ("n", "no"):
            sys.exit()

    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/storage/volume/mount"
    payload = volume_mount_payload_validator(
        name=name,
        target=target,
        mount_path=mount_path,
    )
    try:
        res = requests.post(
            url,
            data=json.dumps(payload),
            headers=headers,
            timeout=10,
        )

        click.echo(volume_mount_response(res))

    except requests.exceptions.ReadTimeout:
        message = "Connection timed out. Try again or contact us at support@comtegra.pl"
        increment_metric(f"{get_namespace()}.volume.mount.error")
        click.echo(prepare_error_message(message))
