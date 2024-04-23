'''对 tsugu_api 进行配置'''

from enum import StrEnum
from typing import Optional

class Client(StrEnum):
    HTTPX: str = 'httpx'
    '''使用 `httpx`'''
    AIO_HTTP: str = 'aiohttp'
    '''使用 `aiohttp`'''

client: Client = Client.HTTPX
'''使用的 HTTP 客户端'''

timeout: int = 10
'''请求超时时间'''

proxy: str = ''
'''代理地址'''

backend_url: str = 'http://tsugubot.com:8080'
'''
后端地址

默认为 Tsugu 官方后端，若有自建后端服务器可进行修改。
'''
backend_proxy: bool = True
'''
是否使用后端代理

当设置代理地址后可修改此项以决定是否使用代理。

默认为 True，即使用后端代理。若使用代理时后端服务器无法访问，可将此项设置为 False。
'''
userdata_backend_url: str = 'http://tsugubot.com:8080'
'''
用户数据后端地址

默认为 Tsugu 官方后端，若有自建后端服务器可进行修改。
'''
userdata_backend_proxy: bool = True
'''
是否使用用户数据后端代理

当设置代理地址后可修改此项以决定是否使用代理。

默认为 True，即使用后端代理。若使用代理时后端服务器无法访问，可将此项设置为 False。
'''

use_easy_bg: bool = True
'''
是否使用简易背景，使用可在降低背景质量的前提下加快响应速度。

默认为 True，即使用简易背景。若不使用简易背景，可将此项设置为 False。
'''
compress: bool = True
'''
是否压缩返回数据，压缩可减少返回数据大小。

默认为 True，即压缩返回数据。若不压缩返回数据，可将此项设置为 False。
'''

def _get_proxy() -> Optional[dict[str, str]]:
    global proxy
    
    if proxy == '':
        return None
    return {
        'http://': proxy,
        'https://': proxy
    }

__all__ = [
    'timeout',
    'proxy',
    'backend_url',
    'backend_proxy',
    'userdata_backend_url',
    'userdata_backend_proxy',
    'use_easy_bg',
    'compress'
]
