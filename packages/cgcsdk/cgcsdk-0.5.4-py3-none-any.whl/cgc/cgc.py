import click
from cgc.commands.volume.volume_cmd import volume_group
from cgc.commands.compute.compute_cmd import compute_group
from cgc.commands.billing.billing_cmd import billing_group
from cgc.commands.auth.auth_cmd import auth_login, auth_register
from cgc.commands.cgc_cmd import cgc_rm, cgc_status
from cgc.utils.version_control import check_version, get_version
from cgc.utils.click_group import CustomGroup


@click.group(cls=CustomGroup)
@click.version_option(get_version())
def cli():
    """CGC application developed by Comtegra S.A."""
    check_version()


cli.add_command(volume_group)
cli.add_command(compute_group)
cli.add_command(billing_group)
cli.add_command(auth_register)
cli.add_command(auth_login)
cli.add_command(cgc_rm)
cli.add_command(cgc_status)


if __name__ == "__main__" or __name__ == "cgc.cgc":
    cli()
else:
    raise Exception("This program is not intended for importing!")
