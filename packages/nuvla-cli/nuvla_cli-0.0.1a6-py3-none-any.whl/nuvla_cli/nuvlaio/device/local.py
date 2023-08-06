"""
Local device implementation module
"""
import os
import json
import logging
from typing import Dict, List
from subprocess import Popen, check_output, DEVNULL

from .device import Device, DeviceConfiguration
from ...schemas.engine_schema import EngineSchema, engine_cte


class LocalDevice(Device):
    def __init__(self, device_config: DeviceConfiguration):
        super().__init__(device_config)
        self.logger: logging.Logger = logging.getLogger(self.__class__.__name__)

    @staticmethod
    def generate_deployment_config(uuid, n):
        it_conf: EngineSchema = EngineSchema(
            JOB_PORT=5000 + n,
            AGENT_PORT=5500 + n,
            NUVLABOX_UUID=uuid,
            NUVLAEDGE_UUID=uuid,
            COMPOSE_PROJECT_NAME='nuvlaedge_{}'.format(n),
            VPN_INTERFACE_NAME='vpn_{}'.format(n),
            EXCLUDED_MONITORS='geolocation,container_stats_monitor'
        )
        return it_conf

    def start(self, config: EngineSchema):

        self.logger.info('Starting engine locally')
        deployment_envs: Dict = os.environ.copy()
        deployment_envs.update(config.dict(exclude={'engine_files'}))
        for k, v in deployment_envs.items():
            deployment_envs[k] = str(v)

        if not config.engine_files:
            raise Exception('Engine files not provided')

        deployment_command: str = engine_cte.BASE_DEPLOYMENT_COMMAND.format(
            project_name=config.COMPOSE_PROJECT_NAME,
            files=' -f '.join(config.engine_files),
            action='up')
        print(deployment_command)

        Popen(deployment_command.split(),
              env=deployment_envs,
              stdout=DEVNULL,
              stderr=DEVNULL)

    def stop(self, project_name: str):
        stop_command: str = engine_cte.BASE_DEPLOYMENT_COMMAND.format(
            project_name=project_name,
            files='-f docker-compose.yml',
            action='down'
        )

        Popen(stop_command.split(),
              stdout=DEVNULL,
              stderr=DEVNULL)

    def gather_present_engines(self) -> List:
        """

        :return:
        """
        result = check_output(['docker', 'compose', 'ls', '--format', 'json'])\
            .decode('utf-8')

        engine_names: List = [name.get('Name') for name in json.loads(result)]
        return engine_names
