import logging

import click

from gantry.cli.application import application
from gantry.cli.bucket import bucket
from gantry.cli.data_connector import data_connector
from gantry.cli.projection import projection
from gantry.cli.secret import secret


@click.group()
@click.option(
    "--loglevel",
    "-l",
    type=click.Choice(["debug", "info", "warning", "error", "critical"], case_sensitive=False),
    default="info",
)
@click.pass_context
def cli(ctx, loglevel):
    ctx.ensure_object(dict)

    formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    pkg_logger = logging.getLogger("gantry")
    pkg_logger.addHandler(handler)
    pkg_logger.setLevel(level=loglevel.upper())

    # pass logging info for subcommands to configure other loggers
    ctx.obj["logging_handler"] = handler
    ctx.obj["logging_level"] = loglevel.upper()


cli.add_command(projection)
cli.add_command(application)
cli.add_command(bucket)
cli.add_command(data_connector)
cli.add_command(secret)

if __name__ == "__main__":
    cli()
