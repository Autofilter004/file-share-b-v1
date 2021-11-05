from pyrogram import __version__

from bot import Bot

from config import OWNER_ID

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()

async def cb_handler(client: Bot, query: CallbackQuery):

    data = query.data

    if data == "about":

        await query.message.reply_photo(

            "https://telegra.ph/file/9547063d1d78f20e6d073.jpg",

            caption = f"<b>➥ Creator : <a href='tg://user?id={OWNER_ID}'>🇩ᴇᴇᴘᴜ</a>\n\n➥ Language : <code>Python3</code>\n\n➥ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n\n➥ Source Code : <a href='https://github.com'>Click here</a>\n\n➥ Channel : @Xaglerzz\n\n➥ Support : @Deepu_The_Editor</b>",

            reply_markup = InlineKeyboardMarkup(

                [

                    [

                        InlineKeyboardButton("🔒 Close", callback_data = "close")

                    ]

                ]

            )

        )

    elif data == "close":

        await query.message.delete()

        try:

            await query.message.reply_to_message.delete()

        except:

            pass
