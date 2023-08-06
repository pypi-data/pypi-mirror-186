""" Common utilities for CLI """

from typing import List, NoReturn


class NuvlaID(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate_nuvla_id

    @classmethod
    def validate_nuvla_id(cls, nuvla_id: str) -> str:
        id_parts: List[str] = nuvla_id.split('/')
        if len(id_parts) != 2:
            print('Validator called')
            raise ValueError("Nuvla ID's format must me a string with format: "
                             "<resource_id>/<unique-identifier>")

        return nuvla_id


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


colors: Colors = Colors()


def print_warning(message: str) -> NoReturn:
    """

    :param message:
    :return:
    """
    print(f'\n{Colors.WARNING} \tWARNING:{Colors.ENDC} {message}\n')


def print_success(message: str) -> NoReturn:
    """

    :param message:
    :return:
    """
    print(f'\n{Colors.OKGREEN} \tSuccess:{Colors.ENDC} {message}\n')
