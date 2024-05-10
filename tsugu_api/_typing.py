'''
`tsugu_api._typing`

定义了一些类型别名
'''

from typing import (
    Union,
    Literal,
    TypeAlias,
    TypedDict,
    NotRequired
)

_Server: TypeAlias = Literal[0, 1, 2, 3, 4]
'''
服务器 ID

值:
    0: 日服
    1: 国际服
    2: 台服
    3: 国服
    4: 韩服
'''

class _Data(TypedDict):
    '''API 单个响应数据'''
    type: Literal['string', 'base64']
    string: str

_Response: TypeAlias = list[_Data]

class _CarData(TypedDict):
    '''车牌数据'''
    number: int
    rawMessage: str
    source: str
    userId: int
    time: int
    avanter: str
    userName: str

_Status: TypeAlias = Literal['success', 'failure']
'''响应状态'''

class _Result(TypedDict):
    '''响应结果'''
    status: _Status
    data: str

class _QueryResult(TypedDict):
    '''`/station/queryAllRoom` 响应结果'''
    status: _Status
    data: Union[str, list[_CarData]]

class _SubmitResult(TypedDict):
    '''`/station/submitRoomNumber` 响应结果'''
    status: _Status
    data: Union[str, list[_CarData]]

class _ServerData(TypedDict):
    '''服务器数据'''
    playerId: int
    bindingStatus: int

class _UserData(TypedDict):
    '''用户数据'''
    _id: NotRequired[str]
    user_id: str
    platform: str
    server_mode: _Server
    default_server: list[_Server]
    car: bool
    server_list: list[_ServerData]

class _UserDataResult(TypedDict):
    '''`get_user_data` 响应结果'''
    status: _Status
    data: Union[str, _UserData]

class _VerifyCode(TypedDict):
    '''验证码'''
    verifyCode: int

class _BindResponse(TypedDict):
    '''绑定响应'''
    status: _Status
    data: Union[str, _VerifyCode]

_Difficulty: TypeAlias = Literal['easy', 'normal', 'hard', 'expert', 'special']
'''难度名'''
