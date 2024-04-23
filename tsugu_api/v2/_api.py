from tsugu_api import settings
from tsugu_api._network import Api
from tsugu_api._typing import _Server, _Response

def _v2_post_request(
    api: str,
    text: str,
    default_server: list[_Server],
    server: _Server
) -> _Response:
    '''V2 POST 请求

    参数:
        api (str): API 名称
        text (str): 参数文本（可为空）
        default_server (list[_Server]): 默认服务器列表
        server (_Server): 主服务器

    返回:
        _Response: 请求返回数据
    '''
    
    # 构建 URL
    url = f'{settings.backend_url}/v2/{api}'
    
    # 构建数据
    data = {
        'text': text,
        'default_server': default_server,
        'server': server,
        'useEasyBG': settings.use_easy_bg,
        'compress': settings.compress
    }
    
    # 发送请求
    return Api(
        url,
        proxy=settings.backend_proxy,
        data=data
    ).post().json()

def card_illustration(
    text: str
) -> _Response:
    '''卡片插图

    参数:
        text (str): 参数文本

    返回:
        _Response: 请求返回数据
    '''
    
    return _v2_post_request(
        'cardIllustration',
        text,
        [],
        3
    )

def player(
    text: str,
    server: _Server
) -> _Response:
    '''玩家状态信息

    参数:
        text (str): 参数文本
        server (_Server): 主服务器

    返回:
        _Response: 请求返回数据
    '''
    
    return _v2_post_request(
        'player',
        text,
        [],
        server
    )

def gacha_simulate(
    text: str,
    default_server: list[_Server],
    server: _Server
) -> _Response:
    '''抽卡模拟

    参数:
        text (str): 参数文本
        default_server (list[_Server]): 默认服务器列表
        server (_Server): 主服务器

    返回:
        _Response: 请求返回数据
    '''
    
    return _v2_post_request(
        'gachaSimulate',
        text,
        default_server,
        server
    )

def gacha(
    text: str,
    default_server: list[_Server],
    server: _Server
) -> _Response:
    '''查询卡池

    参数:
        text (str): 参数文本
        default_server (list[_Server]): 默认服务器列表
        server (_Server): 主服务器

    返回:
        _Response: 请求返回数据
    '''
    
    return _v2_post_request(
        'gacha',
        text,
        default_server,
        server
    )

def event(
    text: str,
    default_server: list[_Server],
    server: _Server
) -> _Response:
    '''查询活动

    参数:
        text (str): 参数文本
        default_server (list[_Server]): 默认服务器列表
        server (_Server): 主服务器

    返回:
        _Response: 请求返回数据
    '''
    
    return _v2_post_request(
        'event',
        text,
        default_server,
        server
    )

def song(
    text: str,
    default_server: list[_Server],
    server: _Server
) -> _Response:
    '''查询歌曲

    参数:
        text (str): 参数文本
        default_server (list[_Server]): 默认服务器列表
        server (_Server): 主服务器

    返回:
        _Response: 请求返回数据
    '''
    
    return _v2_post_request(
        'song',
        text,
        default_server,
        server
    )

def song_meta(
    text: str,
    default_server: list[_Server],
    server: _Server
) -> _Response:
    '''查询分数表

    参数:
        text (str): 参数文本
        default_server (list[_Server]): 默认服务器列表
        server (_Server): 主服务器

    返回:
        _Response: 请求返回数据
    '''
    
    return _v2_post_request(
        'songMeta',
        text,
        default_server,
        server
    )

def character(
    text: str,
    default_server: list[_Server],
    server: _Server
) -> _Response:
    '''查询角色

    参数:
        text (str): 参数文本
        default_server (list[_Server]): 默认服务器列表
        server (_Server): 主服务器

    返回:
        _Response: 请求返回数据
    '''
    
    return _v2_post_request(
        'character',
        text,
        default_server,
        server
    )

def chart(
    text: str,
    default_server: list[_Server],
    server: _Server
) -> _Response:
    '''查询谱面

    参数:
        text (str): 参数文本
        default_server (list[_Server]): 默认服务器列表
        server (_Server): 主服务器

    返回:
        _Response: 请求返回数据
    '''
    
    return _v2_post_request(
        'chart',
        text,
        default_server,
        server
    )

def ycx_all(
    text: str,
    default_server: list[_Server],
    server: _Server
) -> _Response:
    '''查询全部预测线

    参数:
        text (str): 参数文本
        default_server (list[_Server]): 默认服务器列表
        server (_Server): 主服务器

    返回:
        _Response: 请求返回数据
    '''
    
    return _v2_post_request(
        'ycxAll',
        text,
        default_server,
        server
    )

def ycx(
    text: str,
    default_server: list[_Server],
    server: _Server
) -> _Response:
    '''查询预测线

    参数:
        text (str): 参数文本
        default_server (list[_Server]): 默认服务器列表
        server (_Server): 主服务器

    返回:
        _Response: 请求返回数据
    '''
    
    return _v2_post_request(
        'ycx',
        text,
        default_server,
        server
    )

def lsycx(
    text: str,
    default_server: list[_Server],
    server: _Server
) -> _Response:
    '''查询历史预测线

    参数:
        text (str): 参数文本
        default_server (list[_Server]): 默认服务器列表
        server (_Server): 主服务器

    返回:
        _Response: 请求返回数据
    '''
    
    return _v2_post_request(
        'lsycx',
        text,
        default_server,
        server
    )

def ycm(
    text: str
) -> _Response:
    '''有车吗？查看现有车牌

    参数:
        text (str): 参数文本，大部分情况下传空字符串即可

    返回:
        _Response: 请求返回数据
    '''
    
    return _v2_post_request(
        'ycm',
        text,
        [],
        3
    )

def card(
    text: str,
    default_server: list[_Server],
    server: _Server
) -> _Response:
    '''查询卡牌

    参数:
        text (str): 参数文本
        default_server (list[_Server]): 默认服务器列表
        server (_Server): 主服务器

    返回:
        _Response: 请求返回数据
    '''
    
    return _v2_post_request(
        'card',
        text,
        default_server,
        server
    )
