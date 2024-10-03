import requests
from pyrogram import Client, filters
from TanuMusic import app

@app.on_message(filters.command("gemini"))
async def gemini(client, message):
    user_message = message.text[len("/gemini "):].strip()
    if not user_message:
        await message.reply_text("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴘʀᴏᴍᴘᴛ ᴀғᴛᴇʀ ᴛʜᴇ /gemini ᴄᴏᴍᴍᴀɴᴅ.")
        return
    try:
        response = requests.get(f"https://gemini.apiitzasuraa.workers.dev/?prompt={user_message}")
        response.raise_for_status()
        bot_reply = response.json()['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        bot_reply = f"Sorry, I couldn't get a response from the API. Error: {e}"
    await message.reply_text(bot_reply)
