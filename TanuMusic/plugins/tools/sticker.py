from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from TanuMusic import app
from uuid import uuid4
import pyrogram


BUTTONS = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url="https://t.me/TanuMusicxBot?startgroup=true"),
    ],
]


@app.on_message(filters.command("kang"))
async def _packkang(app, message):  
    txt = await message.reply_text("✦ ᴘʀᴏᴄᴇssɪɴɢ....")
    if not message.reply_to_message:
        await txt.edit("ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ.")
        return
    if not message.reply_to_message.sticker:
        await txt.edit("ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ.")
        return
    if message.reply_to_message.sticker.is_animated or message.reply_to_message.sticker.is_video:
        return await txt.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ɴᴏɴ-ᴀɴɪᴍᴀᴛᴇᴅ sᴛɪᴄᴋᴇʀ.")
    
    pack_name = (
        f"{message.from_user.first_name}_sticker_pack_by_@TanuMusicxBot"
        if len(message.command) < 2 else message.text.split(maxsplit=1)[1]
    )
    
    short_name = message.reply_to_message.sticker.set_name
    stickers = await app.invoke(
        pyrogram.raw.functions.messages.GetStickerSet(
            stickerset=pyrogram.raw.types.InputStickerSetShortName(short_name=short_name),
            hash=0
        )
    )
    sticks = [
        pyrogram.raw.types.InputStickerSetItem(
            document=pyrogram.raw.types.InputDocument(
                id=i.id, access_hash=i.access_hash, file_reference=i.thumbs[0].bytes
            ),
            emoji=i.attributes[1].alt
        )
        for i in stickers.documents
    ]

    try:
        short_name = f"sticker_pack_{str(uuid4()).replace('-', '')}_by_{app.me.username}"
        user_id = await app.resolve_peer(message.from_user.id)
        await app.invoke(
            pyrogram.raw.functions.stickers.CreateStickerSet(
                user_id=user_id,
                title=pack_name,
                short_name=short_name,
                stickers=sticks,
            )
        )
        await txt.edit(
            f"❖ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴋᴀɴɢᴇᴅ ʟɪɴᴋ !\n● ᴛᴏᴛᴀʟ sᴛɪᴄᴋᴇʀ ➥ {len(sticks)}",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ᴘᴀᴄᴋ ʟɪɴᴋ", url=f"http://t.me/addstickers/{short_name}")]]
            )
        )
    except Exception as e:
        await message.reply(str(e))


@app.on_message(filters.command(["stickerid", "stid"]))
async def sticker_id(app, msg):
    if not msg.reply_to_message or not msg.reply_to_message.sticker:
        await msg.reply_text("✦ Reply to a sticker.")
        return
    
    st_in = msg.reply_to_message.sticker
    await msg.reply_text(
        f"""
❖ sᴛɪᴄᴋᴇʀ ɪɴғᴏ ❖

● sᴛɪᴄᴋᴇʀ ɪᴅ ➥ {st_in.file_id}\n
● sᴛɪᴄᴋᴇʀ ᴜɴɪǫᴜᴇ ɪᴅ ➥ {st_in.file_unique_id}
        """, 
        reply_markup=InlineKeyboardMarkup(BUTTONS),
    )
