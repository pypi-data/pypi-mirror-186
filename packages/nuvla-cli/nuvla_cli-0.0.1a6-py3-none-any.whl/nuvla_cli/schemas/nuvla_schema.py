""" Schema for Nuvla.io configuration """
from typing import Dict, Optional

from pydantic import BaseSettings, Field, BaseModel

from ..common.common import NuvlaID
from ..schemas.edge_schema import EdgeSchema


class NuvlaSchema(BaseSettings):
    nuvla_endpoint: str = Field('https://nuvla.io', env='NUVLA_ENDPOINT')

    # User
    api_key: str = Field(None, env='NUVLA_API_KEY')
    api_secret: str = Field(None, env='NUVLA_API_SECRET')


class NuvlaIOCLI(BaseModel):
    edges: Dict[NuvlaID, EdgeSchema]
    user: str
    credentials: str
    deployments: str
    apps: str


class CLIConstants(BaseModel):
    DEFAULT_NAME: str = '[CLI] NuvlaEdge_'
    CLI_TAG: str = 'cli.created=True'
    CLI_DUMMY_TAG: str = 'cli.dummy=True'
    CLI_FLEET_PREFIX: str = 'cli.fleet.name='
    FLEET_DEFAULT_NAME: str = '[{fleet_name}] NuvlaEdge_{cnt}'


cli_constants: CLIConstants = CLIConstants()

