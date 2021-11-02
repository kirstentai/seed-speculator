import click

from scraper.routines import main

@click.command()
def cli():
    main()