import click

from neurodocker import __version__
from neurodocker.cli.generate import generate
from neurodocker.cli.generate import genfromjson


@click.group()
@click.version_option(__version__, message="%(prog)s version %(version)s")
def cli():
    """Generate custom containers, and minify existing containers.

    Note: The minify command has been removed due to lack of ptrace in docker.
    """


cli.add_command(generate)
cli.add_command(genfromjson)

# `docker-py` is required for minification but is not installed by default.
# We also pass if there is an error retrieving the Docker client.
# Say, for example, the Docker engine is not running (or it is not installed).
"""
# Removing minify due to lack of ptrace availability in docker

try:
    from neurodocker.cli.minify.trace import minify
    cli.add_command(minify)
except (ImportError, RuntimeError):
    # TODO: should we log a debug message? We don't even have a logger at the
    # time of writing, so probably not.
    pass
"""
