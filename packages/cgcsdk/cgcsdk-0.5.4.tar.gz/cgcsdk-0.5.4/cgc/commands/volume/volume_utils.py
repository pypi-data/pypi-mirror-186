def get_formatted_volume_list_and_total_size(list_of_volumes: list):
    """Method format data in list of voulmes to be displayed in table and calculate total size of volumes

    :param list_of_volumes: list of volumes to be formatted
    :type list_of_volumes: list
    :return: list of volumes to be displayed in table and total size of volumes
    :rtype: list, int
    """
    list_to_print = []
    total_size = 0
    for volume in list_of_volumes:
        name = volume["name"]
        used = volume["used"]
        size = volume["size"]
        access_types = ", ".join(volume["access_types"])
        mounts = volume["mounted_to"]
        mounts[:] = [s.rsplit("-", 2)[0] for s in mounts]
        all_mounted_to = ", ".join(mounts)
        total_size += int("".join(filter(str.isdigit, size)))
        row_list = [name, used, size, access_types, all_mounted_to]
        list_to_print.append(row_list)
    return list_to_print, total_size
