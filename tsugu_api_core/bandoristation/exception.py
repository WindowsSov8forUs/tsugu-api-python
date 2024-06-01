from tsugu_api_core.exception import TsuguException

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
