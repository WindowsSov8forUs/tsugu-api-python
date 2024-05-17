'''
`tsugu_api_core._typing`

定义了一些类型别名
'''

from typing import (
    Any,
    List,
    Union,
    Literal,
    TypeAlias,
    TypedDict
)
from typing_extensions import NotRequired

from httpx import Response
from aiohttp import ClientResponse

_ApiResponse: TypeAlias = Union[Response, ClientResponse]

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
SERVER_ID = (0, 1, 2, 3, 4)
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
SERVER_NAME = ('jp', 'en', 'tw', 'cn', 'kr')
_Server: TypeAlias = Union[_ServerId, _ServerName]
'''服务器'''
SERVER = (0, 1, 2, 3, 4, 'jp', 'en', 'tw', 'cn', 'kr')

def is_server(server: Any) -> bool:
    return server in SERVER

def is_server_list(server_list: List[Any]) -> bool:
    for server in server_list:
        if not is_server(server):
            return False
    return True

class _Data(TypedDict):
    '''API 单个响应数据'''
    type: Literal['string', 'base64']
    string: str

_Response: TypeAlias = List[_Data]

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
    player: NotRequired[_Player]
    avanter: NotRequired[str]
    userName: NotRequired[str]

class _QueryResponse(TypedDict):
    '''`/station/queryAllRoom` 响应结果'''
    status: _Status
    data: Union[str, List[_Room]]

class _TsuguUserServer(TypedDict):
    '''服务器数据'''
    playerId: int
    bindingStatus: Literal[0, 1, 2]
    verifyCode: NotRequired[int]

class _TsuguUser(TypedDict):
    '''用户数据'''
    user_id: str
    platform: str
    server_mode: _ServerId
    default_server: List[_ServerId]
    car: bool
    server_list: List[_TsuguUserServer]

class _GetUserDataResponse(TypedDict):
    '''`/user/getUserData` 响应结果'''
    status: _Status
    data: Union[str, _TsuguUser]

class _Update(TypedDict):
    '''更新数据'''
    user_id: NotRequired[str]
    platform: NotRequired[str]
    server_mode: NotRequired[_ServerId]
    default_server: NotRequired[List[_ServerId]]
    car: NotRequired[bool]
    server_list: NotRequired[List[_TsuguUserServer]]

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
