'''`tsugu_api_async._network`

向 Tsugu 后端发送请求相关模块'''
from typing import Any, Literal, Optional

from ._settings import settings
from .client import _Client, Request, Response
from .exception import BadRequestError, FailedException, HTTPStatusError

BANDORI_STATION_URL = 'https://api.bandoristation.com'

# 向后端发送 API 请求类
class Api:
    '''向后端发送 API 请求类

    参数:
        host (str): 请求的主机地址
        api (str): 请求的 API 路径
        proxy (bool): 是否使用代理服务器
    '''
    host: str
    '''请求的主机地址'''
    api: str
    '''请求的 API 路径'''
    proxy: bool
    '''是否使用代理服务器'''
    # 初始化
    def __init__(
        self,
        host: str,
        api: str,
        proxy: bool
    ) -> None:
        '''初始化'''
        self.host = host.rstrip('/')
        self.api = api
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
            max_retries=settings.max_retries,
        ) as client:
            # 构建一个请求体
            request = Request(
                method,
                self.host + self.api,
                params=params,
                data=data,
                headers=headers
            )
            
            response = await client.arequest(request)
        
        # 处理接收到的响应
        if response.status_code == 200:
            return response
        if response.status_code == 400:
            if self.host == BANDORI_STATION_URL:
                return response
            _response: dict[str, Any] = response.json()
            raise BadRequestError(self.api, _response) from response.exception # type: ignore
        elif response.status_code in (404, 409, 422, 500):
            _response: dict[str, Any] = response.json()
            raise FailedException(self.api, response.status_code, _response) from response.exception # type: ignore
        else:
            raise HTTPStatusError(response.status_code) from response.exception
    
    async def apost(self, data: Optional[dict[str, Any]]=None) -> Response:
        '''异步发送 POST 请求

        参数:
            data (Optional[dict[str, Any]]): 请求的数据

        返回:
            Response: 收到的响应
        '''
        return await self._arequest('post', data=data)
    
    async def aget(self, params: Optional[dict[str, Any]]=None) -> Response:
        '''异步发送 GET 请求

        参数:
            params (Optional[dict[str, Any]]): 请求的参数

        返回:
            _ApiResponse: 收到的响应
        '''
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
        
        # 构建一个请求体
        request = Request(
            method,
            self.host + self.api,
            params=params,
            data=data,
            headers=headers
        )
        
        # 发送请求并获取响应
        with _Client()(
            proxy=settings.proxy if self.proxy and settings.proxy else None,
            timeout=settings.timeout,
            max_retries=settings.max_retries,
        ) as client:
            response = client.request(request)
        
        # 处理接收到的响应
        if response.status_code == 200:
            return response
        if response.status_code == 400:
            if self.host == BANDORI_STATION_URL:
                return response
            _response: dict[str, Any] = response.json()
            raise BadRequestError(self.api, _response) from response.exception # type: ignore
        elif response.status_code in (409, 422, 500):
            _response: dict[str, Any] = response.json()
            raise FailedException(self.api, response.status_code, _response) from response.exception # type: ignore
        else:
            raise HTTPStatusError(response.status_code) from response.exception
    
    def post(self, data: Optional[dict[str, Any]]=None) -> Response:
        '''发送 POST 请求

        参数:
            data (Optional[dict[str, Any]]): 请求的数据

        返回:
            Response: 收到的响应
        '''
        return self._request('post', data=data)
    
    def get(self, params: Optional[dict[str, Any]]=None) -> Response:
        '''发送 GET 请求

        参数:
            params (Optional[dict[str, Any]]): 请求的参数

        返回:
            Response: 收到的响应
        '''
        return self._request('get', params=params)
