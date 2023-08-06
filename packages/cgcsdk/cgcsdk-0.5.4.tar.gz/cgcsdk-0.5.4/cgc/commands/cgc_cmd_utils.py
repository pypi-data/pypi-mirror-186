import click
from tabulate import tabulate
from cgc.telemetry.basic import increment_metric
from cgc.utils.consts.message_consts import UNEXPECTED_ERROR
from cgc.utils.message_utils import prepare_error_message


def print_user_resources(data: dict, metric_error: str):
    """Generates and prints resource limits and available resources in a pretty format

    :param data: data to extrct resources from
    :type data: dict
    :param metric_error: error metric for graphana
    :type metric_error: str
    """
    try:
        resources_available = data["details"]["available_resources"]
        resources_limits = data["details"]["limits_resources"]
        list_headers = ["Resource", "Type", "Available", "Limit"]
        resource_names = [
            "CPU",
            "RAM",
            "GPU",
            "-",
            "-",
            "-",
            "Volume",
            "Storage",
            "-",
            "-",
            "-",
        ]
        types = [
            "",
            "",
            "",
            "A100",
            "A5000",
            "V100",
            "Count",
            "",
            "cpu-nvme",
            "cpu-ssd",
            "gpu-nvme",
        ]
        resource_keys = [
            "limits.cpu",
            "limits.memory",
            "requests.nvidia.com/gpu",
            "comtegra.cloud/a100",
            "comtegra.cloud/a5000",
            "comtegra.cloud/v100",
            "persistentvolumeclaims",
            "requests.storage",
            "compute-nvme-rwx.storageclass.storage.k8s.io/requests.storage",
            "compute-ssd-rwx.storageclass.storage.k8s.io/requests.storage",
            "gpu-nvme-rwx.storageclass.storage.k8s.io/requests.storage",
        ]

        resources_available_list = []
        resources_limits_list = []
        for key in resource_keys:
            available = resources_available[key]
            limit = resources_limits[key]
            if "storage" in key or "memory" in key:
                available = f"{available} GiB"
                limit = f"{limit} GiB"
            else:
                available = int(available)
                limit = int(limit)
            resources_available_list.append(available)
            resources_limits_list.append(limit)

        test = list(
            zip(resource_names, types, resources_available_list, resources_limits_list)
        )
        click.echo(tabulate(test, headers=list_headers))

    except KeyError:
        increment_metric(metric_error)
        click.echo(prepare_error_message(UNEXPECTED_ERROR))
