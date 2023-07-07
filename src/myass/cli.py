#!/usr/bin/env python3

import click
import confuse

from myass.assistant import Assistant


@click.command()
@click.argument('name')
def main(name):
    try:
        assistant = Assistant(name)
    except confuse.exceptions.ConfigError as e:
        raise click.ClickException(e)
    while True:
        click.echo(assistant(click.prompt(name)))


if __name__ == '__main__':
    main()