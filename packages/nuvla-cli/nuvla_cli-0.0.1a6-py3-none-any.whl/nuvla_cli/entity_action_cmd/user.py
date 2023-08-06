""" Create command for Edge, Fleet and Device (Remote) """
import logging

import typer

from nuvla_cli.nuvlaio.nuvlaio_cli import NuvlaIO

app = typer.Typer()
logger: logging.Logger = logging.getLogger(__name__)


@app.command(name='login')
def login(key: str = typer.Option('', help='Nuvla API key'),
          secret: str = typer.Option('', help='Nuvla API Secret'),
          config_file: str = typer.Option('', help='Optional configuration file path '
                                                   'where the keys are stored.'),
          endpoint: str = typer.Option('https://nuvla.io',
                                       help='Optional configuration for a different Nuvla endpoint'),
          secure: bool = typer.Option(True, help='Whether or not the endpoint is https')) \
        -> None:
    """
    Login to Nuvla. The login is persistent and only with API keys. To create the Key pair
    go to Nuvla/Credentials sections and add a new Nuvla API credential.

    Login is possible via 3 ways: Environmental variables (NUVLA_API_KEY and
    NUVLA_API_SECRET), arguments (key and secret) or via toml configuration file

    """
    nuvla: NuvlaIO = NuvlaIO(endpoint=endpoint, secure=secure, gather_data=False)

    nuvla.log_to_nuvla(key, secret, config_file)


@app.command(name='logout')
def logout(endpoint: str = typer.Option('https://nuvla.io',
                                        help='Optional configuration for a different Nuvla endpoint'),
           secure: bool = typer.Option(True, help='Whether or not the endpoint is https')) -> None:
    """
    Removes the local Nuvla persistent session and stops any open connection
    """
    nuvla: NuvlaIO = NuvlaIO(endpoint=endpoint, secure=secure, gather_data=False)

    nuvla.logout()
