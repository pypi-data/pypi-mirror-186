""" Create command for Edge, Fleet and Device (Remote) """
import logging

import typer

from ..nuvlaio.edge import Edge


app = typer.Typer()
logger: logging.Logger = logging.getLogger(__name__)


@app.command(name='edge')
def remove_edge(uuid: str = typer.Option(..., help='NuvlaEdge unique uuid')) -> None:
    """
    Removes a NuvlaEdge provided a UUID
    """
    it_edge: Edge = Edge()

    it_edge.remove_edge(uuid)


@app.command(name='fleet')
def remove_fleet(name: str = typer.Option(..., help='Fleet unique name')) -> None:
    """
    Removes a Fleet of Nuvlaedge provided the unique fleet name
    """
    it_edge: Edge = Edge()
    it_edge.remove_fleet(name)
