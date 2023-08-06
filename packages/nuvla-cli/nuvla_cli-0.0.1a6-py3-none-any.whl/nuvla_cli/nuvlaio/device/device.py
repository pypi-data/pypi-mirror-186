"""
Device  base/common module for engine deployments
"""
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, Dict

from pydantic import BaseModel

from nuvla_cli.schemas.engine_schema import EngineSchema


class DeviceTypes(str, Enum):
    REMOTE = 'REMOTE'
    LOCAL = 'LOCAL'
    DUMMY = 'DUMMY'

    @staticmethod
    def from_str(label):
        if label in ('remote', 'REMOTE'):
            return DeviceTypes.REMOTE
        elif label in ('local', 'LOCAL'):
            return DeviceTypes.LOCAL
        elif not label or label in ('dummy', 'DUMMY'):
            return DeviceTypes.DUMMY
        else:
            raise NotImplementedError


class DeviceConfiguration(BaseModel):
    address: str
    user: str
    port: int = 22
    hostname: Optional[str]
    docker: Optional[str]
    docker_compose: Optional[str]
    pub_key: Optional[str]
    deployments: Dict[str, EngineSchema] = {}
    online: bool = False
    device_type: Optional[str]


class Device(ABC):

    def __init__(self, device_config: DeviceConfiguration):
        """

        :param device_config:
        """
        self.device_config: DeviceConfiguration = device_config

    @abstractmethod
    def start(self, config: EngineSchema):
        """
        Starts a nuvlaedge engine
        :param config:
        :return: None
        """
        ...

    @abstractmethod
    def stop(self, project_name: str):
        """
        Stops a nuvlaedge engine
        :param project_name:
        :return: None
        """
        ...

    @abstractmethod
    def gather_present_engines(self):
        ...
