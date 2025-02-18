'''
`tsugu_api_core._typing`

定义了一些类型别名
'''

from typing import (
    Any,
    Dict,
    List,
    Union,
    Literal,
    TypeAlias,
    TypedDict,
    TypeGuard,
)
from typing_extensions import NotRequired

ServerId: TypeAlias = Literal[0, 1, 2, 3, 4]
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
ServerName: TypeAlias = Literal['jp', 'en', 'tw', 'cn', 'kr']
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
Server: TypeAlias = Union[ServerId, ServerName]
'''服务器'''
SERVER = (0, 1, 2, 3, 4, 'jp', 'en', 'tw', 'cn', 'kr')

def is_server(server: Any) -> TypeGuard[Server]:
    return server in SERVER

def is_server_list(server_list: List[Any]) -> TypeGuard[List[Server]]:
    for server in server_list:
        if not is_server(server):
            return False
    return True

class _Data(TypedDict):
    '''API 单个响应数据'''
    type: Literal['string', 'base64']
    string: str

_Response: TypeAlias = List[_Data]

class _Error(TypedDict):
    '''错误信息'''
    type: str
    '''错误类型'''
    location: Literal['body', 'cookies', 'headers', 'params', 'query']
    '''参数位置'''
    msg: str
    '''错误信息'''
    path: str
    '''参数名称'''
    value: Any
    '''参数值'''

class _BadRequestResponse(TypedDict):
    '''参数错误响应信息'''
    status: Literal['failed']
    data: str
    error: List[_Error]

class _FailedResponse(TypedDict):
    '''失败响应信息'''
    status: Literal['failed']
    data: str

_Status: TypeAlias = Literal['success', 'failed']
'''响应状态'''

FuzzySearchResult: TypeAlias = Dict[str, List[Union[str, int]]]

class _FuzzySearchResponse(TypedDict):
    '''`/fuzzySearch` 响应结果'''
    status: _Status
    data: FuzzySearchResult

_DifficultyId: TypeAlias = Literal[0, 1, 2, 3, 4]
'''难度 ID'''

class _UserPlayerInList(TypedDict):
    playerId: int
    server: ServerId

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
    player: NotRequired[_UserPlayerInList]
    avatarUrl: NotRequired[str]
    userName: NotRequired[str]

class _QueryResponse(TypedDict):
    '''`/station/queryAllRoom` 响应结果'''
    status: _Status
    data: List[_Room]

class _TsuguUserServer(TypedDict):
    '''服务器数据'''
    playerId: int
    bindingStatus: Literal[0, 1, 2]
    verifyCode: NotRequired[int]

class _TsuguUser(TypedDict):
    '''用户数据'''
    userId: str
    '''用户 ID'''
    platform: str
    '''平台'''
    mainServer: ServerId
    '''主服务器'''
    displayedServerList: List[ServerId]
    '''显示的服务器列表'''
    shareRoomNumber: bool
    '''是否分享房间号'''
    userPlayerIndex: int
    '''用户账号索引'''
    userPlayerList: List[_UserPlayerInList]
    '''用户账号列表'''

class _GetUserDataResponse(TypedDict):
    '''`/user/getUserData` 响应结果'''
    status: _Status
    data: _TsuguUser

class PartialTsuguUser(TypedDict):
    '''更新数据'''
    userId: NotRequired[str]
    '''用户 ID'''
    platform: NotRequired[str]
    '''平台'''
    mainServer: NotRequired[ServerId]
    '''主服务器'''
    displayedServerList: NotRequired[List[ServerId]]
    '''显示的服务器列表'''
    shareRoomNumber: NotRequired[bool]
    '''是否分享房间号'''
    userPlayerIndex: NotRequired[int]
    '''用户账号索引'''
    userPlayerList: NotRequired[List[_UserPlayerInList]]
    '''用户账号列表'''

class _ChangeUserDataResponse(TypedDict):
    '''`/user/changeUserData` 响应结果'''
    status: _Status

class _VerifyCode(TypedDict):
    '''验证码'''
    verifyCode: int

_BindingAction: TypeAlias = Literal['bind', 'unbind']
'''绑定操作'''

class _BindPlayerRequestResponse(TypedDict):
    '''`/user/bindPlayerRequest` 绑定响应'''
    status: _Status
    data: _VerifyCode

class _BindPlayerVerificationResponse(TypedDict):
    '''`/user/bindPlayerVerification` 响应结果'''
    status: _Status
    data: str
