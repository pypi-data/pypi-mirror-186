"""

"""
import logging
from pathlib import Path
from typing import Any

from nuvla.api import Api
from rich.prompt import IntPrompt

from nuvla_cli.common.constants import LOCAL_PATH


class CliApi(Api):
    def __init__(self,
                 endpoint: str = 'https://nuvla.io',
                 insecure: bool = False,
                 persist_cookie: bool = True,
                 cookie_file: Any = None,
                 reauthenticate: bool = False,
                 login_creds: dict = None,
                 authn_header: Any = None,
                 debug: bool = False,
                 compress: bool = False):

        self.logger: logging.Logger = logging.getLogger(__name__)

        # Asses endpoint from cookie if exists
        if not cookie_file:
            cookie_location: Path = LOCAL_PATH / 'cookies.txt'
        else:
            cookie_location: Path = Path(cookie_file)

        if cookie_location.exists():
            self.logger.info(f'Path exists in {cookie_location}')
            available_cookies: list = []
            secure: list = []
            with cookie_location.open('r') as file:
                for line in file.readlines():
                    if line.startswith('#') or not line.strip():
                        continue
                    else:
                        clean_line: list = line.strip().replace('\t', ' ').split(' ')
                        available_cookies.append(clean_line[0])
                        secure.append((clean_line[3]).lower())

            if len(available_cookies) > 0:
                choice = 0
                if len(available_cookies) > 1:

                    print(f'Multiple sessions stored: {available_cookies}, please choose one to load')
                    choice: int = IntPrompt.ask(f'Choose one {list(enumerate(available_cookies))}')

                endpoint = 'https://' + available_cookies[choice]
                insecure = secure[choice] == 'true'

        super().__init__(endpoint, insecure, persist_cookie, cookie_file, reauthenticate, login_creds, authn_header,
                         debug, compress)


