import warnings
from typing_extensions import deprecated
from typing import List, Optional, Sequence

from tsugu_api_core._network import Api
from tsugu_api_core._settings import settings
from tsugu_api_core._typing import (
    _Room,
    Server,
    ServerId,
    _Response,
    _DifficultyId,
    FuzzySearchResult,
    _FuzzySearchResponse
)

def cutoff_all(main_server: ServerId, event_id: Optional[int] = None) -> _Response:
    '''查询活动排行榜全部预测线

    参数:
        main_server (_ServerId): 主服务器
        event_id (int): 活动 ID

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'mainServer': main_server,
        'compress': settings.compress
    }
    if event_id:
        data['eventId'] = event_id
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/cutoffAll',
        proxy=settings.backend_proxy
    ).post(data).json()

def cutoff_detail(main_server: ServerId, tier: int, event_id: Optional[int] = None) -> _Response:
    '''查询活动排行榜预测线

    参数:
        main_server (_ServerId): 主服务器
        tier (int): 排行榜挡位
        event_id (int): 活动 ID

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'mainServer': main_server,
        'tier': tier,
        'compress': settings.compress
    }
    if event_id:
        data['eventId'] = event_id
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/cutoffDetail',
        proxy=settings.backend_proxy
    ).post(data).json()

def cutoff_list_of_recent_event(main_server: ServerId, tier: int, event_id: Optional[int] = None) -> _Response:
    '''查询历史活动排行榜预测线

    参数:
        main_server (_ServerId): 主服务器
        tier (int): 排行榜挡位
        event_id (int): 活动 ID

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'mainServer': main_server,
        'tier': tier,
        'compress': settings.compress
    }
    if event_id:
        data['eventId'] = event_id
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/cutoffListOfRecentEvent',
        proxy=settings.backend_proxy
    ).post(data).json()

def event_stage(main_server: ServerId, event_id: Optional[int] = None, meta: bool = False) -> _Response:
    '''查询团队 LIVE 佳节活动舞台数据

    参数:
        main_server (_ServerId): 主服务器
        event_id (int): 活动 ID
        meta (bool): 是否携带歌曲分数表

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'mainServer': main_server,
        'meta': meta,
        'compress': settings.compress
    }
    if event_id:
        data['eventId'] = event_id
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/eventStage',
        proxy=settings.backend_proxy
    ).post(data).json()

def fuzzy_search(text: str) -> _FuzzySearchResponse:
    '''模糊搜索

    参数:
        text (str): 搜索文本

    返回:
        _FuzzySearchResponse: 响应信息
    '''
    
    # 构建数据
    data = {
        'text': text,
        'compress': settings.compress
    }
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/fuzzySearch',
        proxy=settings.backend_proxy
    ).post(data).json()

def gacha_simulate(main_server: ServerId, times: Optional[int] = None, gacha_id: Optional[int] = None) -> _Response:
    '''模拟抽卡

    参数:
        main_server (_ServerId): 主服务器
        times (int): 抽卡次数
        gacha_id (int): 卡池 ID

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'mainServer': main_server,
        'compress': settings.compress
    }
    if times:
        data['times'] = times
    if gacha_id:
        data['gachaId'] = gacha_id
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/gachaSimulate',
        proxy=settings.backend_proxy
    ).post(data).json()

def get_card_illustration(card_id: int) -> _Response:
    '''获取卡面

    参数:
        card_id (int): 卡片 ID

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'cardId': str(card_id)
    }
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/getCardIllustration',
        proxy=settings.backend_proxy
    ).post(data).json()

@deprecated("The `lsycx` api is now deprecated, use `cutoff_list_of_recent_event` instead.", category=None)
def lsycx(server: Server, tier: int, event_id: Optional[int] = None) -> _Response:
    '''查询历史排行榜预测线

    参数:
        server (_Server): 服务器
        tier (int): 排行榜挡位
        event_id (int): 活动 ID

    返回:
        _Response: 响应信息
    '''
    warnings.warn(
        "The `lsycx` api is now deprecated, use `cutoff_list_of_recent_event` instead.",
        DeprecationWarning
    )
    
    if not isinstance(server, int):
        raise ValueError("'server' must be an integer.")
    
    return cutoff_list_of_recent_event(server, tier, event_id)

def room_list(room_list: List[_Room]) -> _Response:
    '''绘制车牌绘图

    参数:
        room_list (list[_CarData]): 车牌信息列表

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'roomList': room_list,
        'compress': settings.compress
    }
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/roomList',
        proxy=settings.backend_proxy
    ).post(data).json()

def search_card(
    displayed_server_list: Sequence[ServerId],
    text: Optional[str] = None,
    fuzzy_search_result: Optional[FuzzySearchResult] = None
) -> _Response:
    '''查询卡片

    参数:
        displayed_server_list (Sequence[_ServerId]): 展示服务器
        text (str): 查询参数，与 `fuzzy_search_result` 二选一
        fuzzy_search_result (_FuzzySearchResult): 模糊搜索结果，与 `text` 二选一

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'displayedServerList': displayed_server_list,
        'useEasyBG': settings.use_easy_bg,
        'compress': settings.compress
    }
    if text:
        data['text'] = text
    if fuzzy_search_result:
        data['fuzzySearchResult'] = fuzzy_search_result
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/searchCard',
        proxy=settings.backend_proxy
    ).post(data).json()

def search_character(
    displayed_server_list: Sequence[ServerId],
    fuzzy_search_result: Optional[FuzzySearchResult] = None,
    text: Optional[str] = None
) -> _Response:
    '''查询角色

    参数:
        displayed_server_list (Sequence[_ServerId]): 展示服务器
        fuzzy_search_result (_FuzzySearchResult): 模糊搜索结果，与 `text` 二选一
        text (str): 查询参数，与 `fuzzy_search_result` 二选一

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'displayedServerList': displayed_server_list,
        'compress': settings.compress
    }
    if fuzzy_search_result:
        data['fuzzySearchResult'] = fuzzy_search_result
    if text:
        data['text'] = text
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/searchCharacter',
        proxy=settings.backend_proxy
    ).post(data).json()

def search_event(
    displayed_server_list: Sequence[ServerId],
    fuzzy_search_result: Optional[FuzzySearchResult] = None,
    text: Optional[str] = None
) -> _Response:
    '''查询活动

    参数:
        displayed_server_list (Sequence[_ServerId]): 展示服务器
        fuzzy_search_result (_FuzzySearchResult): 模糊搜索结果，与 `text` 二选一
        text (str): 查询参数，与 `fuzzy_search_result` 二选一

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'displayedServerList': displayed_server_list,
        'useEasyBG': settings.use_easy_bg,
        'compress': settings.compress
    }
    if fuzzy_search_result:
        data['fuzzySearchResult'] = fuzzy_search_result
    if text:
        data['text'] = text
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/searchEvent',
        proxy=settings.backend_proxy
    ).post(data).json()

def search_gacha(
    displayed_server_list: Sequence[ServerId],
    gacha_id: int
) -> _Response:
    '''查询卡池

    参数:
        displayed_server_list (Sequence[_ServerId]): 展示服务器
        gacha_id (int): 卡池 ID

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'displayedServerList': displayed_server_list,
        'gachaId': gacha_id,
        'useEasyBG': settings.use_easy_bg,
        'compress': settings.compress
    }
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/searchGacha',
        proxy=settings.backend_proxy
    ).post(data).json()

def search_player(player_id: int, main_server: ServerId) -> _Response:
    '''查询玩家状态

    参数:
        player_id (int): 玩家 ID
        main_server (_ServerId): 服务器

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'playerId': player_id,
        'mainServer': main_server,
        'useEasyBG': settings.use_easy_bg,
        'compress': settings.compress
    }
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/searchPlayer',
        proxy=settings.backend_proxy
    ).post(data).json()

def search_song(
    displayed_server_list: Sequence[ServerId],
    fuzzy_search_result: Optional[FuzzySearchResult] = None,
    text: Optional[str] = None
) -> _Response:
    '''查询歌曲

    参数:
        displayed_server_list (Sequence[_ServerId]): 展示服务器
        fuzzy_search_result (_FuzzySearchResult): 模糊搜索结果，与 `text` 二选一
        text (str): 查询参数，与 `fuzzy_search_result` 二选一

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'displayedServerList': displayed_server_list,
        'compress': settings.compress
    }
    if fuzzy_search_result:
        data['fuzzySearchResult'] = fuzzy_search_result
    if text:
        data['text'] = text
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/searchSong',
        proxy=settings.backend_proxy
    ).post(data).json()

def song_chart(
    displayed_server_list: Sequence[ServerId],
    song_id: int,
    difficulty_id: _DifficultyId
) -> _Response:
    '''查询歌曲谱面

    参数:
        displayed_server_list (Sequence[_ServerId]): 展示服务器
        song_id (int): 歌曲 ID
        difficulty_id (_DifficultyId): 难度 ID

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'displayedServerList': displayed_server_list,
        'songId': song_id,
        'difficultyId': difficulty_id,
        'compress': settings.compress
    }
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/songChart',
        proxy=settings.backend_proxy
    ).post(data).json()

def song_meta(
    displayed_server_list: Sequence[ServerId],
    main_server: ServerId
) -> _Response:
    '''查询歌曲分数表

    参数:
        displayed_server_list (Sequence[_ServerId]): 展示服务器
        main_server (_ServerId): 主服务器

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'displayedServerList': displayed_server_list,
        'mainServer': main_server,
        'compress': settings.compress
    }
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/songMeta',
        proxy=settings.backend_proxy
    ).post(data).json()

def song_random(
    main_server: ServerId,
    fuzzy_search_result: Optional[FuzzySearchResult] = None,
    text: Optional[str] = None
) -> _Response:
    '''随机歌曲

    参数:
        main_server (_ServerId): 主服务器
        fuzzy_search_result (_FuzzySearchResult): 模糊搜索结果，与 `text` 二选一
        text (str): 查询参数，与 `fuzzy_search_result` 二选一

    返回:
        _Response: 响应信息
    '''
    
    # 构建数据
    data = {
        'mainServer': main_server,
        'useEasyBG': settings.use_easy_bg,
        'compress': settings.compress
    }
    if fuzzy_search_result:
        data['fuzzySearchResult'] = fuzzy_search_result
    if text:
        data['text'] = text
    
    # 发送请求
    return Api(
        settings.backend_url,
        '/songRandom',
        proxy=settings.backend_proxy
    ).post(data).json()

@deprecated("The `ycx` api is now deprecated, use `cutoff_detail` instead.", category=None)
def ycx(server: Server, tier: int, event_id: Optional[int] = None) -> _Response:
    '''查询排行榜预测线

    参数:
        server (_Server): 服务器
        tier (int): 排行榜挡位
        event_id (int): 活动 ID

    返回:
        _Response: 响应信息
    '''
    warnings.warn(
        "The `ycx` api is now deprecated, use `cutoff_detail` instead.",
        DeprecationWarning
    )
    
    if not isinstance(server, int):
        raise ValueError("'server' must be an integer.")
    
    return cutoff_detail(server, tier, event_id)

@deprecated("The `ycx_all` api is now deprecated, use `cutoff_all` instead.", category=None)
def ycx_all(server: Server, event_id: Optional[int] = None) -> _Response:
    '''查询全挡位预测线

    参数:
        server (_Server): 服务器
        event_id (int): 活动 ID

    返回:
        _Response: 响应信息
    '''
    warnings.warn(
        "The `ycx_all` api is now deprecated, use `cutoff_all` instead.",
        DeprecationWarning
    )
    
    if not isinstance(server, int):
        raise ValueError("'server' must be an integer.")
    
    return cutoff_all(server, event_id)
