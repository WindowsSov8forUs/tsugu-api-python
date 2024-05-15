class RoomSubmitFailure(BaseException):
    '''房间号上传失败'''
    def __init__(self, response: str) -> None:
        '''初始化'''
        self.message = response
        return

class RoomQueryFailure(BaseException):
    '''房间号获取失败'''
    def __init__(self, response: str) -> None:
        '''初始化'''
        self.message = response
        return