from pyrogram import Client, enums, filters
import asyncio
from TanuMusic import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.handlers import MessageHandler

#####
BUTTONS = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/TanuMusicxBot?startgroup=true"),
    ],
]

####

@app.on_message(filters.command("dice"))
async def dice(bot, message):
    x=await bot.send_dice(message.chat.id)
    m=x.dice.value
    await message.reply_text(f"⬤ ʜᴇʏ ʙᴀʙʏ ➥ {message.from_user.mention}\n⬤ ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➥ {m}", reply_markup=InlineKeyboardMarkup(BUTTONS) ,quote=True)
  
@app.on_message(filters.command("dart"))
async def dart(bot, message):
    x=await bot.send_dice(message.chat.id, "🎯")
    m=x.dice.value
    await message.reply_text(f"⬤ ʜᴇʏ ʙᴀʙʏ ➥ {message.from_user.mention}\n⬤ ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➥ {m}", reply_markup=InlineKeyboardMarkup(BUTTONS),quote=True)

@app.on_message(filters.command("basket"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🏀")
    m=x.dice.value
    await message.reply_text(f"⬤ ʜᴇʏ ʙᴀʙʏ ➥ {message.from_user.mention}\n⬤ ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➥ {m}",reply_markup=InlineKeyboardMarkup(BUTTONS), quote=True)
@app.on_message(filters.command("jackpot"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🎰")
    m=x.dice.value
    await message.reply_text(f"⬤ ʜᴇʏ ʙᴀʙʏ ➥ {message.from_user.mention}\n⬤ ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➥ {m}",reply_markup=InlineKeyboardMarkup(BUTTONS), quote=True)
@app.on_message(filters.command("ball"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🎳")
    m=x.dice.value
    await message.reply_text(f"⬤ ʜᴇʏ ʙᴀʙʏ ➥ {message.from_user.mention}\n⬤ ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➥ {m}",reply_markup=InlineKeyboardMarkup(BUTTONS), quote=True)
@app.on_message(filters.command("football"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "⚽")
    m=x.dice.value
    await message.reply_text(f"⬤ ʜᴇʏ ʙᴀʙʏ ➥ {message.from_user.mention}\n⬤ ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➥ {m}",reply_markup=InlineKeyboardMarkup(BUTTONS), quote=True)

#####
