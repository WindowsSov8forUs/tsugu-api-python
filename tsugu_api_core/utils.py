'''
`tsugu_api_core.utils` Tsugu API 工具模块
'''

from tsugu_api_core.bandoristation._typing import StationRoom
from tsugu_api_core._typing import (
    _Room,
    ServerId,
    ServerName
)

def string_to_server_code(server: str) -> ServerId:
    if server == 'jp':
        return 0
    elif server == 'en':
        return 1
    elif server == 'tw':
        return 2
    elif server == 'cn':
        return 3
    elif server == 'kr':
        return 4
    elif server == '日服':
        return 0
    elif server == '国际服':
        return 1
    elif server == '台服':
        return 2
    elif server == '国服':
        return 3
    elif server == '韩服':
        return 4
    else:
        raise ValueError('服务器名称不存在')

def int_to_server_short(server: int) -> ServerName:
    if server == 0:
        return 'jp'
    elif server == 1:
        return 'en'
    elif server == 2:
        return 'tw'
    elif server == 3:
        return 'cn'
    elif server == 4:
        return 'kr'
    else:
        raise ValueError('服务器代码不存在')

def int_to_server_full(server: int) -> str:
    if server == 0:
        return '日服'
    elif server == 1:
        return '国际服'
    elif server == 2:
        return '台服'
    elif server == 3:
        return '国服'
    elif server == 4:
        return '韩服'
    else:
        raise ValueError('服务器代码不存在')

def station_room_to_tsugu(station_room: StationRoom) -> _Room:
    room: _Room = {
        'number': station_room['number'],
        'rawMessage': station_room['raw_message'],
        'source': station_room['source_info']['name'],
        'userId': str(station_room['user_info']['user_id']),
        'time': station_room['time'],
        'avatarUrl': station_room['user_info']['avatar'],
        'userName': station_room['user_info']['username'],
    }
    return room

__all__ = [
    'string_to_server_code',
    'int_to_server_short',
    'int_to_server_full',
    'station_room_to_tsugu',
]
