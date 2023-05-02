from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجمـوعتك",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="الاوامـر",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="المساعدة", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="الاوامـر", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙲𝙷𝙰𝙽𝙽𝙴𝙻¹", url=f"https://t.me/FH_KP"
            ),
            InlineKeyboardButton(
                text="𝙲𝙷𝙰𝙽𝙽𝙴𝙻²", url=f"https://t.me/KB_HE"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER
            )
        ],
     ]
    return buttons
