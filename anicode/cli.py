# Copyright (c) 2018 Stephen Bunn (stephen@bunn.io)
# MIT License <https://opensource.org/licenses/MIT>

import sys
import cgi
import collections

from . import (__version__,)
from .anicode import (Anicode,)

import halo
import click
import spinners
import colorama
import pyperclip

COLOR = {
    'fore': colorama.Fore,
    'back': colorama.Back,
    'style': colorama.Style,
}
CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help']
)


def _validate_spinner(ctx, param, value):
    """ Validates if a spinner string binds to a spinner.

    :param click.Context ctx: The calling clicks current context
    :param str param: The parameter name
    :param str value: The given value of the parameter
    :raises click.BadParameter:
        - when the spinner value is not a valid spinner
    :returns: The spinner value
    :rtype: str
    """

    spinner_names = [_.name for _ in spinners.spinners.Spinners]
    if value not in spinner_names:
        raise click.BadParameter((
            "spinner '{value}' does not exist, {spinner_names}"
        ).format(**locals()))
    return value


def _render_results(results):
    """ Renders a list of results to stdout.

    :param results: The list of results to write to stdout
    :type results: list[AnicodeResult]
    :returns: Does not return
    """

    for (result_idx, result,) in enumerate(results.values()):
        sys.stdout.write((
            '{style.BRIGHT}{fore.CYAN}{result_idx:>3}{style.RESET_ALL} ➜  '
            '{result.char}  {style.DIM}{result.name}{style.RESET_ALL}\n'
        ).format(**locals(), **COLOR))


def _select_result(results):
    """ Prompts the user to choose a result from the rendered results.

    :param results: The list of results to choose from
    :type results: list[AnicodeResult]
    :returns: The chosen result
    :rtype: AnicodeResult
    """

    choice = input((
        '{style.BRIGHT}[ {fore.CYAN}select character{fore.RESET} ]: '
        '{style.RESET_ALL}'
    ).format(**COLOR))
    if not choice.isdigit():
        raise ValueError((
            "{choice} is not a valid digit"
        ).format(**locals()))

    choice = int(choice)
    if choice < 0 or choice > (len(results) - 1):
        raise ValueError((
            "{choice} is not a valid character index"
        ).format(**locals()))

    return list(results.values())[choice]


def _copy_result(result, html=False):
    """ Copies a given result to the clipboard.

    :param AnicodeResult result: The result to copy
    :param bool html: True if should copy html code instead of unicode
    :returns: Does not return
    """

    (copy_from, extra_spacing,) = (result.char, ' ',)
    if html:
        copy_from = cgi.escape(copy_from).encode(
            'ascii', 'xmlcharrefreplace'
        ).decode('ascii')
        extra_spacing = ''

    sys.stdout.write((
        'copying {fore.GREEN}{copy_from}{fore.RESET}{extra_spacing} '
        'to clipboard... '
    ).format(**locals(), **COLOR))
    pyperclip.copy(copy_from)
    sys.stdout.write((
        '{style.BRIGHT}{fore.GREEN}✓{style.RESET_ALL}\n'
    ).format(**COLOR))


@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.version_option(
    prog_name=__version__.__name__,
    version=__version__.__version__
)
@click.pass_context
def cli(ctx):
    """ The command-line interface to Anicode.

    \b
    Usage:
    \b
        anicode search "query" - (searches for a unicode character)
    """

    if ctx.invoked_subcommand is None:
        click.echo(__version__.__fancy__)
        click.echo(ctx.get_usage())
    ctx.obj = ctx.params


@click.command(
    'search',
    short_help='Searches for a unicode character',
    context_settings={
        'ignore_unknown_options': True
    }
)
@click.argument('query')
@click.option(
    '--count',
    type=int, default=30,
    help='Number of results to render'
)
@click.option(
    '--spinner',
    type=str, default='dots',
    help='Customize spinner type', callback=_validate_spinner
)
@click.option(
    '--html',
    is_flag=True, default=False,
    help='Copy HTML encoding rather than unicode'
)
@click.pass_context
def cli_search(
    ctx,
    query=None, count=30, spinner='dots',
    html=False
):
    client = Anicode()
    with halo.Halo(
        text=((
            'searching for {fore.CYAN}{style.BRIGHT}{query}'
            '{style.RESET_ALL}...'
        ).format(**locals(), **COLOR)),
        spinner=spinner
    ) as spinner:
        results = client.search(query, count=count)

    if len(results) <= 0:
        sys.stdout.write((
            '{fore.YELLOW}no results found{fore.RESET}\n'
        ).format(**COLOR))
        sys.exit(1)

    _render_results(results)
    while True:
        try:
            _copy_result(_select_result(results), html=html)
            sys.exit(0)
        except ValueError as exc:
            sys.stdout.write((
                '{style.BRIGHT}{fore.RED}ERROR:{style.RESET_ALL} '
                '{exc}\n'
            ).format(**locals(), **COLOR))
        except (KeyboardInterrupt, EOFError,) as exc:
            sys.stdout.write((
                '{fore.YELLOW}user interrupted{fore.RESET}\n'
            ).format(**COLOR))
            sys.exit(1)


cli.add_command(cli_search)


if __name__ == '__main__':
    cli()
