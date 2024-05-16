class RoomSubmitFailure(Exception):
    '''房间号上传失败'''
    def __init__(self, response: str) -> None:
        '''初始化'''
        self.message = response
        return

class RoomQueryFailure(Exception):
    '''房间号获取失败'''
    def __init__(self, response: str) -> None:
        '''初始化'''
        self.message = response
        return