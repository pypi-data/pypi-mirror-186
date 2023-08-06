"""
Remote device implementation module
"""
import logging

from fabric import Connection
from fabric.runners import Result

from ...schemas.engine_schema import EngineSchema
from .device import Device, DeviceConfiguration


class RemoteDevice(Device):
    def __init__(self, device_config: DeviceConfiguration):
        super().__init__(device_config)
        self.logger: logging.Logger = logging.getLogger(self.__class__.__name__)

        self.dev_connection: Connection = Connection(
            self.device_config.address,
            self.device_config.user,
            self.device_config.port,
            connect_kwargs={"password": 'pi'})

        if not device_config.hostname:
            hostname: str = self.reachable()
            if hostname:
                self.device_config.hostname = hostname
                self.device_config.online = True
            self.check_dev_requirements()

    def reachable(self):
        """

        :return:
        """
        response: Result = self.dev_connection.run('hostname', hide=True)
        if self.dev_connection.is_connected:
            return response.stdout
        else:
            return ''

    def check_dev_requirements(self) -> bool:
        """

        :return:
        """
        result: Result = self.dev_connection.run('docker -v', hide=True)
        if result.return_code != 0:
            return False
        docker_version: str = result.stdout.split(',')[0].split(' ')[-1]

        result: Result = self.dev_connection.run('docker-compose -v', hide=True)
        docker_compose_version: str = result.stdout
        if result.return_code != 0:
            return False

        self.device_config.docker = docker_version
        self.device_config.docker_compose = docker_compose_version
        return True

    def start(self, config: EngineSchema):
        # 1.- Copy docker-compose
        # 2.- Parse config to env variables
        # 3.- Launch
        pass

    def stop(self, uuid: str):
        pass

    def gather_present_engines(self):
        ...