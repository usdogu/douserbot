from KekikSpatula import Covid
from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message

@Client.on_message(filters.command("covid",".") & filters.me)
async def covid(client: Client,message: Message):
    covid_data = Covid()
    gunluk_vefat = covid_data.nesne.gunluk_vefat
    gunluk_vaka = covid_data.nesne.gunluk_vaka
    gunluk_test = covid_data.nesne.gunluk_test
    gunluk_iyilesen = covid_data.nesne.gunluk_iyilesen
    toplam_vefat = covid_data.nesne.toplam_vefat
    toplam_vaka = covid_data.nesne.toplam_vaka
    toplam_test = covid_data.nesne.toplam_test
    toplam_iyilesen = covid_data.nesne.toplam_iyilesen
    await message.edit_text(f"**Günlük Veri:\n**Test : {gunluk_test}\nVaka : {gunluk_vaka}\nVefat : {gunluk_vefat}\nİyileşen : {gunluk_iyilesen}\n**Toplam Veri**\nTest : {toplam_test}\nVaka : {toplam_vaka}\nVefat : {toplam_vefat}\nİyileşen : {toplam_iyilesen}**")