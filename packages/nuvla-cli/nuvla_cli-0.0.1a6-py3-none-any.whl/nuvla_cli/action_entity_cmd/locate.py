""" Create command for Edge, Fleet and Device (Remote) """
import logging
from typing import List, Tuple

import typer

from nuvla_cli.nuvlaio.edge import Edge
from nuvla_cli.common.common import print_warning, print_success
from nuvla_cli.common.geo_location import generate_random_coordinate, locate_nuvlaedge

app = typer.Typer()
logger: logging.Logger = logging.getLogger(__name__)


@app.command(name='edge')
def locate_edge(uuid: str = typer.Option(..., help='NuvlaEdge uuid to be geolocated'),
                country: str = typer.Option(..., help=' Country within to locate the '
                                                      'NuvlaEdge')) \
        -> None:
    """
    Randomly locates the given edge within a country
    """
    edge: Edge = Edge()

    if uuid not in edge.edges.keys():
        print_warning(f'NuvlaEdge {uuid} not present')
        return

    coords: List[Tuple] = generate_random_coordinate(
        count=1,
        country=country
    )

    locate_nuvlaedge(edge.nuvla_api, coords[0], uuid)



@app.command(name='fleet')
def locate_fleet(name: str = typer.Option(..., help='Fleet name to be geolocated'),
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

