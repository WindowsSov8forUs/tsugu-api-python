'''内置的 AIOHTTP 适配'''

from typing import Any, cast
from typing_extensions import override

from ._client import Client as _Client
from ._client import Request, Response

try:
    import aiohttp
except ModuleNotFoundError as exception:
    raise ImportError(
        'module \'aiohttp\' is not installed, please install it by running \'pip install aiohttp\''
    ) from exception

class Client(_Client):
    _client_session: aiohttp.ClientSession
    
    @override
    def __enter__(self) -> 'Client':
        raise RuntimeError('AIOHTTP client is not synchronous, please use async context manager')
    
    @override
    async def __aenter__(self) -> 'Client':
        self._client_session = aiohttp.ClientSession()
        await self._client_session.__aenter__()
        return self
    
    @override
    def __exit__(self, *args: Any) -> None:
        pass
    
    @override
    async def __aexit__(self, *args: Any) -> None:
        await self._client_session.__aexit__(*args)
    
    @override
    def request(self, request: Request) -> Response:
        raise RuntimeError('AIOHTTP client is not synchronous, please use async context manager')
    
    @override
    async def arequest(self, request: Request) -> Response:
        async with self._client_session.request(
            request.method,
            request.url,
            params=request.params,
            data=request.data,
            headers=request.headers,
            proxy=self.proxy,
        ) as response:
            return Response(
                await response.read(),
                response.status,
            )