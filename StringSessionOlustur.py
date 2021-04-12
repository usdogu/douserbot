import asyncio
from pyrogram import Client
import ini
# https://github.com/keyiflerolsun/keyifUserBot/ dan dızlanıp editlenmiştir
ini_file = ini.parse(open("config.ini").read())
API_ID   = ini_file["pyrogram"]["api_id"]
API_HASH = ini_file["pyrogram"]["api_hash"]

async def session_olustur(api_id, api_hash):
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        print('\n\n')
        print(await app.export_session_string())
        print('\n')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(session_olustur(API_ID, API_HASH))