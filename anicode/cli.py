# Copyright (c) 2018 Stephen Bunn (stephen@bunn.io)
# MIT License <https://opensource.org/licenses/MIT>

from . import (__version__,)

import click


CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help']
)


@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.version_option(
    prog_name=__version__.__name__,
    version=__version__.__version__
)
@click.pass_context
def cli(ctx):
    """\b
    anicode

    A quick unicode search tool (by Stephen Bunn).
    """

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_usage())
    ctx.obj = ctx.params


if __name__ == '__main__':
    cli()
