import math
from config import SUPPORT_CHAT, OWNER_USERNAME
from pyrogram.types import InlineKeyboardButton
from SONALI_MUSIC import app
import config
from SONALI_MUSIC.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "🅚︎—————————"
    elif 10 < umm < 20:
        bar = "—🅡︎————————"
    elif 20 <= umm < 30:
        bar = "——🅘︎———————"
    elif 30 <= umm < 40:
        bar = "———🅣︎——————"
    elif 40 <= umm < 50:
        bar = "————🅘︎—————"
    elif 50 <= umm < 60:
        bar = "—————🅑︎————"
    elif 60 <= umm < 70:
        bar = "——————🅞︎———"
    elif 70 <= umm < 80:
        bar = "———————🅣︎——"
    elif 80 <= umm < 95:
        bar = "————————🅢︎—"
    else:
        bar = "🅚︎—————————"
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
         [
             InlineKeyboardButton(text="< - 𝟤𝟢ˢ", callback_data="seek_backward_20"),
             InlineKeyboardButton(text="• ᴘʀᴏᴍᴏ •", url=f"https://t.me/WHITE_DEVIL_BANNER"),
             InlineKeyboardButton(text="𝟤𝟢ˢ + >", callback_data="seek_forward_20")
         ],
        [
            InlineKeyboardButton(text="˹ᴋɪᴅɴᴀᴘ ᴍᴇ ʙᴀʙᴇs˼", url=f"https://t.me/{app.username}?startgroup=true"),
        ]
    ]
    return buttons 
    
    def stream_markup(_, chat_id):

        def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    
        
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"SonaPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"SonaPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        
        callback_data=f"SonaPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            

        
def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
    



