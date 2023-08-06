"""
Dummy device module implementation
"""

import logging

from nuvla_cli.nuvlaio.cli_api import CliApi as Api

from .device import Device, DeviceConfiguration
from ...schemas.engine_schema import EngineSchema


class DummyDevice(Device):
    def __init__(self, config: DeviceConfiguration):
        super().__init__(config)
        self.logger: logging.Logger = logging.getLogger(self.__class__.__name__)

    def start(self, config: EngineSchema):
        """

        :param config:
        :return:
        """
        uuid = config.NUVLABOX_UUID
        self.logger.info(f'Starting dummy device')
        nuvla_client: Api = Api()
        info = nuvla_client._cimi_post('{}/activate'.format(uuid))

        self.logger.debug(f'{uuid} Activated')
        nuvla_client: Api = Api(persist_cookie=False, reauthenticate=True, login_creds={
            'key': info.get('api-key'),
            'secret': info.get('secret-key')
        })
        commission_payload = {"swarm-endpoint": "https://10.1.1.1:5000",
                              "swarm-client-ca": "fake",
                              "swarm-client-cert": "fake",
                              "swarm-client-key": "fake",
                              "swarm-token-manager": "fake",
                              "swarm-token-worker": "fake",
                              "capabilities": ["NUVLA_JOB_PULL"]}
        nuvla_client._cimi_post('{}/commission'.format(uuid),
                                json=commission_payload)

        res = nuvla_client.get(uuid)
        nuvlabox_status_id = res.data.get('nuvlabox-status')
        self.logger.debug(f'{nuvlabox_status_id} Commissioned')

        nuvla_client.edit(nuvlabox_status_id, data={'status': 'OPERATIONAL'})

    def stop(self, uuid: str):
        pass

    def gather_present_engines(self):
        ...