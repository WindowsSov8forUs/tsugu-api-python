from tsugu_api_core import settings
from tsugu_api_core._network import Api
from tsugu_api_core._typing import (
    ServerId,
    _BindingAction,
    PartialTsuguUser,
    _GetUserDataResponse,
    _ChangeUserDataResponse,
    _BindPlayerRequestResponse,
    _BindPlayerVerificationResponse
)

async def get_user_data(platform: str, user_id: str) -> _GetUserDataResponse:
    '''获取用户数据

    参数:
        platform (str): 平台名称
        user_id (str): 用户 ID

    返回:
        _GetUserDataResponse: API 返回响应
    '''
    
    # 构建数据
    data = {
        'platform': platform,
        'userId': user_id
    }
    
    # 发送请求
    return (await Api(
        settings.userdata_backend_url,
        '/user/getUserData',
        proxy=settings.userdata_backend_proxy
    ).apost(data)).json()

async def change_user_data(platform: str, user_id: str, update: PartialTsuguUser) -> _ChangeUserDataResponse:
    '''修改用户数据

    参数:
        platform (str): 平台名称
        user_id (str): 用户 ID
        update (_PartialTsuguUser): 更新数据

    返回:
        _ChangeUserDataResponse: API 返回响应
    '''
    
    # 构建数据
    data = {
        'platform': platform,
        'userId': user_id,
        'update': update
    }
    
    # 发送请求
    return (await Api(
        settings.userdata_backend_url,
        '/user/changeUserData',
        proxy=settings.userdata_backend_proxy
    ).apost(data)).json()

async def bind_player_request(
    platform: str,
    user_id: str
) -> _BindPlayerRequestResponse:
    '''绑定玩家请求

    参数:
        platform (str): 平台名称
        user_id (str): 用户 ID

    返回:
        _BindPlayerRequestResponse: 请求返回数据
    '''
    
    # 构建数据
    data = {
        'platform': platform,
        'userId': user_id
    }
    
    # 发送请求
    return (await Api(
        settings.userdata_backend_url,
        '/user/bindPlayerRequest',
        proxy=settings.userdata_backend_proxy,
    ).apost(data)).json()

async def bind_player_verification(
    platform: str,
    user_id: str,
    server: ServerId,
    player_id: int,
    binding_action: _BindingAction
) -> _BindPlayerVerificationResponse:
    '''绑定玩家验证

    参数:
        platform (str): 平台名称
        user_id (str): 用户 ID
        server (_ServerId): 服务器编号 0 - 日服 1 - 国际服 2 - 台服 3 - 国服 4 - 韩服
        player_id (int): 玩家 ID
        binding_action (_BindingAction): 绑定操作

    返回:
        _BindPlayerVerificationResponse: 验证返回数据
    '''
    
    # 构建数据
    data = {
        'platform': platform,
        'userId': user_id,
        'server': server,
        'playerId': player_id,
        'bindingAction': binding_action
    }
    
    # 发送请求
    return (await Api(
        settings.userdata_backend_url,
        '/user/bindPlayerVerification',
        proxy=settings.userdata_backend_proxy
    ).apost(data)).json()
