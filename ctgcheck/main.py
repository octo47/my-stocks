import fileinput
import re

import click


@click.command()
@click.argument("input_file", type=click.Path(exists=True, path_type=None))
def check(input_file: str):
    with fileinput.input(input_file) as inp:
        holdings = {}
        for l in inp:
            parts = re.split('[ ]+', l)


if __name__ == '__main__':
    check()
