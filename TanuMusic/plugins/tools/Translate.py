from TanuMusic import app
from pyrogram import filters
from deep_translator import GoogleTranslator, exceptions

@app.on_message(filters.command(["tr", "r"], prefixes=["/", "!","t", "T"]))
async def translate(client, message):
    try:
        if message.reply_to_message:
            text_to_translate = message.reply_to_message.text
            target_language = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else 'en'
        else:
            if len(message.text.split()) < 3:
                await message.reply_text("Kripya kisi sandesh ka jawab dein ya /tr ke baad bhasha code (jaise hi for hindi, en for english) aur anuvad karne ke liye text dein.")
                return
            target_language = message.text.split(None, 2)[1]
            text_to_translate = message.text.split(None, 2)[2]

        if not text_to_translate:
            await message.reply_text("Anuvad karne ke liye koi text nahi mila.")
            return

        translated = GoogleTranslator(source='auto', target=target_language).translate(text_to_translate)
        
        if translated == text_to_translate:
            await message.reply_text(f"Anuvad nahi kiya gaya. Kya aap sahi bhasha code ka upyog kar rahe hain?\nMool text: {text_to_translate}")
        else:
            await message.reply_text(f"Anuvad: {translated}\nBhasha: {target_language}")

    except exceptions.LanguageNotSupportedException:
        await message.reply_text(f"Bhasha code '{target_language}' manya nahi hai. Kripya sahi bhasha code ka prayog karein.")
    except exceptions.TranslationNotFound:
        await message.reply_text("Anuvad nahi mil saka. Kripya phir se koshish karein.")
    except Exception as e:
        await message.reply_text(f"Anuvad karne mein samasya hui: {str(e)}")
