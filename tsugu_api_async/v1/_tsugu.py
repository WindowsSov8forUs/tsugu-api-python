from time import time
from typing import Optional

from tsugu_api_async import settings
from tsugu_api_async._network import Api
from tsugu_api_async._typing import (
    _Server,
    _CarData,
    _Response,
    _Difficulty,
    _QueryResult,
    _SubmitResult
)

async def get_card_illustration(card_id: int) -> _Response:
    '''获取卡面

    参数:
        platform (str): 平台名称
        user_id (str): 用户 ID

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/getCardIllustration'
    
    # 构建数据
    data = {
        'cardId': card_id
    }
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy,
            data=data
        ).post()
    ).json()

async def gacha_simulate(server_mode: _Server, gacha_id: Optional[int] = None) -> _Response:
    '''模拟抽卡

    参数:
        server_mode (_Server): 服务器模式
        gacha_id (int): 卡池 ID

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/gachaSimulate'
    
    # 构建数据
    data = {
        'server_mode': server_mode,
        'compress': settings.compress
    }
    if gacha_id:
        data['gachaId'] = gacha_id
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy,
            data=data
        ).post()
    ).json()

async def search_player(player_id: int, server: _Server) -> _Response:
    '''查询玩家状态

    参数:
        player_id (int): 玩家 ID
        server (_Server): 服务器

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/searchPlayer'
    
    # 构建数据
    data = {
        'playerId': player_id,
        'server': server,
        'useEasyBG': settings.use_easy_bg,
        'compress': settings.compress
    }
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy,
            data=data
        ).post()
    ).json()

async def search_gacha(default_servers: list[_Server], gacha_id: int) -> _Response:
    '''查询卡池

    参数:
        default_servers (list[_Server]): 默认服务器
        gacha_id (int): 卡池 ID

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/searchGacha'
    
    # 构建数据
    data = {
        'default_servers': default_servers,
        'gachaId': gacha_id,
        'useEasyBG': settings.use_easy_bg,
        'compress': settings.compress
    }
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy,
            data=data
        ).post()
    ).json()

async def search_event(default_servers: list[_Server], text: str) -> _Response:
    '''查询活动

    参数:
        default_servers (list[_Server]): 默认服务器
        text (str): 查询参数

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/searchEvent'
    
    # 构建数据
    data = {
        'default_servers': default_servers,
        'text': text,
        'useEasyBG': settings.use_easy_bg,
        'compress': settings.compress
    }
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy,
            data=data
        ).post()
    ).json()

async def search_song(default_servers: list[_Server], text: str) -> _Response:
    '''查询歌曲

    参数:
        default_servers (list[_Server]): 默认服务器
        text (str): 查询参数

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/searchSong'
    
    # 构建数据
    data = {
        'default_servers': default_servers,
        'text': text,
        'useEasyBG': settings.use_easy_bg,
        'compress': settings.compress
    }
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy,
            data=data
        ).post()
    ).json()

async def song_meta(default_servers: list[_Server], server: _Server) -> _Response:
    '''查询歌曲分数表

    参数:
        default_servers (list[_Server]): 默认服务器
        server (_Server): 主服务器

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/songMeta'
    
    # 构建数据
    data = {
        'default_servers': default_servers,
        'server': server,
        'compress': settings.compress
    }
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy,
            data=data
        ).post()
    ).json()

async def search_character(default_servers: list[_Server], text: str) -> _Response:
    '''查询角色

    参数:
        default_servers (list[_Server]): 默认服务器
        text (str): 查询参数

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/searchCharacter'
    
    # 构建数据
    data = {
        'default_servers': default_servers,
        'text': text,
        'compress': settings.compress
    }
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy,
            data=data
        ).post()
    ).json()

async def song_chart(default_servers: list[_Server], song_id: int, difficulty_text: _Difficulty) -> _Response:
    '''查询歌曲谱面

    参数:
        default_servers (list[_Server]): 默认服务器
        song_id (int): 歌曲 ID
        difficulty_text (_Difficulty): 谱面难度

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/songChart'
    
    # 构建数据
    data = {
        'default_servers': default_servers,
        'songId': song_id,
        'difficultyText': difficulty_text,
        'compress': settings.compress
    }
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy,
            data=data
        ).post()
    ).json()

async def ycx_all(server: _Server, event_id: Optional[int] = None) -> _Response:
    '''查询全挡位预测线

    参数:
        server (_Server): 服务器
        event_id (int): 活动 ID

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/ycxAll'
    
    # 构建数据
    data = {
        'server': server,
        'compress': settings.compress
    }
    if event_id:
        data['eventId'] = event_id
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy,
            data=data
        ).post()
    ).json()

async def ycx(server: _Server, tier: int, event_id: Optional[int] = None) -> _Response:
    '''查询排行榜预测线

    参数:
        server (_Server): 服务器
        tier (int): 排行榜挡位
        event_id (int): 活动 ID

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/ycx'
    
    # 构建数据
    data = {
        'server': server,
        'tier': tier,
        'compress': settings.compress
    }
    if event_id:
        data['eventId'] = event_id
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy,
            data=data
        ).post()
    ).json()

async def lsycx(server: _Server, tier: int, event_id: Optional[int] = None) -> _Response:
    '''查询历史排行榜预测线

    参数:
        server (_Server): 服务器
        tier (int): 排行榜挡位
        event_id (int): 活动 ID

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/lsycx'
    
    # 构建数据
    data = {
        'server': server,
        'tier': tier,
        'compress': settings.compress
    }
    if event_id:
        data['eventId'] = event_id
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy,
            data=data
        ).post()
    ).json()

async def room_list(room_list: list[_CarData]) -> _Response:
    '''绘制车牌绘图

    参数:
        room_list (list[_CarData]): 车牌信息列表

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/roomList'
    
    # 构建数据
    data = {
        'roomList': room_list,
        'compress': settings.compress
    }
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy,
            data=data
        ).post()
    ).json()

async def search_card(default_servers: list[_Server], text: str) -> _Response:
    '''查询卡片

    参数:
        default_servers (list[_Server]): 默认服务器
        text (str): 查询参数

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/searchCard'
    
    # 构建数据
    data = {
        'default_servers': default_servers,
        'text': text,
        'useEasyBG': settings.use_easy_bg,
        'compress': settings.compress
    }
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy,
            data=data
        ).post()
    ).json()

async def station_query_all_room() -> _QueryResult:
    '''查询最近车站车牌

    返回:
        _QueryResult: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/station/queryAllRoom'
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy
        ).get()
    ).json()

async def station_submit_room_number(
    number: int,
    raw_message: str,
    platform: str,
    user_id: str,
    user_name: str
) -> _SubmitResult:
    '''提交车牌号

    参数:
        number (int): 车牌号
        raw_message (str): 原始消息
        platform (str): 平台
        user_id (str): 用户 ID
        user_name (str): 用户名

    返回:
        _SubmitResult: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/station/submitRoomNumber'
    
    # 构建数据
    data = {
        'number': number,
        'raw_message': raw_message,
        'platform': platform,
        'user_id': user_id,
        'user_name': user_name,
        'time': int(time())
    }
    
    # 发送请求
    return await (
            await Api(
            url,
            proxy=settings.backend_proxy,
            data=data
        ).post()
    ).json()