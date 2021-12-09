import csv
import fileinput

import click
import typing as t

from etrade import rsu_parser


@click.group()
def cli():
    pass


@click.command()
@click.argument("input_file", type=click.Path(exists=True, path_type=None))
def rsu(input_file: str):
    with open(input_file, 'r', newline='') as inp:
        rsu_parser.convert(inp)


if __name__ == '__main__':
    cli.add_command(rsu)
    cli()
