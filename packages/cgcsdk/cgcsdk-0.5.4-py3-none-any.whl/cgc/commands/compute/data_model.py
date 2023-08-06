def compute_create_payload_validator(
    name, entity, cpu, memory, volumes: list, gpu: int, gpu_type: str
):
    """
    Create payload for app creation.
    """

    payload = {
        "name": name,
        "entity": entity,
        "cpu": cpu,
        "gpu": gpu,
        "memory": memory,
        "gpu_type": gpu_type,
    }
    if len(volumes) != 0:
        payload["pv_volume"] = volumes
    return payload


def compute_delete_payload_validator(name):
    """
    Create payload for app creation.
    """
    payload = {
        "name": name,
    }
    return payload
