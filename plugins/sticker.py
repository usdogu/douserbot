import asyncio
from typing import Any
from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
import random

# https://github.com/keyiflerolsun/keyifUserBot/blob/master/Userbot/Eklentiler/stik.py dız
@Client.on_message(filters.command("q", ".") & filters.me)
async def stik(client:Client, message:Message):
    
    yanit_id  = await yanitlanan_mesaj(message)
    ilk_mesaj = await message.edit("__Bekleyin..__", disable_web_page_preview = True)
    #------------------------------------------------------------- Başlangıç >
    cevaplanan_mesaj = message.reply_to_message

    if cevaplanan_mesaj is None:
        await ilk_mesaj.edit("__stikır yapılacak mesajı yanıtlamalısın..__")
        return

    stik_botu = '@QuotLyBot'
    await cevaplanan_mesaj.forward(stik_botu)
    mesaj = await client.get_history(stik_botu, 1)
    await ilk_mesaj.edit("`Stikır yapıyorum`")

    stik_mi = False
    bar = 0
    hata_limit = 0

    while not stik_mi:
        try:
            mesaj = await client.get_history(stik_botu, 1)
            _ = mesaj[0]["sticker"]["file_id"]
            stik_mi = True
        except TypeError:
            await asyncio.sleep(0.5)
            bar += random.randint(0, 10)

            try:
                await ilk_mesaj.edit(f"**Stikır**\n\n`İşleniyor %{bar}`", parse_mode="md")

            except Exception as hata:
                if hata_limit == 3:
                    break

                await ilk_mesaj.edit(f'**Hata Var !**\n\n__{hata}')

                hata_limit += 1

    await ilk_mesaj.edit("`Tamamlandı !`", parse_mode="md")
    stik_id = mesaj[0]["sticker"]["file_id"]
    await message.reply_sticker(stik_id, reply_to_message_id=yanit_id)
    await client.read_history(stik_botu)
    await ilk_mesaj.delete()

async def yanitlanan_mesaj(message:Message) -> Any:
    yanitlanan_id = None

    if message.reply_to_message:
        yanitlanan_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        yanitlanan_id = message.message_id

    return yanitlanan_id