from tsugu_api import settings
from tsugu_api._network import Api
from tsugu_api.exception import RoomSubmitFailure

BANDORI_STATION_URL = 'https://api.bandoristation.com/index.php'

def submit_room_number(number: int, user_id: str, raw_message: str, source: str, token: str) -> None:
    '''上传车牌号

    参数:
        number (int): 车牌号
        user_id (str): 用户 ID
        raw_message (str): 原始消息，用作车牌号注释
        source (str): 车牌来源，即令牌名称
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
    response = Api(
        BANDORI_STATION_URL,
        proxy=settings.backend_proxy,
        params=params
    ).get().json()
    if response['status'] == 'failure':
        raise RoomSubmitFailure(response['response'])
