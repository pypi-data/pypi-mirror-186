from __future__ import annotations
from enum import Enum

NAME = 'tickerdax'
URL = f'https://{NAME}.com'


class BaseEnum(str, Enum):
    value: str
    description: str

    def __new__(
            cls, value: str, description: str = ""
    ) -> BaseEnum:
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.description = description
        return obj

    @classmethod
    def list(cls):
        return list(map(lambda e: (e.value, e.description), cls))


class KeyTypes:
    REST = 'REST'
    WEBSOCKET = 'WEBSOCKET'


class Envs(BaseEnum):
    DEV = (f'{NAME.upper()}_DEV', '')
    OFFICIAL_DOCKER_IMAGE = (f'{NAME.upper()}_OFFICIAL_DOCKER_IMAGE', '')

    CONFIG = (
        f'{NAME.upper()}_CONFIG',
        'A file path to the config file for the CLI.'
    )
    EMAIL = (
        f'{NAME.upper()}_EMAIL',
        'Your email linked to your tickerdax.com account.'
    )
    REST_API_KEY = (
        f'{NAME.upper()}_REST_API_KEY',
        'Your REST API created with your tickerdax.com account.'
    )
    WEBSOCKET_API_KEY = (
        f'{NAME.upper()}_WEBSOCKET_API_KEY',
        'Your websocket API created with your tickerdax.com account. '
    )
    CACHE_ROOT = (
        f'{NAME.upper()}_CACHE_ROOT',
        "An alternative persistent cache location on disk. By default this is written into a `tickerdax_cache` folder "
        "in your system's temp folder."
    )
    REDIS_SERVER_ADDRESS = (
        f'{NAME.upper()}_REDIS_SERVER_ADDRESS',
        'An alternative redis server address. Can be useful if redis is on another address besides localhost.'
    )
    REDIS_SERVER_PORT = (
        f'{NAME.upper()}_REDIS_SERVER_PORT',
        'An alternative redis server port. Can be useful if redis needs to user another port besides `6379`.'
    )
