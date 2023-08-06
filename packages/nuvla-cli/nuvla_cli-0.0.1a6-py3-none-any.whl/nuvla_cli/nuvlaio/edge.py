""" Edge helper class """
import logging
import time
from typing import Dict, NoReturn, Set, List

import typer
from rich.table import Table
from rich.console import Console
from rich.progress import track

from nuvla_cli.nuvlaio.cli_api import CliApi as NuvlaAPI
from nuvla.api.models import CimiCollection, CimiResponse

from ..common.common import NuvlaID, print_warning
from ..schemas.edge_schema import EdgeSchema
from ..schemas import cli_constants


class Edge:
    def __init__(self, nuvla_api: NuvlaAPI = None):
        self.logger: logging.Logger = logging.getLogger(self.__class__.__name__)
        self.nuvla_api: NuvlaAPI = nuvla_api if nuvla_api else NuvlaAPI()

        if not self.nuvla_api.is_authenticated():
            print_warning('Not authenticated, login first')
            exit(0)

        # Gather all edge information
        self.edges: Dict[NuvlaID, EdgeSchema] = {}
        self.update_edges()

        # Gather fleets
        self.fleets: Dict[str, Set[NuvlaID]] = {'CLI': set()}
        self.update_fleets()

    def update_fleets(self) -> NoReturn:
        """

        :return:
        """
        for k, v in self.edges.items():
            it_fleets: List = [f.replace(cli_constants.CLI_FLEET_PREFIX, '')
                               for f in v.tags
                               if f.startswith(cli_constants.CLI_FLEET_PREFIX)]
            for it_fleet in it_fleets:
                if it_fleet not in self.fleets.keys():
                    self.fleets[it_fleet] = set()

                self.fleets[it_fleet].add(v.uuid)

            if not it_fleets:
                self.fleets['CLI'].add(v.uuid)

    def update_edges(self) -> NoReturn:
        """

        :return:
        """
        self.edges = {}
        cli_edges: CimiCollection = self.nuvla_api.search(
            'nuvlabox',
            filter={f"tags=='{cli_constants.CLI_TAG}'"})

        for i in cli_edges.resources:
            it_edge: EdgeSchema = EdgeSchema.parse_obj(i.data)
            it_edge.dummy = cli_constants.CLI_DUMMY_TAG in i.data.get('tags')

            self.edges[it_edge.uuid] = it_edge

    def generate_proper_name(self, fleet_name: str) -> str:
        """

        :param fleet_name:
        :return:
        """
        # Standard Name generated '[<FLEET_NAME>] NuvlaEdge_<count>'
        if not fleet_name:
            fleet_name = 'CLI'

        it_name: str = cli_constants.FLEET_DEFAULT_NAME.format(
            fleet_name=fleet_name,
            cnt=len(self.fleets[fleet_name]))
        return it_name

    def create_fleet(self, name: str, count: int, dummy: bool):
        """

        :param name:
        :param count:
        :param dummy:
        :return:
        """
        if name in self.fleets.keys():
            response: bool = typer.confirm(
                f'Fleet name {name} already exists, do you want '
                f'to add {count} edges to the currently '
                f'existing fleet?')
            if not response:
                return

        edge_name: str = cli_constants.FLEET_DEFAULT_NAME.format(fleet_name=name,
                                                                 cnt='{}')
        for i in track(range(count), description=f'Creating {count} edges in fleet '
                                                 f'{name}'):
            self.create_edge(edge_name.format(i), fleet_name=name, dummy=dummy,
                             description='', vpn=False)

    def create_edge(self, name: str, description: str, dummy: bool, fleet_name: str, vpn: bool) \
            -> NuvlaID:
        """

        :param name:
        :param description:
        :param dummy:
        :param fleet_name:
        :param vpn:
        :return:
        """
        self.logger.debug(f'Creating new Edge')

        edge_name: str = name if name else self.generate_proper_name(fleet_name)
        it_edge_conf: EdgeSchema = EdgeSchema(name=edge_name,
                                              description=description,
                                              dummy=dummy)

        # create the instance with the latest release
        it_edge_conf.release = self.nuvla_api.search(
            'nuvlabox-release',
            orderby="created:desc",
            last=1).resources[0].data['release']

        # Version corresponds to the first digit of the release
        it_edge_conf.version = int(it_edge_conf.release.split('.')[0])

        if fleet_name:
            it_edge_conf.tags.append(cli_constants.CLI_FLEET_PREFIX + fleet_name)

        if dummy:
            it_edge_conf.tags.append(cli_constants.CLI_DUMMY_TAG)
            it_edge_conf.refresh_interval = 604800  # Default refresh period of 1 week

        creation_data: dict = it_edge_conf.dict(exclude={'dummy', 'uuid', 'fleets', 'started', 'release', 'state'},
                                                by_alias=True)

        if not vpn:
            creation_data.pop('vpn-server-id')

        response: CimiResponse = self.nuvla_api.add(
            'nuvlabox',
            data=creation_data)
        it_edge_conf.uuid = response.data.get('resource-id')
        self.edges[it_edge_conf.uuid] = it_edge_conf
        return it_edge_conf.uuid

    def list_fleets(self):
        """

        :return:
        """
        print('\n\tCurrently registered fleets: \n')
        table: Table = Table("Fleet Name", "UUIDS", show_lines=True)
        for k, v in self.fleets.items():

            table.add_row(k, ', '.join(v))
        console: Console = Console()
        console.print(table)

    def list_edges(self):
        """

        :return:
        """
        print('\n\tCurrently registered devices: \n')
        table: Table = Table("Name", "UUID", "Fleets", "State")
        for k, v in self.edges.items():
            if not v.fleets:
                v.fleets.append('CLI')
            table.add_row(v.name, k, ",\n".join(v.fleets), v.state)

        console: Console = Console()
        console.print(table)

    def remove_edge(self, uuid: str, force: bool = False):
        """

        :param uuid:
        :param force:
        :return:
        """
        if not force:
            typer.confirm(f'Are you sure you want to delete the Edge {uuid}', abort=True)

        ne_state: str = self.nuvla_api.search(
            'nuvlabox', filter=f'id=="{uuid}"').resources[0].data['state']
        if ne_state in ['COMMISSIONED', 'ACTIVATED']:
            self.logger.info('Decommissioning...')
            self.nuvla_api.get(uuid + "/decommission")

        while ne_state not in ['DECOMMISSIONED', 'NEW']:
            time.sleep(1)
            ne_state = self.nuvla_api.search(
                'nuvlabox', filter=f'id=="{uuid}"').resources[0].data['state']

        self.nuvla_api.delete(uuid)

    def remove_fleet(self, fleet_name: str):
        """

        :param fleet_name:
        :return:
        """
        if fleet_name not in self.fleets.keys():
            print_warning(f'Fleet name {fleet_name} not present')
            return

        typer.confirm(f'Are you sure you want to delete Fleet: {fleet_name} ', abort=True)

        for uuid in self.fleets.get(fleet_name):
            self.remove_edge(uuid, force=True)

    def remove_edge_from_fleet(self):
        ...

    def add_edge_to_fleet(self):
        ...

    def get_state_from_uuid(self, uuid: str):
        return self.nuvla_api.search(
            'nuvlabox', filter=f'id=="{uuid}"').resources[0].data['state']

    def get_tags_from_uuid(self, uuid: str):
        return self.nuvla_api.search(
            'nuvlabox', filter=f'id=="{uuid}"').resources[0].data['tags']

    def add_tags_to_edge(self, uuid: NuvlaID, tags: List[str]):
        """

        :param uuid:
        :param tags:
        :return:
        """
        unique_tags: Set = set(tags)
        unique_tags.add(cli_constants.CLI_TAG)
        for i in self.get_tags_from_uuid(uuid):
            unique_tags.add(i)

        self.nuvla_api.edit(uuid, data={'tags': list(unique_tags)})

