from typing import Optional

import click


def echo_error(msg: str):
    click.echo("\x1b(B\x1b[m[\x1b[33m✕\x1b(B\x1b[m] {error}: {message}".format(
        error=click.style('Error', fg='red'),
        message=msg))


def echo_success(msg: Optional[str] = None, only_msg=False):
    if msg is None:
        msg = "Done"

    if not only_msg:
        msg = "\x1b(B\x1b[m[\x1b[33m✓\x1b(B\x1b[m] " + str(msg)

    click.echo(msg)
