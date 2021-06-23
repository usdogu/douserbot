#!/usr/bin/env python3
from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
import urllib.parse

@Client.on_message(filters.command("google",".") & filters.me)
async def google(client: Client, message: Message):
    text = None
    if not message.reply_to_message:
        text = " ".join(message.command[1:])
    else:
        text = message.reply_to_message.text
    url_encoded_text = urllib.parse.quote_plus(text)
    url = f"https://www.google.com/search?q={url_encoded_text}"
    await message.edit(url)

@Client.on_message(filters.command("gg",".") & filters.me)
async def gg(client: Client, message: Message):
    text = None
    if not message.reply_to_message:
        text = " ".join(message.command[1:])
    else:
        text = message.reply_to_message.text
    url_encoded_text = urllib.parse.quote_plus(text)
    url = f"https://lmgtfy.app/?q={url_encoded_text}"
    await message.edit(url)
