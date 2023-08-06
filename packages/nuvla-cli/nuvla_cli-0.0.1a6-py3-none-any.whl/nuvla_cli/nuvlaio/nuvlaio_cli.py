"""

"""
import logging
from typing import NoReturn

from requests import Response
from rich import print
from nuvla_cli.nuvlaio.cli_api import CliApi as Api

from nuvla.api.models import CimiResource

from ..schemas.user_schema import (UserSchema, SessionSchema)
from ..common.common import print_warning, print_success


class NuvlaIO:
    def __init__(self, endpoint: str = 'https://nuvla.io', secure: bool = True, gather_data: bool = True):
        """

        """
        self.logger: logging.Logger = logging.getLogger(self.__class__.__name__)

        # Nuvla API instance
        self.nuvla_client: Api = Api(endpoint=endpoint, insecure=not secure)

        # UserInfo
        self.user_info: UserSchema = UserSchema()
        self.session_info: SessionSchema = SessionSchema()

        if self.nuvla_client.is_authenticated() and gather_data:
            self.gather_user_info()
        else:
            print_warning(f'Not authenticated')

    def gather_user_info(self) -> NoReturn:
        """

        :return:
        """
        nuvla_session_info: CimiResource = \
            self.nuvla_client.get(self.nuvla_client.current_session())

        self.session_info = SessionSchema.parse_obj(nuvla_session_info.data)
        print(self.session_info)
        nuvla_user_info: CimiResource = self.nuvla_client.get(self.session_info.user)
        self.user_info = UserSchema.parse_obj(nuvla_user_info.data)

    def log_to_nuvla(self, key: str, secret: str, config_file: str) -> NoReturn:
        """
        Logs in to nuvla using the api keys and secret provided via env. variables
        :return: None
        """
        # self.nuvla_client.login_apikey(key=key, secret=secret)

        if self.nuvla_client.is_authenticated():
            session_info = self.nuvla_client.get(self.nuvla_client.current_session())
            user_info = self.nuvla_client.get(session_info.data.get('user'))
            print_success(
                f'Session already authenticated as {user_info.data.get("name")}')
            return

        if self.user_info.API_KEY and self.user_info.API_SECRET:
            print('Logging to Nuvla with environmental variables')

            response: Response = self.nuvla_client.login_apikey(self.user_info.API_KEY,
                                                                self.user_info.API_SECRET)
            print(response.status_code)

        elif key and secret:
            print('Logging to Nuvla with arguments')
            response: Response = self.nuvla_client.login_apikey(key, secret)

        elif config_file:
            print('Logging to Nuvla with configuration not supported yet')
            # self.nuvla_client.login_apikey(key, secret)
            return

        else:
            print_warning('No keys provided via any of the two options: envs or '
                          'CLI options')
            return

        if self.nuvla_client.is_authenticated():
            self.gather_user_info()
            print_success(f'Successfully logged in as {self.user_info.name}')
        else:
            print_warning(f'Not successfully authenticated with code: {response.status_code}')

    def logout(self):
        if not self.nuvla_client.is_authenticated():
            print_warning('Currently not logged in')

        else:
            self.logger.debug('Logging out')
            self.nuvla_client.logout()

