import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOG_GROUP_ID
from TanuMusic import app  

IMG = [
"https://graph.org/file/f76fd86d1936d45a63c64.jpg",
"https://graph.org/file/69ba894371860cd22d92e.jpg",
"https://graph.org/file/67fde88d8c3aa8327d363.jpg",
"https://graph.org/file/3a400f1f32fc381913061.jpg",
"https://graph.org/file/a0893f3a1e6777f6de821.jpg",
"https://graph.org/file/5a285fc0124657c7b7a0b.jpg",
"https://graph.org/file/25e215c4602b241b66829.jpg",
"https://graph.org/file/a13e9733afdad69720d67.jpg",
"https://graph.org/file/692e89f8fe20554e7a139.jpg",
"https://graph.org/file/db277a7810a3f65d92f22.jpg",
"https://graph.org/file/a00f89c5aa75735896e0f.jpg",
"https://graph.org/file/f86b71018196c5cfe7344.jpg",
"https://graph.org/file/a3db9af88f25bb1b99325.jpg",
"https://graph.org/file/5b344a55f3d5199b63fa5.jpg",
"https://graph.org/file/84de4b440300297a8ecb3.jpg",
"https://graph.org/file/84e84ff778b045879d24f.jpg",
"https://graph.org/file/a4a8f0e5c0e6b18249ffc.jpg",
"https://graph.org/file/ed92cada78099c9c3a4f7.jpg",
"https://graph.org/file/d6360613d0fa7a9d2f90b.jpg",
"https://graph.org/file/37248e7bdff70c662a702.jpg",
"https://graph.org/file/0bfe29d15e918917d1305.jpg",
"https://graph.org/file/16b1a2828cc507f8048bd.jpg",
"https://graph.org/file/e6b01f23f2871e128dad8.jpg",
"https://graph.org/file/cacbdddee77784d9ed2b7.jpg",
"https://graph.org/file/ddc5d6ec1c33276507b19.jpg",
"https://graph.org/file/39d7277189360d2c85b62.jpg",
"https://graph.org/file/5846b9214eaf12c3ed100.jpg",
"https://graph.org/file/ad4f9beb4d526e6615e18.jpg",
"https://graph.org/file/3514efaabe774e4f181f2.jpg",   

]

Tanu = [
    "https://graph.org/file/9bba2b7ee9ba3806de65d.jpg",
    "https://graph.org/file/ef82f289043a4fa74f8ff.jpg",
    "https://graph.org/file/9c27c68958e06ae074c38.jpg",
    "https://graph.org/file/0ff325b1d2efe80299aa3.jpg",
    "https://graph.org/file/41167b953cf3579853d47.jpg",
    "https://graph.org/file/bd93ab42e69305f274028.jpg",
    "https://graph.org/file/97575db5586c05d6b2898.jpg",
    "https://graph.org/file/07c393fdf931a407c9bc0.jpg",
    "https://graph.org/file/f332767490ad3a5ca20e8.jpg",
    "https://graph.org/file/f3449e9069667f647d14e.jpg",
    "https://graph.org/file/9f51cdc739f907cbd2c7e.jpg",
    "https://telegra.ph/file/d7a6a923c38e051ce35f3.jpg",
    "https://graph.org/file/f86b71018196c5cfe7344.jpg",
    "https://graph.org/file/a3db9af88f25bb1b99325.jpg",
    "https://graph.org/file/5b344a55f3d5199b63fa5.jpg",
    "https://graph.org/file/84de4b440300297a8ecb3.jpg",
    "https://graph.org/file/84e84ff778b045879d24f.jpg",
    "https://graph.org/file/a4a8f0e5c0e6b18249ffc.jpg",
    "https://graph.org/file/ed92cada78099c9c3a4f7.jpg",
    "https://graph.org/file/d6360613d0fa7a9d2f90b.jpg",
    "https://graph.org/file/37248e7bdff70c662a702.jpg",
    "https://graph.org/file/0bfe29d15e918917d1305.jpg",
    "https://graph.org/file/16b1a2828cc507f8048bd.jpg",
    "https://graph.org/file/e6b01f23f2871e128dad8.jpg",
    "https://graph.org/file/cacbdddee77784d9ed2b7.jpg",
    "https://graph.org/file/ddc5d6ec1c33276507b19.jpg",
    "https://graph.org/file/39d7277189360d2c85b62.jpg",
    "https://graph.org/file/5846b9214eaf12c3ed100.jpg",
    "https://graph.org/file/ad4f9beb4d526e6615e18.jpg",
    "https://graph.org/file/3514efaabe774e4f181f2.jpg",    
]



@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"❖ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #ɴᴇᴡ_ɢʀᴏᴜᴘ ❖\n\n"
               
                f"● ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➥ {message.chat.title}\n"
                f"● ɢʀᴏᴜᴘ ɪᴅ ➥ {message.chat.id}\n"
                f"● ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➥ @{message.chat.username}\n"
                f"● ɢʀᴏᴜᴘ ʟɪɴᴋ ➥ {link}\n"
                f"● ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ➥ {count}\n\n"
                f"❖ ᴀᴅᴅᴇᴅ ʙʏ ➥ {message.from_user.mention}"
            )
            await app.send_photo(LOGGER_ID, photo=random.choice(IMG), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"sᴇᴇ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɢʀᴏᴜᴘ", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"❖ <b>ʙᴏᴛ #ʟᴇғᴛ_ɢʀᴏᴜᴘ ʙʏ ᴀ ᴄʜᴜᴛɪʏᴀ</b> ❖\n\n● ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➥ {title}\n\n● ɢʀᴏᴜᴘ ɪᴅ ➥ {chat_id}\n\n● ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ➥ {remove_by}\n\n❖ ʙᴏᴛ ɴᴀᴍᴇ ➥  ˹ ᴛᴀɴᴜ ꭙ ᴍᴜsɪᴄ™ ♡゙"
        await app.send_photo(LOGGER_ID, photo=random.choice(Tanu), caption=left, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))

#welcome

