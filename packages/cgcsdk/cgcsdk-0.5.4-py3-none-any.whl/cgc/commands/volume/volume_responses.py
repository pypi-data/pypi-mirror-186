import json
import requests

from cgc.telemetry.basic import increment_metric, change_gauge
from cgc.utils.message_utils import prepare_error_message
from cgc.utils.message_utils import prepare_success_message
from cgc.utils.message_utils import prepare_warning_message
from cgc.utils.config_utils import get_namespace
from cgc.utils.response_utils import response_precheck
from cgc.utils.consts.message_consts import UNEXPECTED_ERROR


def volume_create_error_parser(error: dict) -> str:
    """Function that pases error from API for volume create command.
    For now there is two errors implementned to give string output.

    :param error: Dict containing error message and further info from API.
    :type error: dict
    :return: String or dict depending on error.
    :rtype: str or dict
    """

    try:
        if error["reason"] == "AlreadyExists":
            message = f"Volume with name {error['details']['name']} already exists."
            return prepare_error_message(message)
        if error["reason"] == "PVC_CREATE_NO_SC":
            message = f"Volume {error['details']['name']} could not be created. No storage class defined for this access type."
            return prepare_error_message(message)
        if error["reason"] == "PVC_CREATE_MOUNT_FAILURE":
            message = "PVC created successfully but Filebrowser deployment is not existing in namespace."
            return prepare_warning_message(message)
        if error["reason"] == "Invalid":
            message = "Invalid volume name, for more information refer to: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/"
            return prepare_error_message(message)
        message = error["reason"]
        return prepare_error_message(message)
    except KeyError:
        return prepare_error_message(UNEXPECTED_ERROR)


def volume_create_response(response: requests.Response) -> str:
    """Create response string for volume create command.

    :param response: dict object from API response.
    :type response: requests.Response
    :return: Response string.
    :rtype: str
    """

    metric_ok = f"{get_namespace()}.volume.create.ok"
    metric_error = f"{get_namespace()}.volume.create.error"
    response_precheck(response, metric_error)
    try:
        data = json.loads(response.text)

        def shoot_telemetry(size: int):
            """Function that sends telemetry for volume create command.
            Created only because occured error 201. We don't know all the errors yet. 201 creates volume but fires excepion"""
            increment_metric(metric_ok)
            change_gauge(f"{get_namespace()}.volume.count", 1)
            change_gauge(f"{get_namespace()}.volume.totalSizeAccumulated", size)

        if response.status_code == 200:
            name = data["details"]["volume_created"]["name"]
            size = data["details"]["volume_created"]["size"]
            access = data["details"]["volume_created"]["access_type"][0]
            disk_type = data["details"]["volume_created"]["disks_type"]
            shoot_telemetry(int("".join(filter(str.isdigit, size))))
            message = f"Volume {name} of size {size} GB on {disk_type} created. Volume is {access}."
            return prepare_success_message(message)

        if response.status_code == 202:
            error = volume_create_error_parser(data)
            size = data["details"]["volume_created"]["size"]
            shoot_telemetry(int("".join(filter(str.isdigit, size))))
            return error

        increment_metric(metric_error)
        error = volume_create_error_parser(data)
        return error
    except (KeyError, json.JSONDecodeError):
        increment_metric(metric_error)
        return prepare_error_message(UNEXPECTED_ERROR)


def volume_delete_error_parser(error: dict) -> str:
    """Function that pases error from API for volume delete command.
    For now there is one error implementned to give string output.

    :param error: Dict containing error message and further info from API.
    :type error: dict
    :return: String or dict depending on error.
    :rtype: str or dict
    """

    try:
        if error["reason"] == "NotFound":
            message = f"Volume {error['details']['name']} not found."
            return prepare_error_message(message)
        if error["reason"] == "PVC_DELETE_EXCEPTION":
            message = f"Volume {error['details']['pvc_name']} is still mounted. Please unmount it or use the --force flag."
            return prepare_error_message(message)
        message = error["reason"]
        return prepare_error_message(message)
    except KeyError:
        return prepare_error_message(UNEXPECTED_ERROR)


def volume_delete_response(response: requests.Response) -> str:
    """Create response string for volume delete command.

    :param response: dict object from API response.
    :type response: requests.Response
    :return: Response string.
    :rtype: str
    """

    metric_ok = f"{get_namespace()}.volume.delete.ok"
    metric_error = f"{get_namespace()}.volume.delete.error"
    response_precheck(response, metric_error)
    try:
        data = json.loads(response.text)

        if response.status_code == 200:
            name = data["details"]["volume_deleted"]["name"]
            size = int(
                "".join(filter(str.isdigit, data["details"]["volume_deleted"]["size"]))
            )
            increment_metric(metric_ok)
            change_gauge(f"{get_namespace()}.volume.count", -1)
            change_gauge(f"{get_namespace()}.volume.totalSizeAccumulated", -size)

            message = f"Volume {name} deleted."
            return prepare_success_message(message)
        increment_metric(metric_error)
        error = volume_delete_error_parser(data)
        return error
    except (KeyError, json.JSONDecodeError):
        increment_metric(metric_error)
        return prepare_error_message(UNEXPECTED_ERROR)


def volume_mount_error_parser(error: dict) -> str:
    """Function that pases error from API for volume delete command.
    For now there is one error implementned to give string output.

    :param error: Dict containing error message and further info from API.
    :type error: dict
    :return: String or dict depending on error.
    :rtype: str or dict
    """

    try:
        error_code = error["code"]
        reason = error["reason"]
        volume = error["details"]["pvc_name"]
        target = error["details"]["target_template_name"]
        if error_code == 400:
            message = f"Volume {volume} is already mounted to {target}"
            return prepare_error_message(message)
        if error_code == 404 and reason == "PVC_MOUNT_EXCEPTION":
            message = f"Mount unsuccessful, could not find app {target} in namespace"
            return prepare_error_message(message)
        if error_code == 404 and reason == "PVC_NOT_FOUND":
            message = f"Mount unsuccessful, could not find volume {volume} in namespace"
            return prepare_error_message(message)
        if error_code == 501:
            message = "Volume mount for stateful sets is not supported yet"
            return prepare_error_message(message)
        message = error["reason"]
        return prepare_error_message(message)
    except KeyError:
        return prepare_error_message(UNEXPECTED_ERROR)


def volume_mount_response(response: requests.Response) -> str:
    """Create response string for volume delete command.

    :param response: dict object from API response.
    :type response: requests.Response
    :return: Response string.
    :rtype: str
    """

    metric_ok = f"{get_namespace()}.volume.mount.ok"
    metric_error = f"{get_namespace()}.volume.mount.error"
    response_precheck(response, metric_error)

    try:
        data = json.loads(response.text)

        if response.status_code == 200:
            name = data["details"]["pvc_name"]
            target = data["details"]["target_template_name"]
            mount_path = data["details"]["mount_path"]
            increment_metric(metric_ok)
            message = f"Volume {name} succesfully mounted to {target}, mount path: {mount_path}."
            return prepare_success_message(message)
        increment_metric(metric_error)
        error = volume_mount_error_parser(data)
        return error
    except (KeyError, json.JSONDecodeError):
        increment_metric(metric_error)
        return prepare_error_message(UNEXPECTED_ERROR)


def volume_umount_error_parser(error: dict) -> str:
    """Function that pases error from API for volume delete command.
    For now there is one error implementned to give string output.

    :param error: Dict containing error message and further info from API.
    :type error: dict
    :return: String or dict depending on error.
    :rtype: str or dict
    """
    error_code = error["code"]
    reason = error["reason"]
    volume = error["details"]["pvc_name"]
    try:
        if error_code == 404 and reason == "PVC_NOT_FOUND":
            message = f"Volume {volume} have not been found in namespace."
            return prepare_error_message(message)
        if error_code == 404 and reason == "PVC_UNMOUNT":
            message = f"Volume {volume} is not mounted to any compute resources."
            return prepare_error_message(message)
        message = error["reason"]
        return prepare_error_message(message)
    except KeyError:
        return prepare_error_message(UNEXPECTED_ERROR)


def volume_umount_response(
    response: requests.Response, target_template_name: tuple
) -> str:
    """Create response string for volume delete command.

    :param response: dict object from API response.
    :type response: requests.Response
    :return: Response string.
    :rtype: str
    """

    metric_ok = f"{get_namespace()}.volume.umount.ok"
    metric_error = f"{get_namespace()}.volume.umount.error"
    response_precheck(response, metric_error)
    try:
        data = json.loads(response.text)

        if response.status_code == 200:
            name = data["details"]["pvc_name"]
            increment_metric(metric_ok)
            message = f"Volume {name} succesfully unmounted from selected apps."
            return prepare_success_message(message)
        increment_metric(metric_error)
        error = volume_umount_error_parser(data)
        return error

    except (KeyError, json.JSONDecodeError):
        increment_metric(metric_error)
        return prepare_error_message(UNEXPECTED_ERROR)
