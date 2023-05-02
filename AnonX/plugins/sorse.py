
import asyncio

import os
import config
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint
@app.on_message(
    command(["السورس","سورس"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/dc6751255ec8481ace945.mp4",
        caption=f"""[» ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sᴏᴜʀᴄᴇ ʟɪɴᴅᴀ](https://t.me/FH_KP)\n\n[» ᴏɴᴇ ᴏғ ᴛʜᴇ ʙᴇsᴛ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛs](https://t.me/FH_KP)\n\n[» sᴏᴜʀᴄᴇ ʟɪɴᴅᴀ](https://t.me/KB_HE)**""",
        reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "𝙲𝙷𝙰𝙽𝙽𝙴𝙻¹", url=f"https://t.me/FH_KP"),
                    InlineKeyboardButton(
                        "𝙲𝙷𝙰𝙽𝙽𝙴𝙻²", url=f"https://t.me/KB_HE")
                ],[
                    InlineKeyboardButton(
                       "𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁", user_id=6274098601)
              
                 ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )



