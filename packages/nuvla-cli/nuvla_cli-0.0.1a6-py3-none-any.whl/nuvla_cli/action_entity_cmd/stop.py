""" Create command for Edge, Fleet and Device (Remote) """
import logging

import typer

from nuvla_cli.nuvlaio.nuvlaedge_engine import NuvlaEdgeEngine


app = typer.Typer()
logger: logging.Logger = logging.getLogger(__name__)


@app.command(name='edge')
def stop_edge(uuid: str = typer.Option(..., help='NuvlaEdge uuid to be stopped')):
    """
    Stops a local NuvlaEdge engine
    """
    deployer: NuvlaEdgeEngine = NuvlaEdgeEngine()

    deployer.stop_edge(uuid)


@app.command(name='fleet')
def stop_fleet(fleet_name: str = typer.Option(..., help='Fleet name to be stopped')):
    """
    Stops a local fleet
    """
    deployer: NuvlaEdgeEngine = NuvlaEdgeEngine()
    deployer.stop_fleet(fleet_name)
