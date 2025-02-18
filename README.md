<div align="center">

![tsugu-api-ython logo](https://github.com/WindowsSov8forUs/tsugu-api-python/blob/main/logo.png)

# tsugu-api-python

_✨ Python 编写的 [TsuguBanGDreamBot](https://github.com/Yamamoto-2/tsugu-bangdream-bot?tab=readme-ov-file) 相关各种功能 API 调用库  ✨_

</div>

<p align="center">

<a href="https://github.com/Yamamoto-2/tsugu-bangdream-bot">
  <img src="https://img.shields.io/badge/tsugu bangdream bot-api-FFEE88" alt="license">
</a>

<a href="https://github.com/WindowsSov8forUs/tsugu-api-python">
  <img src="https://img.shields.io/github/v/release/WindowsSov8forUs/tsugu-api-python" alt="Latest Release Version">
</a>

<a href="https://github.com/WindowsSov8forUs/tsugu-api-python/blob/main/LICENSE">
  <img src="https://img.shields.io/github/license/WindowsSov8forUs/tsugu-api-python" alt="License">
</a>

<a href="https://www.python.org/downloads/">
  <img src="https://img.shields.io/pypi/pyversions/tsugu-api-python" alt="Python Version">
</a>

<a href="https://pypi.org/project/tsugu-api-python/">
  <img src="https://img.shields.io/pypi/v/tsugu-api-python?label=stable" alt="PyPI Version">
</a>

<a href="https://pypi.org/project/tsugu-api-python/">
  <img src="https://img.shields.io/pypi/v/tsugu-api-python?include_prereleases&label=latest" alt="PyPI Version">
</a>

</p>

## 说明

这是一个用 Python 编写的调用 [TsuguBanGDreamBot](https://github.com/Yamamoto-2/tsugu-bangdream-bot?tab=readme-ov-file) 相关各种功能 API 的库，包括绝大部分 Tsugu 提供的功能。使用本 API 库提供的方法可以实现绝大部分功能，而搭配 [bestdori-api](https://github.com/WindowsSov8forUs/bestdori-api) 可以实现用户绑定等其他功能。

> 该 API 库同时提供了异步与同步版本，可自行选择使用。

> 一切数据获取等操作通过配置的后端服务器进行，该 API 库只提供前端所需的调用功能。若需要使用本地数据库，请自行操作。

### 目前已有的功能

> 所有方法都同时拥有异步与同步版本。

#### Tsugu 后端功能

|功能描述|方法名称|
|:------|:----------|
|获取活动试炼舞台信息|`event_stage`|
|模拟指定卡池抽卡结果|`gacha_simulate`|
|获取卡面图片|`get_card_illustration`|
|查询指定活动指定档位相关的历史预测线|`lsycx`|
|获取指定车牌列表的图片形式|`room_list`|
|查询符合条件的卡牌|`search_card`|
|查询符合条件的角色信息|`search_character`|
|查询符合条件的活动信息|`search_event`|
|查询指定卡池信息|`search_gacha`|
|获取玩家状态信息|`search_player`|
|查询符合条件的歌曲信息|`search_song`|
|查询指定歌曲指定难度的谱面|`song_chart`|
|查询歌曲分数表|`song_meta`|
|查询指定活动的指定档位预测线|`ycx`|
|查询指定活动的全部档位预测线|`ycx_all`|

#### 车站数据后端功能

|功能描述|方法名称|
|:------|:----------|
|提交房间信息到后端|`station_submit_room_number`|
|从后端获取最近的房间信息列表|`station_query_all_room`|

> 若后端不支持用户数据库，以上功能可能无法使用，请以 **车站功能** API 代替。

#### 用户数据后端功能

|功能描述|方法名称|
|:------|:----------|
|获取用户数据|`get_user_data`|
|修改用户数据|`change_user_data`|
|发送绑定用户请求|`bind_player_request`|
|验证绑定用户请求|`bind_player_verification`|

> 以上功能都可使用本地用户数据库代替，本 API 不提供相关的配置方法。

#### 车站功能

|功能描述|方法名称|
|:------|:----------|
|从车站获取最近的房间信息列表|`query_room_number`|
|提交房间信息到车站|`submit_room_number`|


## 快速使用

以下将以获取歌曲 **EXIST** (id=325) 的信息为例。

使用以下指令安装本模块：
```bash
$ pip3 install tsugu-api-python
```

使用如下代码，获取指定歌曲信息图片：

```python
from tsugu_api import search_song

def main() -> None:
    result = search_song([3, 0], "EXIST") # 这里也可以传入 "325" ，具体取决于用户输入信息

main()
```

> `[3, 0]` 指代用户的默认服务器列表，可从通过 `get_user_data()` 方法获取的返回值中获取。

获取到的 `result` 将是一个 `_Response` 对象，当获取到准确的信息时， `result` 的值如下：

```python
[
    {
        "type": "base64",
        "string": ... # 图片的 Base64 字符串
    }
]
```

若传入的查询参数不合法或查询过程中出错，获取到的 `result` 的值如下：

```python
[
    {
        "type": "string",
        "string": ... # 错误信息
    }
]
```

> 异步版本的调用方式相同，只是将 `tsugu_api` 改为 `tsugu_api_async` 即可。

### 注册自定义 HTTP 客户端

在 `1.5.0` 以后版本， `tsugu-api-python` 将不再强制要求安装 `httpx` 与 `aiohttp` 库，并允许用户自己实现用于请求的 HTTP 客户端。 `tsugu-api-python` 内部提供对于 `httpx` 与 `aiohttp` 的客户端实现。

用户可通过实现 `tsugu_api_core.client.Client` 类，并通过 `tsugu_api_core.register_client` 方法注册。注册后 `tsugu-api-python` 将不会根据 `settings` 中的 `client` 配置选择客户端实现，而是使用用户提供的自定义客户端实现。

以下给出一个实现基于 `requests` 请求库的客户端实现。

```python
# 客户端实现

# 导入一些需要的库
from json import dumps
from typing import Any, cast
from typing_extensions import override

# 导入 requests 库
import requests

# 导入 Client 基类与 Request 、 Response 类
from tsugu_api_core.client import Client as _Client
from tsugu_api_core.client import Request, Response

# 实现客户端类
class Client(_Client):
    _session: requests.Session

    @override
    def __enter__(self) -> 'Client':
        self._client = requests.Session()
        self._client.trust_env = True
        self._client.__enter__()
        return self
    
    @override
    async def __aenter__(self) -> 'Client':
        # requests 库是一个同步请求库，但客户端需要进行异步实现。这里抛出异常来指出这个错误使用。
        raise RuntimeError('REQUESTS client is not asynchronous, please use sync context manager')
    
    @override
    def __exit__(self, *args: Any) -> None:
        self._session.close()
    
    @override
    async def __aexit__(self, *args: Any) -> None:
        pass # 这里这个方法永远不会被使用

    @override
    def request(self, request: Request) -> Response:
        # requests 需要一个代理字典，但 Client 类只会传入一个代理地址，这里构建这个字典。
        # 此处实现根据用户需求不同进行不同实现。
        proxies = {
            'http': self.proxy,
            'https': self.proxy,
        }

        # 此处请求实现根据用户需求不同而进行不同实现
        # 这里列举出了 Request 类的所有可拥有属性
        with self._session.request(
            request.method,
            request.url,
            params=request.params,
            data=cast(dict, dumps(request.data)) if request.data is not None else request.data,
            headers=request.headers,
            proxies=proxies if self.proxy else None,
        ) as response:
            # 请求后构建 Response 类并返回
            # - content: 响应内容， bytes 类型
            # - status_code: 状态码
            # - exception: raise_for_status 方法抛出的错误
            try:
                response.raise_for_status()
                return Response(
                    response.content,
                    response.status_code,
                )
            except Exception as exception:
                return Response(
                    response.content,
                    response.status_code,
                    exception,
                )
    
    @override
    async def arequest(self, request: Request) -> Response:
        # requests 库是一个同步请求库，但客户端需要进行异步实现。这里抛出异常来指出这个错误使用。
        raise RuntimeError('REQUESTS client is not asynchronous, please use sync request method.')
```

在客户端实现后，通过注册方法注册客户端。

```python
from tsugu_api_core import register_client

register_client(Client)
```

随后 `tsugu-api-python` 就会在进行同步请求时优先使用自定义的基于 `requests` 请求库的客户端，而不是内置的基于 `httpx` 库的客户端。