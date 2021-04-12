from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
import aiohttp
@Client.on_message(filters.command("paste", ".") & filters.me)
async def paste(_, message: Message):
    text = None
    if not message.reply_to_message:
        text = " ".join(message.command[1:])
    else:
        text = message.reply_to_message.text
    await message.edit_text("İstek Atılıyor....")
    async with aiohttp.ClientSession() as sess:
        async with sess.post("https://nekobin.com/api/documents", json={"content": text},timeout= 3) as resp:
            key = (await resp.json())["result"]["key"]
    await message.edit_text(f"https://nekobin.com/{key}")