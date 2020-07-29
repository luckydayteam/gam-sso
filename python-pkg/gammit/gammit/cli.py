""" CLI interface for the gammit tool """

import click
import sys

from .utils import ( GAM )

if sys.version_info <= (3, 0):
    sys.stdout.write("Sorry, requires Python 3.x, not Python 2.x\n")
    sys.exit(1)

def main():
    main_unchecked()

@click.group(context_settings={'help_option_names': ['-h', '--help']})
def main_unchecked(**kwargs):
    pass

### main ###

@main_unchecked.command(help='Update users via GAM')
@click.option('--domain', '-d', required=True, help="G-Suite domain ")
def update(**kwargs):
    g = GAM()
    g.go(**kwargs)
