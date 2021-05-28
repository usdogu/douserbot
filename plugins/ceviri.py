from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
from googletrans import Translator
@Client.on_message(filters.command("cevir",".") & filters.me)
async def cevir(client: Client,message: Message):
    translator = Translator()
    text = None
    if not message.reply_to_message:
        text = " ".join(message.command[1:])
    else:
        text = message.reply_to_message.text
    await message.edit_text(translator.translate(text,dest="tr").text)