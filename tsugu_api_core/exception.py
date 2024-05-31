from typing import List
from tsugu_api_core._typing import _BadRequestResponse

class TsuguException(Exception):
    '''tsugu_api_core 异常基类'''
    data: str = ''
    '''从 API 返回参数中获取的错误信息'''
    def __init__(self, data: str) -> None:
        '''初始化'''
        self.data = data
    
    def __str__(self) -> str:
        return self.data

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
                f"\tGot a wrong value '{str(error['value'])}' for {error['type']} parameter '{error['path']}' in {error['location']}: {error['msg']}"
            )
        
        super().__init__(f"API {api} got wrong parameters:\n" + '\n'.join(error_messages))
        
        return

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