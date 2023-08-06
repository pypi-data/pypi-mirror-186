import click


def list_get_main_container(container_list: list, entity: str) -> dict:
    """Determines the main container of an app.

    :param container_list: list of containers
    :type container_list: list
    :param entity: type of app
    :type entity: str
    :return: main container
    :rtype: dict
    """
    for container in container_list:
        try:
            if container["name"] == entity:
                return container
        except KeyError:
            click.echo("something went wrong")
    return None


def list_get_mounted_volumes(volume_list: list) -> str:
    """Formats and returns list of PVC volumes mounted to an app.

    :param volume_list: list of all volumes mounted to an app
    :type volume_list: list
    :return: list of PVC volumes
    :rtype: str
    """
    volume_name_list = []
    for volume in volume_list:
        volume_type = volume.get("type")
        if volume_type == "PVC":
            volume_name = volume.get("name")
            volume_name_list.append(volume_name)
    volumes_mounted = (
        ", ".join(volume_name_list) if len(volume_name_list) != 0 else None
    )
    return volumes_mounted


def list_get_app_list_to_print(app_list: list, detailed: bool) -> list:
    """Formats and returns list of apps to print.

    :param app_list: list of apps
    :type app_list: list
    :return: formatted list of apps
    :rtype: list
    """
    app_list_to_print = []
    for app in app_list:
        try:
            labels = app["labels"]
            app_name = labels["app-name"]
            app_type = labels["entity"]
            status = app["status"]

            app_url = labels.get("pod_url")
            app_token = labels.get("app-token")

            main_container = list_get_main_container(app["containers"], app_type)
            volumes_mounted = list_get_mounted_volumes(main_container["mounts"])

            if app_type != "filebrowser":
                gpu_type = labels.get("gpu-label")
                gpu_count = (
                    labels.get("gpu-count")
                    if labels.get("gpu-count") is not None
                    else 0
                )

                limits = main_container["resources"].get("limits")
                cpu = limits.get("cpu") if limits is not None else 0
                ram = limits.get("memory") if limits is not None else "0Gi"
            else:
                gpu_type = None
                gpu_count = None
                cpu = None
                ram = None

            row_list = [
                app_name,
                app_type,
                status,
                volumes_mounted,
                cpu,
                ram,
                gpu_type,
                gpu_count,
                app_url,
                app_token,
            ]
            if not detailed:
                row_list.pop(-1)

            app_list_to_print.append(row_list)
        except KeyError:
            pass
    return app_list_to_print
