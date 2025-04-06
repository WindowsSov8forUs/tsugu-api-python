'''内置的 HTTPX 客户端适配'''

import time
import asyncio
from json import dumps
from typing import Any, cast
from typing_extensions import override

from ._client import Client as _Client
from ._client import Request, Response

try:
    import httpx
except ModuleNotFoundError as exception:
    raise ImportError(
        'module \'httpx\' is not installed, please install it by running \'pip install httpx\''
    ) from exception

__HTTPX_ABOVE_0_28_0__ : bool = tuple(httpx.__version__.split('.')) >= ('0', '28', '0')

class Client(_Client):
    '''HTTPX 客户端适配'''
    _client: httpx.Client
    '''HTTPX 客户端'''
    _async_client: httpx.AsyncClient
    '''异步 HTTPX 客户端'''

    @override
    def __enter__(self) -> 'Client':
        if __HTTPX_ABOVE_0_28_0__:
            self._client = httpx.Client(
                proxy=self.proxy,
                timeout=self.timeout,
                trust_env=False,
            )
        else:
            proxies = {
                'http://': self.proxy,
                'https://': self.proxy,
            } if self.proxy else None
            
            self._client = httpx.Client(
                proxies=cast(dict, proxies),
                timeout=self.timeout,
                trust_env=False,
            )
        
        self._client.__enter__()
        return self
    
    @override
    async def __aenter__(self) -> 'Client':
        if __HTTPX_ABOVE_0_28_0__:
            self._async_client = httpx.AsyncClient(
                proxy=self.proxy,
                timeout=self.timeout,
                trust_env=False,
            )
        else:
            proxies = {
                'http://': self.proxy,
                'https://': self.proxy,
            } if self.proxy else None
            
            self._async_client = httpx.AsyncClient(
                proxies=cast(dict, proxies),
                timeout=self.timeout,
                trust_env=False,
            )
        
        await self._async_client.__aenter__()
        return self
    
    @override
    def __exit__(self, *args: Any) -> None:
        self._client.__exit__(*args)
    
    @override
    async def __aexit__(self, *args: Any) -> None:
        await self._async_client.__aexit__(*args)
    
    @override
    def request(self, request: Request) -> Response:
        if __HTTPX_ABOVE_0_28_0__:
            _request = httpx.Request(
                request.method,
                request.url,
                params=request.params,
                content=cast(dict, dumps(request.data)) if request.data is not None else request.data,
                headers=request.headers,
            )
        else:
            _request = httpx.Request(
                request.method,
                request.url,
                params=request.params,
                data=cast(dict, dumps(request.data)) if request.data is not None else request.data,
                headers=request.headers,
            )
        
        retries = 0
        while True:
            try:
                _response = self._client.send(_request)
                break
            except Exception as exception:
                if retries >= self.max_retries:
                    raise exception
                retries += 1
                time.sleep(0.5)
        
        # 处理响应
        try:
            _response.raise_for_status()
            return Response(
                _response.content,
                _response.status_code,
            )
        except httpx.HTTPStatusError as exception:
            return Response(
                exception.response.content,
                exception.response.status_code,
                exception,
            )
    
    @override
    async def arequest(self, request: Request) -> Response:
        if __HTTPX_ABOVE_0_28_0__:
            _request = httpx.Request(
                request.method,
                request.url,
                params=request.params,
                content=cast(dict, dumps(request.data)) if request.data is not None else request.data,
                headers=request.headers,
            )
        else:
            _request = httpx.Request(
                request.method,
                request.url,
                params=request.params,
                data=cast(dict, dumps(request.data)) if request.data is not None else request.data,
                headers=request.headers,
            )
        
        retries = 0
        while True:
            try:
                _response = await self._async_client.send(_request)
                break
            except Exception as exception:
                if retries >= self.max_retries:
                    raise exception
                retries += 1
                await asyncio.sleep(0.5)
        
        # 处理响应
        try:
            _response.raise_for_status()
            return Response(
                _response.content,
                _response.status_code,
            )
        except httpx.HTTPStatusError as exception:
            return Response(
                exception.response.content,
                exception.response.status_code,
                exception,
            )