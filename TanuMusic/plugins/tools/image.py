from pyrogram.types import InputMediaPhoto, InputMediaAnimation, InputMediaDocument, InputMediaAudio, InputMediaVideo
from config import BANNED_USERS
from TanuMusic import app
from pyrogram import filters
from TheApi import api

# Handler for image commands
@app.on_message(filters.command(["image", "img", "mg", "mage"], prefixes=["/", "!", "I", "i"]) & ~BANNED_USERS)
async def image_from_bing(_, message):
    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply_text("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

    query = message.reply_to_message.text if message.reply_to_message else " ".join(message.command[1:])
    messagesend = await message.reply_text("**🔍 sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ɪᴍᴀɢᴇs...**")

    media_group = [InputMediaPhoto(media=url) for url in api.bing_image(query, 5)]
    await messagesend.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ...**")
    try:
        await app.send_media_group(message.chat.id, media_group)
        await messagesend.delete()
    except Exception as e:
        await messagesend.edit(str(e))

# Handler for animation commands
@app.on_message(filters.command(["animation", "ani", "ni"], prefixes=["/", "!", "A", "a"]) & ~BANNED_USERS)
async def animation_from_bing(_, message):
    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply_text("**ɢɪᴠᴇ ᴀɴɪᴍᴀᴛɪᴏɴ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

    query = message.reply_to_message.text if message.reply_to_message else " ".join(message.command[1:])
    messagesend = await message.reply_text("**🔍 sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ᴀɴɪᴍᴀᴛɪᴏɴs...**")

    media_group = [InputMediaAnimation(media=url) for url in api.bing_animation(query, 5)]
    await messagesend.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ...**")
    try:
        await app.send_media_group(message.chat.id, media_group)
        await messagesend.delete()
    except Exception as e:
        await messagesend.edit(str(e))

# Handler for document commands
@app.on_message(filters.command(["document", "oc", "doc"], prefixes=["/", "!", "D", "d"]) & ~BANNED_USERS)
async def document_from_bing(_, message):
    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply_text("**ɢɪᴠᴇ ᴅᴏᴄᴜᴍᴇɴᴛ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

    query = message.reply_to_message.text if message.reply_to_message else " ".join(message.command[1:])
    messagesend = await message.reply_text("**🔍 sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ᴅᴏᴄᴜᴍᴇɴᴛs...**")

    media_group = [InputMediaDocument(media=url) for url in api.bing_document(query, 5)]
    await messagesend.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ...**")
    try:
        await app.send_media_group(message.chat.id, media_group)
        await messagesend.delete()
    except Exception as e:
        await messagesend.edit(str(e))

# Handler for audio commands
@app.on_message(filters.command(["audio", "sound", "ud", "udio"], prefixes=["/", "!", "a", "A"]) & ~BANNED_USERS)
async def audio_from_bing(_, message):
    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply_text("**ɢɪᴠᴇ ᴀᴜᴅɪᴏ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

    query = message.reply_to_message.text if message.reply_to_message else " ".join(message.command[1:])
    messagesend = await message.reply_text("**🔍 sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ᴀᴜᴅɪᴏs...**")

    media_group = [InputMediaAudio(media=url) for url in api.bing_audio(query, 5)]
    await messagesend.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ...**")
    try:
        await app.send_media_group(message.chat.id, media_group)
        await messagesend.delete()
    except Exception as e:
        await messagesend.edit(str(e))

# Handler for video commands
@app.on_message(filters.command(["video", "id"], prefixes=["/", "!", "V", "v"]) & ~BANNED_USERS)
async def video_from_bing(_, message):
    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply_text("**ɢɪᴠᴇ ᴠɪᴅᴇᴏ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

    query = message.reply_to_message.text if message.reply_to_message else " ".join(message.command[1:])
    messagesend = await message.reply_text("**🔍 sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ᴠɪᴅᴇᴏs...**")

    media_group = [InputMediaVideo(media=url) for url in api.bing_video(query, 5)]
    await messagesend.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ...**")
    try:
        await app.send_media_group(message.chat.id, media_group)
        await messagesend.delete()
    except Exception as e:
        await messagesend.edit(str(e))

__MODULE__ = "Mᴇᴅɪᴀ"
__HELP__ = """
**Media Commands**

* `/image` or `/img` or `/mg` or `/mage` : Search for images on Bing.
* `/animation` or `/ani` : Search for animations on Bing.
* `/document` or `/doc` : Search for documents on Bing.
* `/audio` or `/sound` : Search for audio files on Bing.
* `/video` or `vid` : Search for videos on Bing.

**Usage**

* Send a message with the command and the search query.
* Reply to a message with the command to search for the text in the replied message.
"""
