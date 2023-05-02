import asyncio
import os
from pyrogram.types import CallbackQuery
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    command("الاوامر")
)
async def khalid(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/dc6751255ec8481ace945.mp4",
        caption=f""" اهلين فيك في اوامر بوت الكسا 🎶\n\n -› **جميع اوامر البوت موجودة بالاسفل**\n\n• = » [ᴄʜᴀɴɴᴇʟ](t.me/FH_KP)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "السورس", callback_data=f"gg"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"g1"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"g2"),

                ],[
                    InlineKeyboardButton(
                        "إغـلاق", callback_data=f"close"),                    

                ],
            ]
        ),
    )
@app.on_callback_query(filters.regex("hmaya"))
async def bhr(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f""" اهلين فيك في اوامر بوت الكسا 🎶\n\n -› **جميع اوامر البوت موجودة بالاسفل**\n\n• = » [ᴄʜᴀɴɴᴇʟ](t.me/FH_KP)""",reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "السورس", callback_data=f"gg"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"g1"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"g2"),

                ],[
                    InlineKeyboardButton(
                        "إغـلاق", callback_data=f"close"),                    

                ],
            ]
        ),
    )
@app.on_callback_query(filters.regex("g1"))
async def tt(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""ٓاهلـين حبـي  أليـك قائمة اوامـر التشغيل في المجموعه**
        
**اليك قائـمة الاوامــر 👇**
          

»**لتشغيل اغنيه اكتب : تشغيل او شغل**
»**لأنهاء الاغنيه اكتب : ايقاف او انهاء**
»**لايقاف الاغنيه مؤقت اكتب : قفي**
»**لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او استمر**
»**لتخطي الاغنيه اكتب : تخطي او التالي**
»**لكتم البوت في المحادثه اكتب : اسڪتي**
»**لألغاء كتم البوت في المحادثه اكتب : اتكلم او تكلمي**
»**لتحميـل الاغانـي اڪتب : بحث او تحميل**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [                  
                    InlineKeyboardButton(
                        "تحديثات الكسا", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"hmaya"),
               ],
          ]
        ),
    )
@app.on_callback_query(filters.regex("g2"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""ٓاهلـين حبـي  أليـك قائمة اوامـر التشغيل في القناه**


- لتشغيل اغنيه اكتب : شغل او تشغيل
- لتشغيل فيديو اكتب : فيديو
- لأنهاء الاغنيه اكتب : ايقاف او انهاء
- لايقاف الاغنيه مؤقت اكتب : قفي او قف
- لتكملة الاغنيه من الايقاف المؤقت اكتب : استمري او كملي
- لتخطي الاغنيه اكتب : تخطي او التالي
- لكتم البوت في الكول اكتب : /cmute
- لألغاء كتم البوت في الكول اكتب : /cunmute""",
       reply_markup=InlineKeyboardMarkup(
               [
                    [                  
                    InlineKeyboardButton(
                        "تحديثات الكسا", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"hmaya"),
               ],
          ]
        ),
    )
@app.on_callback_query(filters.regex("gg"))
async def devmusic(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""[ٓ» ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sᴏᴜʀᴄᴇ ʟɪɴᴅᴀ](https://t.me/FH_KP)\n\n[» ᴏɴᴇ ᴏғ ᴛʜᴇ ʙᴇsᴛ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛs](https://t.me/FH_KP)\n\n[» sᴏᴜʀᴄᴇ ʟɪɴᴅᴀ](https://t.me/FH_KP)""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁¹", url=f"https://t.me/FH_3B"),
                    InlineKeyboardButton(
                        "𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁²", url=f"https://t.me/Ooi_1i")
                ],[
                    InlineKeyboardButton(
                        "𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/FH_KP"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"hmaya"),
               ],
          ]
        ),
    ) 
@app.on_callback_query(filters.regex("devmusic"))
async def devmusic(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""» اهلـين حبـي أليـك قائمة قنـوات بـوت الكسا**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "𝙲𝙷𝙰𝙽𝙽𝙴𝙻¹", url=f"https://t.me/FH_KP"),
                    InlineKeyboardButton(
                        "𝙲𝙷𝙰𝙽𝙽𝙴𝙻²", url=f"https://t.me/KB_HE")
                ],[
                    InlineKeyboardButton(
                        "𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁¹", url=f"https://t.me/FH_3B"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"hmaya"),
               ],
          ]
        ),
    ) 
