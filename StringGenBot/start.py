from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention},

اهلا بك ✋ {me2},
مكنك الحصول على كودب ايروجرام او تيليثون اضغط على الزر بالاسفل مط

انضم لقناة السورس 🖤 ʙʏ : [قنـاة السوࢪس](https://t.me/aaaalqp) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="• اضغط للحصول على جلسة •", callback_data="generate")
                ],
                [
                    InlineKeyboardButton(" • سوࢪس الخليفه •", url="https://t.me/aaaalqp"),
                    InlineKeyboardButton("• مطوࢪ البوت •", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
