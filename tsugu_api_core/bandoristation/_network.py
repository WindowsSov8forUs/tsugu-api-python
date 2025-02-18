'''`tsugu_api_core.bandoristation._network`

向车站后端发送请求相关模块'''
from json import dumps
from typing import Any, Literal, Optional, cast

from tsugu_api_core import settings
from tsugu_api_core.exception import HTTPStatusError
from tsugu_api_core.client import _Client, Request, Response

BANDORI_STATION_URL = 'https://api.bandoristation.com/'

# 向后端发送 API 请求类
class Api:
    '''向后端发送 API 请求类

    参数:
        url (str): 请求的 URL 地址
    '''
    function: str
    '''请求的方法名称'''
    proxy: bool
    '''是否使用代理服务器'''
    # 初始化
    def __init__(
        self,
        function: str,
        proxy: bool
    ) -> None:
        '''初始化'''
        self.function = function
        self.proxy = proxy
        return
    
    # 请求发送
    async def _arequest(
        self,
        method: Literal['get', 'post'],
        *,
        params: Optional[dict[str, Any]]=None,
        data: Optional[dict[str, Any]]=None
    ) -> Response:
        '''异步请求发送

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
        
        # 发送请求并获取响应
        async with _Client()(
            proxy=settings.proxy if self.proxy and settings.proxy else None,
            timeout=settings.timeout,
        ) as client:
            # 构建一个请求体
            request = Request(
                method,
                BANDORI_STATION_URL,
                params=params,
                data=cast(dict, dumps(data)) if data is not None else data,
                headers=headers
            )
            
            response = await client.arequest(request)
        
        # 处理接收到的响应
        if response.status_code == 400:
            return response
        else:
            raise HTTPStatusError(response.status_code) from response.exception
    
    async def aget(self, params: Optional[dict[str, Any]]=None) -> Response:
        '''异步发送 GET 请求

        参数:
            params (Optional[dict[str, Any]]): 请求的参数

        返回:
            Response: 收到的响应
        '''
        if params is None:
            params = {
                'function': self.function
            }
        else:
            params['function'] = self.function
        return await self._arequest('get', params=params)

    # 请求发送
    def _request(
        self,
        method: Literal['get', 'post'],
        *,
        params: Optional[dict[str, Any]]=None,
        data: Optional[dict[str, Any]]=None
    ) -> Response:
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
            proxies = settings._get_proxies()
        else:
            proxies = None
        
        # 发送请求并获取响应
        with _Client()(
            proxy=settings.proxy if self.proxy and settings.proxy else None,
            timeout=settings.timeout,
        ) as client:
        # 构建一个请求体
        
            request = Request(
                method,
                BANDORI_STATION_URL,
                params=params,
                data=cast(dict, dumps(data)) if data is not None else data,
                headers=headers
            )
            
            response = client.request(request)
        
        # 处理接收到的响应
        if response.status_code == 400:
            return response
        else:
            raise HTTPStatusError(response.status_code) from response.exception
    
    def get(self, params: Optional[dict[str, Any]]=None) -> Response:
        '''发送 GET 请求

        参数:
            params (Optional[dict[str, Any]]): 请求的参数

        返回:
            Response: 收到的响应
        '''
        if params is None:
            params = {
                'function': self.function
            }
        else:
            params['function'] = self.function
        return self._request('get', params=params)
