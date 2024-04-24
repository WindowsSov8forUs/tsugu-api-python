<div align="center">

![tsugu-api-ython logo](https://github.com/WindowsSov8forUs/tsugu-api-python/blob/main/logo.png)

# tsugu-api-python

_✨ Python 编写的 [TsuguBanGDreamBot](https://github.com/Yamamoto-2/tsugu-bangdream-bot?tab=readme-ov-file) 相关各种功能 API 调用库  ✨_

</div>

<p align="center">

<a href="https://github.com/Yamamoto-2/tsugu-bangdream-bot">
  <img src="https://img.shields.io/badge/tsugu bangdream bot-v1 api-FFEE88" alt="license">
</a>

<a href="https://github.com/Yamamoto-2/tsugu-bangdream-bot">
  <img src="https://img.shields.io/badge/tsugu bangdream bot-v2 api-FFEE88" alt="license">
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

</p>

## 说明

这是一个用 Python 编写的调用 [TsuguBanGDreamBot](https://github.com/Yamamoto-2/tsugu-bangdream-bot?tab=readme-ov-file) 相关各种功能 API 的库，包括绝大部分 Tsugu 提供的功能。使用本 API 库提供的方法可以实现绝大部分功能，而搭配 [bestdori-api](https://github.com/WindowsSov8forUs/bestdori-api) 可以实现用户绑定等其他功能。

> 该 API 库同时提供了异步与同步版本，可自行选择使用。

> 一切数据获取等操作通过配置的后端服务器进行，该 API 库只提供前端所需的调用功能。若需要使用本地数据库，请自行操作。

### 目前已有的功能

> 所有方法都同时拥有异步与同步版本。

#### Tsugu 后端功能

> **`None`** 表示该功能没有相应的方法。

|功能描述|v1 方法名称|v2 方法名称|
|:------|:----------|:---------|
|获取卡面图片|`get_card_illustration`|`card_illustration`|
|获取玩家状态信息|`search_player`|`player`|
|模拟指定卡池抽卡结果|`gacha_simulate`|`gacha_simulate`|
|查询指定卡池信息|`search_gacha`|`gacha`|
|查询符合条件的活动信息|`search_event`|`event`|
|查询符合条件的歌曲信息|`search_song`|`song`|
|查询歌曲分数表|`song_meta`|`song_meta`|
|查询符合条件的角色信息|`search_character`|`character`|
|查询指定歌曲指定难度的谱面|`song_chart`|`chart`|
|查询指定活动的全部档位预测线|`ycx_all`|`ycx_all`|
|查询指定活动的指定档位预测线|`ycx`|`ycx`|
|查询指定活动指定档位相关的历史预测线|`lsycx`|`lsycx`|
|获取指定车牌列表的图片形式|`room_list`|**`None`**|
|查询符合条件的卡牌|`search_card`|`card`|
|从后端获取最近的车牌信息列表|`station_query_all_room`|**`None`**|
|提交车牌信息到后端|`station_submit_room_number`|**`None`**|
|获取最近的车牌信息数据|**`None`**|`ycm`|

> 部分功能类似的方法在 `v1` 和 `v2` 中调用方式并不相同。

#### 用户数据后端功能 (仅 `v1` )

|功能描述|v1 方法名称|
|:------|:----------|
获取用户数据|`get_user_data`|
发送绑定用户请求|`bind_player_request`|
验证绑定用户请求|`bind_player_verification`|
设置是否转发指定用户的车牌|`set_car_forwarding`|
设置指定用户的默认服务器列表|`set_default_server`|
设置指定用户的主服务器模式|`set_server_mode`|

> 以上功能都可使用本地用户数据库代替，本 API 不提供相关的配置方法。

#### 车站功能 (仅 `v1` )

|功能描述|v1 方法名称|
|:------|:----------|
|提交车牌信息到车站|`submit_room_number`|


## 快速使用

以下将以获取歌曲 **EXIST** (id=325) 和卡面 **羽沢 つぐみ - Precious birthday！** (id=1672) 的信息为例。

使用以下指令安装本模块：
```bash
$ pip3 install tsugu-api-python
```

首先是使用如下代码，通过 `v1` 版本获取指定歌曲信息图片：

```python
from tsugu_api.v1 import search_song

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

然后是使用如下代码，通过 `v2` 版本获取指定卡牌信息图片：

```python
from tsugu_api.v2 import card

def main() -> None:
    result = card("1672", [3, 0]) # 这里也可以传入其他字符串 ，结果将变为一个符合参数的卡牌列表图片

main()
```

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
