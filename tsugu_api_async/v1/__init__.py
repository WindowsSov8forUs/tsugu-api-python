'''
`tsugu_api_async.v1` Tsugu 的 v1 版本 API 请求模块

v1 版本 API 为 Tsugu 原生 API
'''

from ._user import get_user_data as get_user_data
from ._user import set_server_mode as set_server_mode
from ._user import set_car_forwarding as set_car_forwarding
from ._user import set_default_server as set_default_server
from ._user import bind_player_request as bind_player_request
from ._user import bind_player_verification as bind_player_verification

from ._tsugu import ycx as ycx
from ._tsugu import lsycx as lsycx
from ._tsugu import ycx_all as ycx_all
from ._tsugu import room_list as room_list
from ._tsugu import song_meta as song_meta
from ._tsugu import song_chart as song_chart
from ._tsugu import search_card as search_card
from ._tsugu import search_song as search_song
from ._tsugu import search_event as search_event
from ._tsugu import search_gacha as search_gacha
from ._tsugu import search_player as search_player
from ._tsugu import gacha_simulate as gacha_simulate
from ._tsugu import search_character as search_character
from ._tsugu import get_card_illustration as get_card_illustration
from ._tsugu import station_query_all_room as station_query_all_room
from ._tsugu import station_submit_room_number as station_submit_room_number

from ._bandoristation import submit_room_number as submit_room_number

__all__ = [
    'get_user_data',
    'set_server_mode',
    'set_car_forwarding',
    'set_default_server',
    'bind_player_request',
    'bind_player_verification',
    'submit_room_number'
]
