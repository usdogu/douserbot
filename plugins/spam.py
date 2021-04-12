import asyncio
from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message

@Client.on_message(filters.command("spam", ".") & filters.me)
async def spam(client: Client, message: Message):
    await message.delete()
    kac_kere = message.command[1]
    metin = " ".join(message.command[2:])
    for _ in range(int(kac_kere)):
        await client.send_message(message.chat.id,metin)
        await asyncio.sleep(0.20)