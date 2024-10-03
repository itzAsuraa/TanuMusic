import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message

import config
from config import BANNED_USERS
from strings import get_command
from TanuMusic import app
from TanuMusic.misc import db
from TanuMusic.utils import Dnsbin, get_channeplayCB, seconds_to_min
from TanuMusic.utils.database import get_cmode, is_active_chat, is_music_playing
from TanuMusic.utils.decorators.language import language, languageCB
from TanuMusic.utils.inline import queue_back_markup, queue_markup

###Commands
QUEUE_COMMAND = get_command("QUEUE_COMMAND")

basic = {}


def get_image(videoid):
    try:
        url = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
        return url
    except Exception:
        return config.YOUTUBE_IMG_URL


def get_duration(playing):
    file_path = playing[0]["file"]
    if "index_" in file_path or "live_" in file_path:
        return "Unknown"
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return "Unknown"
    else:
        return "Inline"


@app.on_message(filters.command(QUEUE_COMMAND) & filters.group & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    if message.command[0][0] == "c":
        chat_id = await get_cmode(message.chat.id)
        if chat_id is None:
            return await message.reply_text(_["setting_12"])
        try:
            await app.get_chat(chat_id)
        except:
            return await message.reply_text(_["cplay_4"])
        cplay = True
    else:
        chat_id = message.chat.id
        cplay = False
    if not await is_active_chat(chat_id):
        return await message.reply_text(_["general_6"])
    got = db.get(chat_id)
    if not got:
        return await message.reply_text(_["queue_2"])
    file = got[0]["file"]
    videoid = got[0]["vidid"]
    user = got[0]["by"]
    title = (got[0]["title"]).title()
    typo = (got[0]["streamtype"]).title()
    DUR = get_duration(got)
    if "live_" in file:
        IMAGE = get_image(videoid)
    elif "vid_" in file:
        IMAGE = get_image(videoid)
    elif "index_" in file:
        IMAGE = config.STREAM_IMG_URL
    else:
        if videoid == "telegram":
            IMAGE = (
                config.TELEGRAM_AUDIO_URL
                if typo == "Audio"
                else config.TELEGRAM_VIDEO_URL
            )
        elif videoid == "soundcloud":
            IMAGE = config.SOUNCLOUD_IMG_URL
        else:
            IMAGE = get_image(videoid)
    send = (
        "**⌛️ᴅᴜʀᴀᴛɪᴏɴ:** ᴜɴᴋɴᴏᴡɴ ᴅᴜʀᴀᴛɪᴏɴ sᴛʀᴇᴀᴍ \n\nᴄʟɪᴄᴋ ᴏɴ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴡʜᴏʟᴇ ǫᴜᴇᴜᴇᴅ ʟɪsᴛ."
        if DUR == "Unknown"
        else "\nᴄʟɪᴄᴋ ᴏɴ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴡʜᴏʟʀ ǫᴜᴇᴜᴇᴅ ʟɪsᴛ."
    )
    cap = f"""**{app.mention} ᴘʟᴀʏᴇʀ**

🎥**ᴘʟᴀʏɪɴɢ:** {title}

🔗**sᴛʀᴇᴀᴍ ᴛʏᴘᴇ:** {typo}
🙍‍♂️**ᴘʟᴀʏᴇᴅ ʙʏ:** {user}
{send}"""
    upl = (
        queue_markup(_, DUR, "c" if cplay else "g", videoid)
        if DUR == "Unknown"
        else queue_markup(
            _,
            DUR,
            "c" if cplay else "g",
            videoid,
            seconds_to_min(got[0]["played"]),
            got[0]["dur"],
        )
    )
    basic[videoid] = True
    mystic = await message.reply_photo(IMAGE, caption=cap, reply_markup=upl)
    if DUR != "Unknown":
        try:
            while db[chat_id][0]["vidid"] == videoid:
                await asyncio.sleep(5)
                if await is_active_chat(chat_id):
                    if basic[videoid]:
                        if await is_music_playing(chat_id):
                            try:
                                buttons = queue_markup(
                                    _,
                                    DUR,
                                    "c" if cplay else "g",
                                    videoid,
                                    seconds_to_min(db[chat_id][0]["played"]),
                                    db[chat_id][0]["dur"],
                                )
                                await mystic.edit_reply_markup(reply_markup=buttons)
                            except FloodWait:
                                pass
                        else:
                            pass
                    else:
                        break
                else:
                    break
        except:
            return


@app.on_callback_query(filters.regex("GetTimer") & ~BANNED_USERS)
async def quite_timer(client, CallbackQuery: CallbackQuery):
    try:
        await CallbackQuery.answer()
    except:
        pass


@app.on_callback_query(filters.regex("GetQueued") & ~BANNED_USERS)
@languageCB
async def queued_tracks(client, CallbackQuery: CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    what, videoid = callback_request.split("|")
    try:
        chat_id, channel = await get_channeplayCB(_, what, CallbackQuery)
    except:
        return
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_6"], show_alert=True)
    got = db.get(chat_id)
    if not got:
        return await CallbackQuery.answer(_["queue_2"], show_alert=True)
    if len(got) == 1:
        return await CallbackQuery.answer(_["queue_5"], show_alert=True)
    await CallbackQuery.answer()
    basic[videoid] = False
    buttons = queue_back_markup(_, what)
    med = InputMediaPhoto(
        media="https://telegra.ph//file/6f7d35131f69951c74ee5.jpg",
        caption=_["queue_1"],
    )
    await CallbackQuery.edit_message_media(media=med)
    j = 0
    msg = ""
    for x in got:
        j += 1
        if j == 1:
            msg += f'ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ:\n\n🏷ᴛɪᴛʟᴇ: {x["title"]}\nᴅᴜʀᴀᴛɪᴏɴ: {x["dur"]}\nʙʏ: {x["by"]}\n\n'
        elif j == 2:
            msg += f'ǫᴜᴇᴜᴇᴅ:\n\n🏷ᴛɪᴛʟᴇ: {x["title"]}\nᴅᴜʀᴀᴛɪᴏɴ: {x["dur"]}\nʙʏ: {x["by"]}\n\n'
        else:
            msg += f'🏷ᴛɪᴛʟᴇ: {x["title"]}\nᴅᴜʀᴀᴛɪᴏɴ: {x["dur"]}\nʙʏ: {x["by"]}\n\n'
    if "Queued" in msg:
        if len(msg) < 700:
            await asyncio.sleep(1)
            return await CallbackQuery.edit_message_text(msg, reply_markup=buttons)

        if "🏷" in msg:
            msg = msg.replace("🏷", "")
        if "ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ" in msg:
            msg = msg.replace("ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ", "Current Playling")
        if "ᴛɪᴛʟᴇ" in msg:
            msg = msg.replace("ᴛɪᴛʟᴇ", "Title")
        if "ᴅᴜʀᴀᴛɪᴏɴ" in msg:
            msg = msg.replace("ᴅᴜʀᴀᴛɪᴏɴ", "Duration")
        if "ʙʏ" in msg:
            msg = msg.replace("ʙʏ", "By")
        if "ǫᴜᴇᴜᴇᴅ" in msg:
            msg = msg.replace("ǫᴜᴇᴜᴇᴅ", "Queued")

        link = await Dnsbin(msg)
        await CallbackQuery.edit_message_text(
            _["queue_3"].format(link), reply_markup=buttons
        )
    else:
        if len(msg) > 700:
            if "🏷" in msg:
                msg = msg.replace("🏷", "")
            if "ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ" in msg:
                msg = msg.replace("ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ", "Current Playling")
            if "ᴛɪᴛʟᴇ" in msg:
                msg = msg.replace("ᴛɪᴛʟᴇ", "Title")
            if "ᴅᴜʀᴀᴛɪᴏɴ" in msg:
                msg = msg.replace("ᴅᴜʀᴀᴛɪᴏɴ", "Duration")
            if "ʙʏ" in msg:
                msg = msg.replace("ʙʏ", "By")
            if "ǫᴜᴇᴜᴇᴅ" in msg:
                msg = msg.replace("ǫᴜᴇᴜᴇᴅ", "Queued")

            link = await Dnsbin(msg)
            await asyncio.sleep(1)
            return await CallbackQuery.edit_message_text(
                _["queue_3"].format(link), reply_markup=buttons
            )

        await asyncio.sleep(1)
        return await CallbackQuery.edit_message_text(msg, reply_markup=buttons)


@app.on_callback_query(filters.regex("queue_back_timer") & ~BANNED_USERS)
@languageCB
async def queue_back(client, CallbackQuery: CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cplay = callback_data.split(None, 1)[1]
    try:
        chat_id, channel = await get_channeplayCB(_, cplay, CallbackQuery)
    except:
        return
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_6"], show_alert=True)
    got = db.get(chat_id)
    if not got:
        return await CallbackQuery.answer(_["queue_2"], show_alert=True)
    await CallbackQuery.answer(_["set_cb_8"], show_alert=True)
    file = got[0]["file"]
    videoid = got[0]["vidid"]
    user = got[0]["by"]
    title = (got[0]["title"]).title()
    typo = (got[0]["streamtype"]).title()
    DUR = get_duration(got)
    if "live_" in file:
        IMAGE = get_image(videoid)
    elif "vid_" in file:
        IMAGE = get_image(videoid)
    elif "index_" in file:
        IMAGE = config.STREAM_IMG_URL
    else:
        if videoid == "telegram":
            IMAGE = (
                config.TELEGRAM_AUDIO_URL
                if typo == "Audio"
                else config.TELEGRAM_VIDEO_URL
            )
        elif videoid == "soundcloud":
            IMAGE = config.SOUNCLOUD_IMG_URL
        else:
            IMAGE = get_image(videoid)
    send = (
        "**⌛️ᴅᴜʀᴀᴛɪᴏɴ:** ᴜɴᴋɴᴏᴡɴ ᴅᴜʀᴀᴛɪᴏɴ sᴛʀᴇᴀᴍ \n\nᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴡʜᴏʟᴇ ǫᴜᴇᴜᴇᴅ ʟɪsᴛ."
        if DUR == "Unknown"
        else "\nᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴡʜᴏʟᴇ ǫᴜᴇᴜᴇᴅ ʟɪsᴛ."
    )
    cap = f"""**{app.mention} ᴘʟᴀʏᴇʀ**

🎥**ᴘʟᴀʏɪɴɢ:** {title}

🔗**sᴛʀᴇᴀᴍ ᴛʏᴘᴇ:** {typo}
🙍‍♂️**ᴘʟᴀʏᴇᴅ ʙʏ :** {user}
{send}"""
    upl = (
        queue_markup(_, DUR, cplay, videoid)
        if DUR == "Unknown"
        else queue_markup(
            _,
            DUR,
            cplay,
            videoid,
            seconds_to_min(got[0]["played"]),
            got[0]["dur"],
        )
    )
    basic[videoid] = True

    med = InputMediaPhoto(media=IMAGE, caption=cap)
    mystic = await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
    if DUR != "Unknown":
        try:
            while db[chat_id][0]["vidid"] == videoid:
                await asyncio.sleep(5)
                if await is_active_chat(chat_id):
                    if basic[videoid]:
                        if await is_music_playing(chat_id):
                            try:
                                buttons = queue_markup(
                                    _,
                                    DUR,
                                    cplay,
                                    videoid,
                                    seconds_to_min(db[chat_id][0]["played"]),
                                    db[chat_id][0]["dur"],
                                )
                                await mystic.edit_reply_markup(reply_markup=buttons)
                            except FloodWait:
                                pass
                        else:
                            pass
                    else:
                        break
                else:
                    break
        except:
            return
