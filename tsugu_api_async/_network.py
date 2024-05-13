'''`tsugu_api_async._network`

向 Tsugu 后端发送请求相关模块'''
from json import dumps
from typing import Any, Literal, Optional, cast

from aiohttp import ClientSession
from httpx import Request, Response, AsyncClient, HTTPStatusError

from . import settings
from ._typing import _ApiResponse

# 向后端发送 API 请求类
class Api:
    '''向后端发送 API 请求类

    参数:
        url (str): 请求的 URL 地址
    '''
    url: str
    '''请求的 API 地址'''
    proxy: bool
    '''是否使用代理服务器'''
    # 初始化
    def __init__(
        self,
        url: str,
        proxy: bool
    ) -> None:
        '''初始化'''
        self.url = url
        self.proxy = proxy
        return
    
    # 请求发送
    async def _request(
        self,
        method: Literal['get', 'post'],
        *,
        params: Optional[dict[str, Any]]=None,
        data: Optional[dict[str, Any]]=None
    ) -> _ApiResponse:
        '''请求发送

        参数:
            method (Literal[&#39;get&#39;, &#39;post&#39;]): API 调用方法
            params (Optional[dict[str, Any]]): 请求的参数
            data (Optional[dict[str, Any]]): 请求的数据

        返回:
            Response: 收到的响应
        '''
        # 构建请求头
        if method == 'post':
            headers = {'Content-Type': 'application/json'}
        else:
            headers = None
        
        # 构建代理服务器字典
        if self.proxy:
            proxies = settings._get_proxy()
        else:
            proxies = None
        
        # 发送请求并获取响应
        if settings.client == settings.Client.HTTPX:
            async with AsyncClient(proxies=cast(dict, proxies), timeout=settings.timeout, trust_env=False) as client:
                # 构建一个请求体
                request = Request(
                    method,
                    self.url,
                    params=params,
                    data=cast(dict, dumps(data)) if data is not None else data,
                    headers=headers
                )
                
                response = await client.send(request)
        else:
            async with ClientSession() as session:
                response = await session.request(
                    method,
                    self.url,
                    params=params,
                    data=cast(dict, dumps(data)) if data is not None else data,
                    headers=headers,
                    proxy=settings.proxy if len(settings.proxy) > 0 and self.proxy else None,
                )
        
        # 处理接收到的响应
        if isinstance(response, Response):
            try:
                response.raise_for_status()
            except HTTPStatusError as exception:
                if exception.response.status_code == 400:
                    return response
                else:
                    raise exception
        else:
            if response.status == 400:
                return response
            else:
                response.raise_for_status()
        return response
    
    async def post(self, data: Optional[dict[str, Any]]=None) -> _ApiResponse:
        '''发送 POST 请求

        参数:
            data (Optional[dict[str, Any]]): 请求的数据

        返回:
            _ApiResponse: 收到的响应
        '''
        return await self._request('post', data=data)
    
    async def get(self, params: Optional[dict[str, Any]]=None) -> _ApiResponse:
        '''发送 GET 请求

        参数:
            params (Optional[dict[str, Any]]): 请求的参数

        返回:
            _ApiResponse: 收到的响应
        '''
        return await self._request('get', params=params)
