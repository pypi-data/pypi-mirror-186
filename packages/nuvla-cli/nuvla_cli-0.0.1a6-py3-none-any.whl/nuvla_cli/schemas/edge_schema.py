""" Schema for NuvlaEdge configuration """
from typing import Optional, List

from pydantic import BaseModel, Field

from nuvla_cli.common.common import NuvlaID


class EdgeSchema(BaseModel):
    name: str
    uuid: NuvlaID = Field('', alias='id')
    dummy: bool = False
    release: Optional[str]
    version: Optional[str]
    tags: List[str] = ['cli.created=True']
    fleets: List[str] = []
    state: Optional[str]
    started: bool = False
    vpn_server_id: str = \
        Field('infrastructure-service/eb8e09c2-8387-4f6d-86a4-ff5ddf3d07d7',
              env='VPN_SERVER_ID', alias='vpn-server-id')
    refresh_interval: Optional[int] = Field(30, alias='refresh-interval')
