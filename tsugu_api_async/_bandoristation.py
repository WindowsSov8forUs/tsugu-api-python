from typing import List

from httpx import Response

from tsugu_api_core import settings
from tsugu_api_core._network import Api
from tsugu_api_core._typing import _StationRoom
from tsugu_api_core.exception import RoomQueryFailure, RoomSubmitFailure

BANDORI_STATION_URL = 'https://api.bandoristation.com/index.php'

async def submit_room_number(number: int, user_id: str, raw_message: str, source: str, token: str) -> None:
    '''上传房间号

    参数:
        number (int): 房间号
        user_id (str): 用户 ID
        raw_message (str): 原始消息，用作房间号注释
        source (str): 房间来源，即令牌名称
        token (str): 上传用的车站令牌
    '''
    
    # 构建参数
    params = {
        'function': 'submit_room_number',
        'number': number,
        'user_id': user_id,
        'raw_message': raw_message,
        'source': source,
        'token': token
    }
    
    # 发送请求
    response = await Api(
            BANDORI_STATION_URL,
            proxy=settings.backend_proxy
    ).aget(params)
    if isinstance(response, Response): response = response.json()
    else: response = await response.json()
    if response['status'] == 'failure':
        raise RoomSubmitFailure(response['response'])

async def query_room_number() -> List[_StationRoom]:
    '''获取房间号

    返回:
        List[_StationRoom]: 房间信息列表
    '''
    
    # 构建参数
    params = {
        'function': 'query_room_number'
    }
    
    # 发送请求
    response = await Api(
        BANDORI_STATION_URL,
        proxy=settings.backend_proxy
    ).aget(params)
    if isinstance(response, Response): response = response.json()
    else: response = await response.json()
    if response['status'] == 'failure':
        raise RoomQueryFailure(response['response'])
    return response['response']
