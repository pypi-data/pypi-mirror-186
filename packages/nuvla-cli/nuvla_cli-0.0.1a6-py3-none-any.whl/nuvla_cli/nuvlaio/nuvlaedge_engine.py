import logging
from typing import List, Set
from threading import Thread

from rich import print
from rich.progress import track


from .edge import Edge
from .device import Device, DeviceTypes, DEVICE_FACTORY, DeviceConfiguration
from ..common.common import NuvlaID, print_warning
from ..schemas.edge_schema import EdgeSchema
from ..schemas.engine_schema import engine_cte, EngineSchema
from ..schemas.nuvla_schema import cli_constants


class NuvlaEdgeEngine:
    BASE_ENGINE_CONFIG: EngineSchema = EngineSchema()

    def __init__(self):
        """

        """
        self.logger: logging.Logger = logging.getLogger(self.__class__.__name__)

        self.edge: Edge = Edge()
        self.engine_fleet_check: List[Thread] = []

    def build_engine_configuration(self, present_engines: List[str], uuid: NuvlaID,
                                   engine_files: List[str]) \
            -> EngineSchema:
        """

        :param engine_files:
        :param uuid:
        :param present_engines:
        :return:
        """
        cli_engines: List = [i for i in present_engines
                             if i.startswith(engine_cte.project_base_name)]

        cnt: int = len(cli_engines)
        new_schema: EngineSchema = EngineSchema(
            JOB_PORT=self.BASE_ENGINE_CONFIG.JOB_PORT + cnt,
            AGENT_PORT=self.BASE_ENGINE_CONFIG.AGENT_PORT + cnt,
            NUVLABOX_UUID=uuid,
            NUVLAEDGE_UUID=uuid,
            VPN_INTERFACE_NAME=self.BASE_ENGINE_CONFIG.VPN_INTERFACE_NAME + str(cnt),
            COMPOSE_PROJECT_NAME=self.BASE_ENGINE_CONFIG.COMPOSE_PROJECT_NAME + str(cnt),
            engine_files=engine_files
        )
        return new_schema

    def generate_fleet_configuration(self,
                                     present_engines: List[str],
                                     uuids: List[str],
                                     engine_files: List[str],
                                     fleet_name: str) -> List[EngineSchema]:
        """

        :param engine_files:
        :param present_engines:
        :param uuids:
        :return:
        """
        cli_engines: List = [i for i in present_engines
                             if i.startswith(engine_cte.project_base_name)]
        cnt: int = len(cli_engines)
        configs: List[EngineSchema] = []
        for i, uuid in enumerate(uuids):
            print(i, uuid)
            configs.append(
                EngineSchema(
                    JOB_PORT=self.BASE_ENGINE_CONFIG.JOB_PORT + cnt + i,
                    AGENT_PORT=self.BASE_ENGINE_CONFIG.AGENT_PORT + cnt + i,
                    NUVLABOX_UUID=uuid,
                    NUVLAEDGE_UUID=uuid,
                    VPN_INTERFACE_NAME=self.BASE_ENGINE_CONFIG.VPN_INTERFACE_NAME + str(
                        cnt + i),
                    COMPOSE_PROJECT_NAME=(fleet_name.lower() + '_' + str(cnt + i)),
                    engine_files=engine_files
                )
            )
        return configs

    def start_engine(self, uuid: str, target: DeviceTypes, engine_files: List[str]):
        """

        :param engine_files:
        :param uuid:
        :param target:
        :return:
        """
        self.logger.debug(f'Starting edge in {target} device')

        if cli_constants.CLI_DUMMY_TAG in self.edge.edges.get(NuvlaID(uuid)).tags:
            target = DeviceTypes.DUMMY

        device: Device = DEVICE_FACTORY[target.name](DeviceConfiguration(address='local',
                                                                         user='local'))
        engine_config = EngineSchema(NUVLABOX_UUID=uuid, NUVLAEDGE_UUID=uuid)
        if target != DeviceTypes.DUMMY:
            engine_config = \
                self.build_engine_configuration(device.gather_present_engines(),
                                                NuvlaID(uuid),
                                                engine_files)
        device.start(engine_config)
        if target != DeviceTypes.DUMMY:
            self.edge.add_tags_to_edge(
                NuvlaID(uuid),
                tags=[engine_cte.local_engine_type,
                      engine_cte.cli_engine_name_tag+engine_config.COMPOSE_PROJECT_NAME,
                      engine_cte.started_engine_tag])

    def start_fleet(self, fleet_name: str, target: DeviceTypes, engine_files: List[str] = None):
        """

        :param engine_files:
        :param fleet_name:
        :param target:
        :return:
        """
        if fleet_name not in self.edge.fleets.keys():
            print(f'Fleet {fleet_name} not present, create it first')
            return
        edges: Set = self.edge.fleets.get(fleet_name)
        is_dummy: bool = \
            (cli_constants.CLI_DUMMY_TAG
             in self.edge.edges.get(NuvlaID(list(edges)[0])).tags)

        if is_dummy:
            target = DeviceTypes.DUMMY

        device: Device = DEVICE_FACTORY[target.name](
            DeviceConfiguration(address='local',
                                user='local'))
        if not is_dummy:
            engine_configurations: List[EngineSchema] = \
                self.generate_fleet_configuration(
                    device.gather_present_engines(),
                    list(edges),
                    engine_files,
                    fleet_name
                )
        else:
            engine_configurations: List[EngineSchema] = \
                [EngineSchema(NUVLABOX_UUID=uuid, NUVLAEDGE_UUID=uuid) for uuid in edges]

        for i in track(engine_configurations, description=f'Starting fleet {fleet_name}'):
            device.start(i)
            self.edge.add_tags_to_edge(
                NuvlaID(i.NUVLABOX_UUID),
                tags=[engine_cte.local_engine_type,
                      engine_cte.cli_engine_name_tag + i.COMPOSE_PROJECT_NAME,
                      engine_cte.started_engine_tag])

    def stop_edge(self, uuid: str):
        """

        :return:
        """
        if uuid not in self.edge.edges.keys():
            print(f'Edge not present')
            return
        edge_data: EdgeSchema = self.edge.edges.get(NuvlaID(uuid))
        if engine_cte.started_engine_tag not in edge_data.tags:
            print('Trying to stop a non started engine')
            return
        elif cli_constants.CLI_DUMMY_TAG in edge_data.tags:
            print('Trying to stop a dummy edge, delete instead')
            return
        else:
            device: Device = DEVICE_FACTORY['LOCAL'](
                DeviceConfiguration(address='local',
                                    user='local'))

            project_name: List[str] = [i for i in edge_data.tags
                                       if i.startswith(engine_cte.cli_engine_name_tag)]
            print(project_name)
            if project_name:
                device.stop(project_name[0].replace(engine_cte.cli_engine_name_tag, ''))
            else:
                print('Something went wrong')

    def stop_fleet(self, fleet_name: str):

        if fleet_name not in self.edge.fleets.keys():
            print(f'Fleet {fleet_name} not present, create it first')
            return

        edges: Set = self.edge.fleets.get(fleet_name)

        for uuid in edges:
            if uuid not in self.edge.edges.keys():
                print(f'Edge {uuid} not present')
                return
            edge_data: EdgeSchema = self.edge.edges.get(NuvlaID(uuid))
            if engine_cte.started_engine_tag not in edge_data.tags:
                print('Trying to stop a non started fleet')
                return
            elif cli_constants.CLI_DUMMY_TAG in edge_data.tags:
                print('Trying to stop a dummy fleet, delete instead')
                return
            self.stop_edge(uuid)
