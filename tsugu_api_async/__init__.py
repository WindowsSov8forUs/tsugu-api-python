'''
`tsugu_api` 向 Tsugu 后端 API 请求模块
'''

from tsugu_api_core.utils import *

import tsugu_api_core.settings as settings

from ._user import get_user_data as get_user_data
from ._user import change_user_data as change_user_data
from ._user import bind_player_request as bind_player_request
from ._user import bind_player_verification as bind_player_verification

from ._tsugu import ycx as ycx
from ._tsugu import lsycx as lsycx
from ._tsugu import ycx_all as ycx_all
from ._tsugu import room_list as room_list
from ._tsugu import song_meta as song_meta
from ._tsugu import cutoff_all as cutoff_all
from ._tsugu import song_chart as song_chart
from ._tsugu import event_stage as event_stage
from ._tsugu import search_card as search_card
from ._tsugu import search_song as search_song
from ._tsugu import song_random as song_random
from ._tsugu import fuzzy_search as fuzzy_search
from ._tsugu import search_event as search_event
from ._tsugu import search_gacha as search_gacha
from ._tsugu import cutoff_detail as cutoff_detail
from ._tsugu import search_player as search_player
from ._tsugu import gacha_simulate as gacha_simulate
from ._tsugu import search_character as search_character
from ._tsugu import get_card_illustration as get_card_illustration
from ._tsugu import cutoff_list_of_recent_event as cutoff_list_of_recent_event

from ._station import station_query_all_room as station_query_all_room
from ._station import station_submit_room_number as station_submit_room_number

from ._bandoristation import query_room_number as query_room_number
from ._bandoristation import submit_room_number as submit_room_number
