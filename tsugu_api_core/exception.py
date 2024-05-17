class TsuguException(Exception):
    '''tsugu_api_core 异常基类'''
    data: str = ''
    '''从 API 返回参数中获取的错误信息'''
    def __init__(self, data: str) -> None:
        '''初始化'''
        self.data = data
    
    def __str__(self) -> str:
        return self.data

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