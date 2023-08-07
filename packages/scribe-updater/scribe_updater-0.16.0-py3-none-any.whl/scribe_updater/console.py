import os

import click

from scribe_updater.updater import Updater
from scribe_updater.utils import load_json, make_lower, read_csv
from . import __version__


@click.command()
@click.version_option(version=__version__)
@click.option("-t", "--target", help="financial instutions ground truth", required=True)
@click.option("-g", "--ground", help="master ground truth", required=True)
@click.option("-v", "--variables", help="path for the variables csv", required=False)
@click.option("-o", "--output", help="output path for the result", required=True)
@click.option(
    "-m",
    "--mappings",
    help="version mappings json file for finie versions",
    required=False,
)
@click.option(
    "-a",
    "--authtype",
    help="select pba or vba, default is pba",
    required=False,
)
def main(target, ground, output, variables=None, mappings=None, authtype="pba"):
    """A tool to update scribe competency configurations."""
    try:
        target = make_lower(load_json(target))
        ground = make_lower(load_json(ground))
        v = None

        if variables:
            v = read_csv(variables)

        version_map = None
        if os.path.isfile(f"src/scribe_updater/version_mapping/{mappings}"):
            version_map = load_json(f"src/scribe_updater/version_mapping/{mappings}")

        updater = Updater(ground, target, v, output, version_map)

        updater.prep_output_pba()
        updater.update()
        updater.output_to_json()
        updater.get_change_log()
    except Exception as e:
        click.echo(f"error from updater script : {e}")
