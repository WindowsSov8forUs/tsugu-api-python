from typing import Union

from tsugu_api import settings
from tsugu_api._network import Api
from tsugu_api._typing import (
    _Update,
    _Response,
    _ServerId,
    _BindResponse,
    _UpdateResponse,
    _UserDataResponse,
    _VerificationResponse
)

def get_user_data(platform: str, user_id: str) -> Union[_Response, _UserDataResponse]:
    '''获取用户数据

    参数:
        platform (str): 平台名称
        user_id (str): 用户 ID

    返回:
        _UserDataResult: 用户数据
        _Response: 当请求失败时返回的数据
    '''
    
    # 构建 URL
    url = settings.userdata_backend_url + '/user/getUserData'
    
    # 构建数据
    data = {
        'platform': platform,
        'user_id': user_id
    }
    
    # 发送请求
    return Api(
        url,
        proxy=settings.userdata_backend_proxy
    ).post(data).json()

def change_user_data(platform: str, user_id: str, update: _Update) -> Union[_Response, _UpdateResponse]:
    '''修改用户数据

    参数:
        platform (str): 平台名称
        user_id (str): 用户 ID
        update (_Update): 更新数据

    返回:
        _UpdateResult: 更新结果
        _Response: 当请求失败时返回的数据
    '''
    
    # 构建 URL
    url = settings.userdata_backend_url + '/user/changeUserData'
    
    # 构建数据
    data = {
        'platform': platform,
        'user_id': user_id,
        'update': update
    }
    
    # 发送请求
    return Api(
        url,
        proxy=settings.userdata_backend_proxy
    ).post(data).json()

def bind_player_request(
    platform: str,
    user_id: str,
    server: _ServerId,
    bind_type: bool
) -> Union[_Response, _BindResponse]:
    '''绑定玩家请求

    参数:
        platform (str): 平台名称
        user_id (str): 用户 ID
        server (_ServerId): 服务器编号 0 - 日服 1 - 国际服 2 - 台服 3 - 国服 4 - 韩服
        bind_type (bool): 绑定类型， `true` 为绑定， `false` 为解绑

    返回:
        _BindResponse: 请求返回数据
        _Response: 当请求失败时返回的数据
    '''
    
    # 构建 URL
    url = settings.userdata_backend_url + '/user/bindPlayerRequest'
    
    # 构建数据
    data = {
        'platform': platform,
        'user_id': user_id,
        'server': server,
        'bindType': bind_type
    }
    
    # 发送请求
    return Api(
        url,
        proxy=settings.userdata_backend_proxy,
    ).post(data).json()

def bind_player_verification(
    platform: str,
    user_id: str,
    server: _ServerId,
    player_id: int,
    bind_type: bool
) -> Union[_Response, _VerificationResponse]:
    '''绑定玩家验证

    参数:
        platform (str): 平台名称
        user_id (str): 用户 ID
        server (_ServerId): 服务器编号 0 - 日服 1 - 国际服 2 - 台服 3 - 国服 4 - 韩服
        player_id (int): 玩家 ID
        bind_type (bool): 绑定类型， `true` 为绑定， `false` 为解绑

    返回:
        _VerificationResponse: 验证返回数据
        _Response: 当请求失败时返回的数据
    '''
    
    # 构建 URL
    url = settings.userdata_backend_url + '/user/bindPlayerVerification'
    
    # 构建数据
    data = {
        'platform': platform,
        'user_id': user_id,
        'server': server,
        'playerId': player_id,
        'bindType': bind_type
    }
    
    # 发送请求
    return Api(
        url,
        proxy=settings.userdata_backend_proxy
    ).post(data).json()
