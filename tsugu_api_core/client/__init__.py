'''`tsugu_api_python` HTTP 客户端模块'''

from typing import Type, Optional

from tsugu_api_core._settings import settings

from ._client import Client as Client
from ._client import Request as Request
from ._client import Response as Response

__HTTPClient__: Optional[Type[Client]] = None

def register_client(
    client: Type[Client]
) -> None:
    '''注册一个 HTTP 客户端类，之后将会使用该客户端发送请求而不是内置客户端。

    参数:
        client (Type[Client]): HTTP 客户端类
    '''
    global __HTTPClient__
    __HTTPClient__ = client
    return

def _Client() -> Type[Client]:
    '''获取当前使用的 HTTP 客户端

    返回:
        Client: HTTP 客户端
    '''
    global __HTTPClient__
    if __HTTPClient__ is not None:
        return __HTTPClient__
    
    if settings.client.lower() == 'httpx':
        from .httpx import Client as HTTPXClient
        __HTTPClient__ = HTTPXClient
        return __HTTPClient__
    elif settings.client.lower() == 'aiohttp':
        from .aiohttp import Client as AIOHTTPClient
        __HTTPClient__ = AIOHTTPClient
        return __HTTPClient__
    else:
        raise ValueError('Unknown client type')