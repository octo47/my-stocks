import click

from etrade import rsu_parser, espp_parser, gnl_parser


@click.group()
def cli():
    pass


@click.command()
@click.argument("input_file", type=click.Path(exists=True, path_type=None))
def rsu(input_file: str):
    with open(input_file, 'r', newline='') as inp:
        rsu_parser.convert(inp)


@click.command()
@click.argument("input_file", type=click.Path(exists=True, path_type=None))
def espp(input_file: str):
    with open(input_file, 'r', newline='') as inp:
        espp_parser.convert(inp)


@click.command()
@click.argument("input_file", type=click.Path(exists=True, path_type=None))
def gnl(input_file: str):
    with open(input_file, 'r', newline='') as inp:
        gnl_parser.convert(inp)


if __name__ == '__main__':
    cli.add_command(rsu)
    cli.add_command(espp)
    cli.add_command(gnl)
    cli()
