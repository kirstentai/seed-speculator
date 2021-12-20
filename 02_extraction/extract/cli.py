import click
from extract.extract_meta import main

@click.command()
def cli():
    main()