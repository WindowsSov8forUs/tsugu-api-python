'''
`tsugu_api_core.bandoristation._typing`

定义了一些类型别名
'''

from typing import Any, TypedDict

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

class StationRoom(TypedDict):
    '''车站房间数据'''
    number: int
    raw_message: str
    source_info: _SourceInfo
    time: int
    type: str
    user_info: _UserInfo
