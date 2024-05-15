'''
`tsugu_api._typing`

定义了一些类型别名
'''

from typing import (
    Any,
    Union,
    Literal,
    TypeAlias,
    TypedDict
)
from typing_extensions import NotRequired

_ServerId: TypeAlias = Literal[0, 1, 2, 3, 4]
'''
服务器 ID

值:
    0: 日服
    1: 国际服
    2: 台服
    3: 国服
    4: 韩服
'''
_ServerName: TypeAlias = Literal['jp', 'en', 'tw', 'cn', 'kr']
'''
服务器名

值:
    'jp': 日服
    'en': 国际服
    'tw': 台服
    'cn': 国服
    'kr': 韩服
'''
_Server: TypeAlias = Union[_ServerId, _ServerName]
'''服务器'''

class _Data(TypedDict):
    '''API 单个响应数据'''
    type: Literal['string', 'base64']
    string: str

_Response: TypeAlias = list[_Data]

_DifficultyText: TypeAlias = Literal['easy', 'normal', 'hard', 'expert', 'special']
'''难度名'''

class _Player(TypedDict):
    id: int
    server: _Server

_Status: TypeAlias = Literal['success', 'failed']
'''响应状态'''

class _SubmitResponse(TypedDict):
    '''`/station/submitRoomNumber` 响应结果'''
    status: _Status
    data: str

class _Room(TypedDict):
    '''房间数据'''
    number: int
    rawMessage: str
    source: str
    userId: str
    time: int
    player: _Player
    avanter: NotRequired[str]
    userName: NotRequired[str]

class _QueryResponse(TypedDict):
    '''`/station/queryAllRoom` 响应结果'''
    status: _Status
    data: Union[str, list[_Room]]

class _TsuguUserServer(TypedDict):
    '''服务器数据'''
    playerId: int
    bindingStatus: Literal[0, 1, 2]
    verifyCode: NotRequired[int]

class _TsuguUser(TypedDict):
    '''用户数据'''
    user_id: str
    platform: str
    server_mode: _Server
    default_server: list[_Server]
    car: bool
    server_list: list[_TsuguUserServer]

class _GetUserDataResponse(TypedDict):
    '''`/user/getUserData` 响应结果'''
    status: _Status
    data: Union[str, _TsuguUser]

class _Update(TypedDict):
    '''更新数据'''
    user_id: NotRequired[str]
    platform: NotRequired[str]
    server_mode: NotRequired[_ServerId]
    default_server: NotRequired[list[_ServerId]]
    car: NotRequired[bool]
    server_list: NotRequired[list[_TsuguUserServer]]

class _ChangeUserDataResponse(TypedDict):
    '''`/user/changeUserData` 响应结果'''
    status: _Status
    data: NotRequired[str]

class _VerifyCode(TypedDict):
    '''验证码'''
    verifyCode: int

class _BindPlayerRequestResponse(TypedDict):
    '''`/user/bindPlayerRequest` 绑定响应'''
    status: _Status
    data: Union[str, _VerifyCode]

class _BindPlayerVerificationResponse(TypedDict):
    '''`/user/bindPlayerVerification` 响应结果'''
    status: _Status
    data: str

class _SourceInfo(TypedDict):
    '''来源信息'''
    name: str
    type: str

class _UserInfo(TypedDict):
    '''用户信息'''
    avatar: str
    bandori_player_brief_info: Any
    role: int
    type: str
    user_id: int
    username: str

class _StationRoom(TypedDict):
    '''车站房间数据'''
    number: int
    raw_message: str
    source_info: _SourceInfo
    time: int
    type: str
    user_info: _UserInfo
