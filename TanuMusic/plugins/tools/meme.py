from pyrogram import Client, filters
import requests
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message 
from TanuMusic import app 


BUTTONS1 = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/TanuMusicxBot?startgroup=true"),
    ],
]


# Define a command handler for the /meme command
@app.on_message(filters.command("meme"))
def meme_command(client, message):
    # API endpoint for random memes
    api_url = "https://meme-api.com/gimme"

    try:
        # Make a request to the API
        response = requests.get(api_url)
        data = response.json()

        # Extract the meme image URL
        meme_url = data.get("url")
        title = data.get("title")

        # Mention the bot username in the caption
        caption = f"❖ {title}\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥  ˹ ᴛᴀɴᴜ ꭙ ᴍᴜsɪᴄ™ ♡゙"

        # Send the meme image to the user with the modified caption
        message.reply_photo(
            photo=meme_url, caption=caption,reply_markup=InlineKeyboardMarkup(BUTTONS1),)

    except Exception as e:
        print(f"✦ Error fetching meme ➠ {e}")
        message.reply_text("✦ Sorry, I couldn't fetch a meme at the moment.")
      
