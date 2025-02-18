'''HTTP 客户端类型基类'''

from json import loads
from abc import ABC, abstractmethod
from typing import Any, Dict, Self, Optional

class Request:
    '''HTTP 请求类'''
    
    def __init__(
        self,
        method: str,
        url: str,
        *,
        headers: Optional[Dict[str, str]],
        params: Optional[Dict[str, Any]],
        data: Optional[Dict[str, Any]],
    ) -> None:
        self.method = method
        '''请求方法'''
        self.url = url
        '''请求 URL'''
        self.headers = headers
        '''请求头'''
        self.params = params
        '''请求参数'''
        self.data = data
        '''请求数据'''

class Response:
    '''HTTP 响应类'''
    
    def __init__(self, content: bytes, status_code: int, exception: Optional[Exception]=None) -> None:
        self.content = content
        '''响应内容'''
        self.status_code = status_code
        '''状态码'''
        self.exception = exception
        '''异常'''
    
    def json(self, **kwargs: Any) -> Any:
        '''解析 JSON 响应内容'''
        return loads(self.content, **kwargs)

class Client(ABC):
    '''HTTP 客户端类型基类'''
    
    def __init__(self, proxy: Optional[str], timeout: int) -> None:
        self.proxy = proxy
        '''代理服务器地址'''
        self.timeout = timeout
        '''超时时间'''
    
    @abstractmethod
    def __enter__(self) -> Self:
        raise NotImplementedError
    
    @abstractmethod
    async def __aenter__(self) -> Self:
        raise NotImplementedError
    
    @abstractmethod
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        raise NotImplementedError
    
    @abstractmethod
    async def __aexit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def request(self, request: Request) -> Response:
        '''发送请求并获取响应'''
        raise NotImplementedError
    
    @abstractmethod
    async def arequest(self, request: Request) -> Response:
        '''异步发送请求并获取响应'''
        raise NotImplementedError