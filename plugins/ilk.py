from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message

@Client.on_message(filters.command("ping",".") & filters.me)
async def  ping(client:Client,message: Message):
    await message.edit_text("Pong!")