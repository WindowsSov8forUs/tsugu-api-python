class RoomSubmitFailure(BaseException):
    '''车牌号上传失败'''
    def __init__(self, response: str) -> None:
        '''初始化'''
        self.message = response
        return