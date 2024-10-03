from TanuMusic import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from gtts import gTTS
import os
import hashlib
import json
from datetime import datetime

# Cache for storing generated audio files
audio_cache = {}

# Stats for tracking usage
usage_stats = {
    "total_requests": 0,
    "language_usage": {},
}

# Load stats from file if it exists
if os.path.exists("tts_stats.json"):
    with open("tts_stats.json", "r") as f:
        usage_stats = json.load(f)

# Available languages in gTTS
available_languages = ['af', 'ar', 'bg', 'bn', 'bs', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 'et', 'fi', 'fr',
                       'gu', 'hi', 'hr', 'hu', 'id', 'is', 'it', 'ja', 'jw', 'km', 'kn', 'ko', 'la', 'lv', 'ml',
                       'mr', 'my', 'ne', 'nl', 'no', 'pl', 'pt', 'ro', 'ru', 'si', 'sk', 'sq', 'sr', 'su', 'sv',
                       'sw', 'ta', 'te', 'th', 'tl', 'tr', 'uk', 'ur', 'vi', 'zh-CN', 'zh-TW']

@app.on_message(filters.command(["tts", "ts"], prefixes=["/", "!", ".", "T", "t"]))
async def tts(client, message):
    if len(message.command) > 1:
        # If text is provided with the command
        text = ' '.join(message.command[1:])
        await process_tts(message, text=text)
    elif message.reply_to_message and message.reply_to_message.text:
        # If replying to a message
        await process_tts(message, text=message.reply_to_message.text)
    else:
        # If no text is provided, show language options
        keyboard = []
        for i in range(0, len(available_languages), 2):
            row = [InlineKeyboardButton(lang, callback_data=f"tts_{lang}") for lang in available_languages[i:i+2]]
            keyboard.append(row)
        markup = InlineKeyboardMarkup(keyboard)
        await message.reply_text("Choose a language, or provide text after the command:", reply_markup=markup)

@app.on_callback_query(filters.regex("^tts_"))
async def tts_callback(client, callback_query):
    lang = callback_query.data.split("_")[1]
    await callback_query.message.reply_text(f"Selected language: {lang}. Now, please provide the text you want to convert to speech.")
    await callback_query.answer()

async def process_tts(message, lang="en", text=None):
    global usage_stats

    if not text:
        await message.reply_text("Please provide text or reply to a message.")
        return

    # Update usage stats
    usage_stats["total_requests"] += 1
    usage_stats["language_usage"][lang] = usage_stats["language_usage"].get(lang, 0) + 1

    # Save stats to file
    with open("tts_stats.json", "w") as f:
        json.dump(usage_stats, f)

    # Generate a unique hash for this text and language combination
    text_hash = hashlib.md5((text + lang).encode()).hexdigest()

    if text_hash in audio_cache:
        audio_file = audio_cache[text_hash]
    else:
        tts = gTTS(text=text, lang=lang)
        audio_file = f"output_{text_hash}.mp3"
        tts.save(audio_file)
        audio_cache[text_hash] = audio_file

    try:
        await message.reply_voice(audio_file)
    except Exception as e:
        await message.reply_text(f"Error sending voice message: {str(e)}")

    # Clean up old cache files
    current_time = datetime.now()
    for file in os.listdir():
        if file.startswith("output_") and file.endswith(".mp3"):
            file_creation_time = datetime.fromtimestamp(os.path.getctime(file))
            if (current_time - file_creation_time).days > 1:  # Delete files older than 1 day
                os.remove(file)
                if file in audio_cache.values():
                    del audio_cache[list(audio_cache.keys())[list(audio_cache.values()).index(file)]]

@app.on_message(filters.command(["tts_stats", "tss"], prefixes=["/", "!", ".", "T", "t"]))
async def tts_stats(client, message):
    stats_message = f"Total TTS requests: {usage_stats['total_requests']}\n\n"
    stats_message += "Language usage:\n"
    for lang, count in usage_stats['language_usage'].items():
        stats_message += f"{lang}: {count}\n"

    await message.reply_text(stats_message)
