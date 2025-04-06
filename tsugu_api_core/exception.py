from typing import List
from tsugu_api_core._typing import _FailedResponse, _BadRequestResponse

class TsuguException(Exception):
    '''tsugu_api_core 异常基类'''
    msg: str = ''
    '''从 API 返回参数中获取的错误信息'''
    def __init__(self, msg: str) -> None:
        '''初始化'''
        self.msg = msg
    
    def __str__(self) -> str:
        return self.msg

class HTTPStatusError(TsuguException):
    '''HTTP 状态码错误'''
    status_code: int
    '''HTTP 状态码'''
    def __init__(self, status_code: int) -> None:
        '''初始化'''
        self.status_code = status_code
        super().__init__(f"HTTP status code error: {status_code}, please check your network environment or contact the developer.")
        return

class BadRequestError(TsuguException):
    '''请求的参数错误'''
    api: str
    '''请求的 API'''
    response: _BadRequestResponse
    '''API 返回的响应'''
    def __init__(self, api: str, response: _BadRequestResponse) -> None:
        '''初始化'''
        self.api = api
        self.response = response
        
        error_messages: List[str] = []
        for error in response['error']:
            error_messages.append(
                f"\tGot a wrong value '{str(error['value'])}' for {error['type']} parameter '{error['path']}' in {error['location']}: {error['msg']}."
            )
        
        super().__init__(f"API '{api}' got wrong parameters:\n" + '\n'.join(error_messages))
        
        return

class FailedException(TsuguException):
    '''API 请求失败'''
    api: str
    '''请求的 API'''
    status_code: int
    '''API 返回的状态码'''
    response: _FailedResponse
    '''API 返回的响应'''
    def __init__(self, api: str, status_code: int, response: _FailedResponse) -> None:
        '''初始化'''
        self.api = api
        self.status_code = status_code
        self.response = response
        
        super().__init__(f"API '{api}' failed ({status_code}) : {response['data']}")
        
        return
    
    def json(self) -> _FailedResponse:
        '''返回 API 返回的响应'''
        return self.response
    
    @property
    def data(self) -> str:
        return self.response['data']

class RoomSubmitFailure(TsuguException):
    '''房间号上传失败'''
    def __init__(self, response: str) -> None:
        '''初始化'''
        super().__init__(response)
        return

class RoomQueryFailure(TsuguException):
    '''房间号获取失败'''
    def __init__(self, response: str) -> None:
        '''初始化'''
        super().__init__(response)
        return
