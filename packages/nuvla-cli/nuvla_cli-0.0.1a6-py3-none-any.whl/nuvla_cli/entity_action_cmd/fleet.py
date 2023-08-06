"""

"""
import logging
from typing import List, Tuple

import typer

from nuvla_cli.nuvlaio.edge import Edge
from nuvla_cli.common.common import print_warning
from nuvla_cli.nuvlaio.device import DeviceTypes
from nuvla_cli.nuvlaio.nuvlaedge_engine import NuvlaEdgeEngine
from nuvla_cli.common.geo_location import generate_random_coordinate, locate_nuvlaedge


app = typer.Typer()
logger: logging.Logger = logging.getLogger(__name__)


@app.command(name='create')
def create_fleet(name: str = typer.Option(..., help='Fleet name desired. Must be unique,'
                                                    ' as it works as identifier'),
                 count: int = typer.Option(10, help='# of Edges to create within the'
                                                    ' fleet'),
                 dummy: bool = typer.Option(False, help='Create a fleet of dummy edges')):
    """
    Creates a new Fleet of Edges in Nuvla
    """
    logger.debug(f'Creating {name} NuvlaEdge')

    it_edge: Edge = Edge()
    it_edge.create_fleet(name=name, count=count, dummy=dummy)


@app.command(name='start')
def start_fleet(fleet_name: str = typer.Option(..., help='Fleet name to be started'),
                engine_file: str = typer.Option('', help='.yml file to use in the start of the engines')):
    """
    Starts a Fleet in the device running this CLI. Only for dummy fleets

    If the fleet entity is created as dummy, it will perform the activation and
    commissioning process
    """
    deployer: NuvlaEdgeEngine = NuvlaEdgeEngine()

    deployer.start_fleet(fleet_name, DeviceTypes.LOCAL, engine_files=[engine_file])


@app.command(name='geolocate')
def geolocate_fleet(name: str = typer.Option(..., help='Fleet name to be geolocated'),
                    country: str = typer.Option(..., help=' Country within to locate the '
                                                          'fleet')) \
        -> None:
    """
    Randomly locates the given fleet within a country
    """
    edge: Edge = Edge()

    if name not in edge.fleets.keys():
        print_warning(f'Fleet name {name} not present')
        return

    coords: List[Tuple] = generate_random_coordinate(
        count=len(edge.fleets.get(name)),
        country=country
    )

    for uuid, coord in zip(edge.fleets.get(name), coords):
        locate_nuvlaedge(edge.nuvla_api, coord, uuid)


@app.command(name='remove')
def remove_fleet(name: str = typer.Option(..., help='Fleet unique name')) -> None:
    """
    Removes a Fleet of Nuvlaedge provided the unique fleet name
    """
    print(f'Creating edge class...')
    it_edge: Edge = Edge()

    print(f'Removing fleet')
    it_edge.remove_fleet(name)


@app.command(name='list')
def list_fleet() -> None:
    """
    Retrieves and prints the list of fleet names created by CLI

    """
    it_edge: Edge = Edge()
    it_edge.list_fleets()
