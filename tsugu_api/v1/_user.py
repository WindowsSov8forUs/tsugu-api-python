from httpx import HTTPStatusError

from tsugu_api import settings
from tsugu_api._network import Api
from tsugu_api._typing import (
    _Result,
    _Server,
    _BindResponse,
    _UserDataResult
)

def get_user_data(platform: str, user_id: str) -> _UserDataResult:
    '''获取用户数据

    参数:
        platform (str): 平台名称
        user_id (str): 用户 ID

    返回:
        _UserDataResult: 用户数据
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
        proxy=settings.userdata_backend_proxy,
        data=data
    ).post().json()

def bind_player_request(
    platform: str,
    user_id: str,
    server: _Server,
    bind_type: bool
) -> _BindResponse:
    '''绑定玩家请求

    参数:
        platform (str): 平台名称
        user_id (str): 用户 ID
        server (_Server): 服务器编号 0 - 日服 1 - 国际服 2 - 台服 3 - 国服 4 - 韩服
        bind_type (bool): 绑定类型， `true` 为绑定， `false` 为解绑

    返回:
        _BindResponse: 请求返回数据
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
    try:
        return Api(
            url,
            proxy=settings.userdata_backend_proxy,
            data=data
        ).post().json()
    except HTTPStatusError as exception:
        if exception.response.status_code == 400:
            return exception.response.json()
        else:
            raise exception

def bind_player_verification(
    platform: str,
    user_id: str,
    player_id: int,
    server: _Server,
    bind_type: bool
) -> _Result:
    '''绑定玩家验证

    参数:
        platform (str): 平台名称
        user_id (str): 用户 ID
        player_id (int): 玩家 ID
        server (_Server): 服务器编号 0 - 日服 1 - 国际服 2 - 台服 3 - 国服 4 - 韩服
        bind_type (bool): 绑定类型， `true` 为绑定， `false` 为解绑

    返回:
        _BindResponse: 请求返回数据
    '''
    
    # 构建 URL
    url = settings.userdata_backend_url + '/user/bindPlayerVerification'
    
    # 构建数据
    data = {
        'platform': platform,
        'user_id': user_id,
        'playerId': player_id,
        'server': server,
        'bindType': bind_type
    }
    
    # 发送请求
    try:
        return Api(
            url,
            proxy=settings.userdata_backend_proxy,
            data=data
        ).post().json()
    except HTTPStatusError as exception:
        if exception.response.status_code == 400:
            return exception.response.json()
        else:
            raise exception

def set_car_forwarding(platform: str, user_id: str, status: bool) -> _Result:
    '''设置车牌号转发

    参数:
        platform (str): 平台名称
        user_id (str): 用户 ID
        status (bool): 是否允许转发车牌号， `true` 为允许， `false` 为不允许

    返回:
        _Result: 请求返回数据
    '''
    
    # 构建 URL
    url = settings.userdata_backend_url + '/user/changeUserData/setCarForwarding'
    
    # 构建数据
    data = {
        'platform': platform,
        'user_id': user_id,
        'status': status
    }
    
    # 发送请求
    try:
        return Api(
            url,
            proxy=settings.userdata_backend_proxy,
            data=data
        ).post().json()
    except HTTPStatusError as exception:
        if exception.response.status_code == 400:
            return exception.response.json()
        else:
            raise exception

def set_default_server(platform: str, user_id: str, text: str) -> _Result:
    '''设置默认服务器

    参数:
        platform (str): 平台名称
        user_id (str): 用户 ID
        text (str): 要设置的默认服务器列表，注意不要使用纯数字

    返回:
        _Result: 请求返回数据
    '''
    
    # 构建 URL
    url = settings.userdata_backend_url + '/user/changeUserData/setDefaultServer'
    
    # 构建数据
    data = {
        'platform': platform,
        'user_id': user_id,
        'text': text
    }
    
    # 发送请求
    try:
        return Api(
            url,
            proxy=settings.userdata_backend_proxy,
            data=data
        ).post().json()
    except HTTPStatusError as exception:
        if exception.response.status_code == 400:
            return exception.response.json()
        else:
            raise exception

def set_server_mode(platform: str, user_id: str, text: str) -> _Result:
    '''设置主服务器

    参数:
        platform (str): 平台名称
        user_id (str): 用户 ID
        text (str): 要设置的主服务器，注意不要使用纯数字

    返回:
        _Result: 请求返回数据
    '''
    
    # 构建 URL
    url = settings.userdata_backend_url + '/user/changeUserData/setServerMode'
    
    # 构建数据
    data = {
        'platform': platform,
        'user_id': user_id,
        'text': text
    }
    
    # 发送请求
    try:
        return Api(
            url,
            proxy=settings.userdata_backend_proxy,
            data=data
        ).post().json()
    except HTTPStatusError as exception:
        if exception.response.status_code == 400:
            return exception.response.json()
        else:
            raise exception
