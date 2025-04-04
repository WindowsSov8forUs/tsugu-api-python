from typing import List

from tsugu_api_core import settings
from tsugu_api_core.bandoristation._network import Api
from tsugu_api_core.bandoristation._typing import StationRoom
from tsugu_api_core.bandoristation.exception import (
    RoomQueryFailure,
    RoomSubmitFailure
)

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
        'number': number,
        'user_id': user_id,
        'raw_message': raw_message,
        'source': source,
        'token': token
    }
    
    # 发送请求
    response = (await Api(
        'submit_room_number',
        proxy=settings.backend_proxy
    ).aget(params)).json()
    if response['status'] == 'failure':
        raise RoomSubmitFailure(response['response'])

async def query_room_number() -> List[StationRoom]:
    '''获取房间号

    返回:
        List[StationRoom]: 房间信息列表
    '''
    
    # 发送请求
    response = (await Api(
        'query_room_number',
        proxy=settings.backend_proxy
    ).aget()).json()
    if response['status'] == 'failure':
        raise RoomQueryFailure(response['response'])
    return response['response']
