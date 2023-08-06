import json
import requests


from cgc.telemetry.basic import increment_metric
from cgc.telemetry.basic import change_gauge
from cgc.utils.message_utils import prepare_error_message, prepare_success_message, prepare_warning_message
from cgc.utils.config_utils import get_namespace
from cgc.utils.response_utils import response_precheck
from cgc.utils.consts.message_consts import UNEXPECTED_ERROR


def compute_create_filebrowser_response(response: requests.Response) -> str:
    """Create response string for compute create_filebrowser command

    :param response: dict object from API response.
    :type response: requests.Response
    :return: Response string.
    :rtype: str
    """
    try:
        metric_ok = f"{get_namespace()}.compute.create_filebrowser.ok"
        metric_error = f"{get_namespace()}.compute.create_filebrowser.error"
        response_precheck(response, metric_error)

        if response.status_code == 200:
            data = response.json()
            namespace = data["details"]["namespace"]
            app_url = data["details"]["created_template"]["pod_url"]
            app_token = data["details"]["created_template"]["app_token"]
            message = f"Filebrowser created successfuly!\nAccessible at: {app_url}\nUsername: {namespace}\nPassword: {app_token}"
            increment_metric(metric_ok)
            return prepare_success_message(message)
        if response.status_code == 409:
            increment_metric(metric_error)
            message = "Filebrowser already exists in namespace."
            return prepare_error_message(message)
        if response.status_code == 413:
            increment_metric(metric_error)
            message = UNEXPECTED_ERROR
            return prepare_error_message(message)
        return prepare_error_message(response.text)
    except (KeyError, json.JSONDecodeError):
        increment_metric(metric_error)
        return prepare_error_message(UNEXPECTED_ERROR)


def compute_create_error_parser(error: dict) -> str:
    """Function that pases error from API for compute create command.

    :param error: Dict containing error message and further info from API.
    :type error: dict
    :return: String or dict depending on error.
    :rtype: str or dict
    """
    # TODO add errors after backend is finished
    try:
        if error["reason"] == "COMPUTE_TEMPLATE_NAME_ALREADY_EXISTS":
            message = f"App creation failed. App with name {error['details']['name']} already exists in namespace."
            return prepare_error_message(message)
        if error["reason"] == "PVC_NOT_FOUND":
            message = f"App creation failed. Volume {error['details']['pvc_name']} not found in namespace."
            return prepare_error_message(message)
        if error["reason"] == "COMPUTE_CREATE_FAILURE":
            message = "App creation failed. Entity template not found."
            return prepare_error_message(message)
        if error["reason"] == "REQUEST_RESOURCE_LIMIT_EXCEDED":
            message = "App creation failed. Request excedes resource limits."
            return prepare_error_message(message)
        if error["reason"] == "RESOURCES_NOT_AVAILABLE_IN_CLUSTER":
            message = "App creation failed. Resources are not available at the moment."
            return prepare_error_message(message)
        if error["reason"] == "Invalid":
            
            message = f"App creation failed. {error['details']['causes'][0]['message']}"
            return prepare_error_message(message)
        message = prepare_error_message(error)
        return message
    except (KeyError, TypeError):
        return prepare_error_message(UNEXPECTED_ERROR)


def compute_create_response(response: requests.Response) -> str:
    """Create response string for compute create command.

    :param response: dict object from API response.
    :type response: requests.Response
    :return: Response string.
    :rtype: str
    """
    try:
        metric_ok = f"{get_namespace()}.compute.create.ok"
        metric_error = f"{get_namespace()}.compute.create.error"
        response_precheck(response, metric_error)

        data = json.loads(response.text)
        warning = ""
        if response.status_code == 200:
            status = data["details"].get("status")
            if status == "PVC NOT FOUND":
                warning = "Volume name not found in namespace\n"
            increment_metric(metric_ok)
            change_gauge(f"{get_namespace()}.compute.count", 1)

            name = data["details"]["created_service"]["name"]
            entity = data["details"]["created_service"]["labels"]["entity"]
            volume_list = data["details"].get("mounted_pvc_list")
            volumes = ",".join(volume_list) if volume_list else None
            try:
                app_token = data["details"]["created_template"]["app_token"]
            except KeyError:
                app_token = None
            app_url = data["details"]["created_template"]["pod_url"]
            # TODO bedzie wiecej entity jupyterowych
            entity_list = [
                "datascience-jupyter",
                "tensorflow-jupyter",
                "nvidia-tensorflow",
                "nvidia-rapids",
                "nvidia-pytorch",
                "nvidia-triton",
            ]
           
            if entity in entity_list:
                message = f"{entity} app {name} has been created! Mounted volumes: {volumes}\nAccessible at: {app_url}\nApp token: {app_token}"
            else:
                message = (
                    f"{entity} App {name} has been created! Mounted volumes: {volumes}"
                )
            return f"{prepare_warning_message(warning)}{prepare_success_message(message)}" 


        increment_metric(metric_error)
        error = compute_create_error_parser(data)
        return error
    except (KeyError, json.JSONDecodeError):
        increment_metric(metric_error)
        return prepare_error_message(UNEXPECTED_ERROR)


def compute_delete_error_parser(error: dict) -> str:
    """Function that pases error from API for compute delete command.

    :param error: Dict containing error message and further info from API.
    :type error: dict
    :return: String or dict depending on error.
    :rtype: str or dict
    """
    try:
        if error["reason"] == "NOT_DELETED_ANYTHING_IN_COMPUTE_DELETE":
            message = f"App {error['details']['name']} not found in namespace."
            return prepare_error_message(message)
        message = prepare_error_message(error)
        return message
    except KeyError:
        return prepare_error_message(UNEXPECTED_ERROR)


def compute_delete_response(response: requests.Response) -> str:
    """Create response string for compute delete command.

    :param response: dict object from API response.
    :type response: requests.Response
    :return: Response string.
    :rtype: str
    """
    try:
        metric_ok = f"{get_namespace()}.compute.delete.ok"
        metric_error = f"{get_namespace()}.compute.delete.error"
        response_precheck(response, metric_error)
        data = json.loads(response.text)

        if response.status_code == 200:
            name = data["details"]["deleted_service"]["name"]
            increment_metric(metric_ok)
            change_gauge(f"{get_namespace()}.compute.count", -1)
            message = f"App {name} and its service successfully deleted."
            return prepare_success_message(message)
        else:
            increment_metric(metric_error)
            error = compute_delete_error_parser(data)
            return error
    except (KeyError, json.JSONDecodeError):
        increment_metric(metric_error)
        return prepare_error_message(UNEXPECTED_ERROR)


def compute_restart_error_parser(error: dict) -> str:
    """Function that pases error from API for compute restart command.

    :param error: Dict containing error message and further info from API.
    :type error: dict
    :return: String or dict depending on error.
    :rtype: str or dict
    """
    try:
        if error["reason"] == "COMPUTE_RESTART_FAILURE" and error["code"] == 404:
            message = f"App {error['details']['name']} not found in namespace."
            return prepare_error_message(message)
        message = prepare_error_message(error)
        return message
    except KeyError:
        return prepare_error_message(UNEXPECTED_ERROR)


def compute_restart_response(response: requests.Response) -> str:
    """Create response string for compute restart command.

    :param response: dict object from API response.
    :type response: requests.Response
    :return: Response string.
    :rtype: str
    """
    try:
        metric_ok = f"{get_namespace()}.compute.restart.ok"
        metric_error = f"{get_namespace()}.compute.restart.error"
        response_precheck(response, metric_error)
        data = json.loads(response.text)

        if response.status_code == 200:
            name = data["details"]["template_name"]
            increment_metric(metric_ok)
            message = f"App {name} has been successfully restarted."
            return prepare_success_message(message)
        else:
            increment_metric(metric_error)
            error = compute_restart_error_parser(data)
            return error
    except (KeyError, json.JSONDecodeError):
        increment_metric(metric_error)
        return prepare_error_message(UNEXPECTED_ERROR)
