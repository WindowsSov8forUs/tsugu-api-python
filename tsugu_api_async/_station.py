from time import time
from typing import Optional

from httpx import Response

from tsugu_api_async import settings
from tsugu_api_async._network import Api
from tsugu_api_async._typing import (
    _QueryResponse,
    _SubmitResponse
)

async def station_submit_room_number(
    number: int,
    raw_message: str,
    platform: str,
    user_id: str,
    user_name: str,
    bandori_station_token: Optional[str] = None
) -> _SubmitResponse:
    '''提交车牌号

    参数:
        number (int): 车牌号
        raw_message (str): 原始消息
        platform (str): 平台
        user_id (str): 用户 ID
        user_name (str): 用户名
        bandori_station_token (Optional[str]): Bandori 车站令牌，不填则使用 Tsugu 后端配置

    返回:
        _SubmitResponse: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/station/submitRoomNumber'
    
    # 构建数据
    data = {
        'number': number,
        'rawMessage': raw_message,
        'platform': platform,
        'user_id': user_id,
        'userName': user_name,
        'time': int(time())
    }
    if bandori_station_token:
        data['bandoriStationToken'] = bandori_station_token
    
    # 发送请求
    resonse = await Api(
        url,
        proxy=settings.backend_proxy
    ).post(data)
    if isinstance(resonse, Response): return resonse.json()
    return await resonse.json()

async def station_query_all_room() -> _QueryResponse:
    '''查询最近车站车牌

    返回:
        _QueryResponse: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/station/queryAllRoom'
    
    # 发送请求
    response = await Api(
        url,
        proxy=settings.backend_proxy
    ).get()
    if isinstance(response, Response): return response.json()
    return await response.json()