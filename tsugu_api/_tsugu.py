from typing import List, Optional, Sequence

from tsugu_api_core import settings
from tsugu_api_core._network import Api
from tsugu_api_core._typing import (
    _Room,
    _Server,
    _Response,
    _DifficultyText
)

def event_stage(server: _Server, event_id: Optional[int] = None, meta: bool = False) -> _Response:
    '''查询团队 LIVE 佳节活动舞台数据

    参数:
        server (_Server): 服务器
        event_id (int): 活动 ID
        meta (bool): 是否携带歌曲分数表

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/eventStage'
    
    # 构建数据
    data = {
        'server': server,
        'meta': meta,
        'compress': settings.compress
    }
    if event_id:
        data['eventId'] = event_id
    
    # 发送请求
    return Api(
        url,
        proxy=settings.backend_proxy
    ).post(data).json()

def gacha_simulate(server_mode: _Server, times: Optional[int] = None, gacha_id: Optional[int] = None) -> _Response:
    '''模拟抽卡

    参数:
        server_mode (_Server): 服务器模式
        times (int): 抽卡次数
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
    if times:
        data['times'] = times
    if gacha_id:
        data['gachaId'] = gacha_id
    
    # 发送请求
    return Api(
        url,
        proxy=settings.backend_proxy
    ).post(data).json()

def get_card_illustration(card_id: int) -> _Response:
    '''获取卡面

    参数:
        card_id (int): 卡片 ID

    返回:
        _Response: 响应信息
    '''
    
    # 构建 URL
    url = settings.backend_url + '/getCardIllustration'
    
    # 构建数据
    data = {
        'cardId': str(card_id)
    }
    
    # 发送请求
    return Api(
        url,
        proxy=settings.backend_proxy
    ).post(data).json()

def lsycx(server: _Server, tier: int, event_id: Optional[int] = None) -> _Response:
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
    return Api(
        url,
        proxy=settings.backend_proxy
    ).post(data).json()

def room_list(room_list: List[_Room]) -> _Response:
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
    return Api(
        url,
        proxy=settings.backend_proxy
    ).post(data).json()

def search_card(default_servers: Sequence[_Server], text: str) -> _Response:
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
    return Api(
        url,
        proxy=settings.backend_proxy
    ).post(data).json()

def search_character(default_servers: Sequence[_Server], text: str) -> _Response:
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
    return Api(
        url,
        proxy=settings.backend_proxy
    ).post(data).json()

def search_event(default_servers: Sequence[_Server], text: str) -> _Response:
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
    return Api(
        url,
        proxy=settings.backend_proxy
    ).post(data).json()

def search_gacha(default_servers: Sequence[_Server], gacha_id: int) -> _Response:
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
    return Api(
        url,
        proxy=settings.backend_proxy
    ).post(data).json()

def search_player(player_id: int, server: _Server) -> _Response:
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
    return Api(
        url,
        proxy=settings.backend_proxy
    ).post(data).json()

def search_song(default_servers: Sequence[_Server], text: str) -> _Response:
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
        'compress': settings.compress
    }
    
    # 发送请求
    return Api(
        url,
        proxy=settings.backend_proxy
    ).post(data).json()

def song_chart(default_servers: Sequence[_Server], song_id: int, difficulty_text: _DifficultyText) -> _Response:
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
    return Api(
        url,
        proxy=settings.backend_proxy
    ).post(data).json()

def song_meta(default_servers: Sequence[_Server], server: _Server) -> _Response:
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
    return Api(
        url,
        proxy=settings.backend_proxy
    ).post(data).json()

def ycx(server: _Server, tier: int, event_id: Optional[int] = None) -> _Response:
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
    return Api(
        url,
        proxy=settings.backend_proxy
    ).post(data).json()

def ycx_all(server: _Server, event_id: Optional[int] = None) -> _Response:
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
    return Api(
        url,
        proxy=settings.backend_proxy
    ).post(data).json()
