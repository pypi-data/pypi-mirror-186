def volume_create_payload_validator(name, access, size, disk_type, host_group):
    """
    Create payload for volume creation.
    """
    payload = {
        "name": name,
        "access_type": access,
        "size": size,
        "disks_type": disk_type,
        "host_group": host_group,
        "auto_mount": "false",
    }
    return payload


def volume_delete_payload_validator(name, force_delete):
    """
    Create payload for volume deletion.
    """
    payload = {
        "name": name,
        "force_delete": force_delete,
    }

    return payload


def volume_mount_payload_validator(name, target, mount_path):
    """
    Create payload for volume mount.
    """
    payload = {
        "name": name,
        "target_template_name": target,
        "start_mount_path": mount_path,
    }

    return payload


def volume_umount_payload_validator(name, target_template_name):
    """
    Create payload for volume umount.
    """
    # convert tuple to list - backend
    target_template_name = list(target_template_name)
    # Send None if compute resource not specified
    if len(target_template_name) == 0:
        target_template_name = None
    payload = {"name": name, "target_template_name": target_template_name}

    return payload
