import click


class CustomGroup(click.Group):
    """Class to customise help message for click groups"""

    def format_usage(self, ctx, formatter):
        pieces = self.collect_usage_pieces(ctx)
        cmd_path = ctx.command_path.removeprefix("python -m ")
        formatter.write_usage(cmd_path, " ".join(pieces))


class CustomCommand(click.Command):
    """Class to customise help message for click commands"""

    def format_usage(self, ctx, formatter):
        pieces = self.collect_usage_pieces(ctx)
        cmd_path = ctx.command_path.removeprefix("python -m ")
        formatter.write_usage(cmd_path, " ".join(pieces))
