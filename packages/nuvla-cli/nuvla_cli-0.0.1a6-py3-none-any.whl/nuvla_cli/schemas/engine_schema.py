"""
"""
from typing import List

from pydantic import BaseModel

from nuvla_cli.common.common import NuvlaID


class EngineConstants:
    project_base_name: str = 'nuvlaedge_'
    started_engine_tag: str = 'cli.engine.started=True'
    cli_engine_name_tag: str = 'cli.engine.name='
    local_engine_type: str = 'cli.engine.type=local'
    remote_engine_type: str = 'cli.engine.type=remote'
    BASE_DEPLOYMENT_COMMAND: str = 'docker compose -p {project_name} -f {files} {action}'


engine_cte: EngineConstants = EngineConstants()


class EngineSchema(BaseModel):
    JOB_PORT: int = 5000
    AGENT_PORT: int = 5500
    NUVLABOX_UUID: NuvlaID = ''
    NUVLAEDGE_UUID: NuvlaID = ''
    VPN_INTERFACE_NAME: str = 'vpn_'
    COMPOSE_PROJECT_NAME: str = 'cli_nuvlaedge_'
    EXCLUDED_MONITORS: str = 'geolocation,container_stats_monitor'

    # Engine deployment files
    engine_files: List[str] = []
