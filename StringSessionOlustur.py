import asyncio
from pyrogram import Client
from os import environ
# https://github.com/keyiflerolsun/keyifUserBot/ dan dızlanıp editlenmiştir

API_ID = input("API ID : ").strip()
API_HASH = input("API HASH : ").strip()
async def session_olustur(api_id, api_hash):
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        print('\n\n')
        print(await app.export_session_string())
        print('\n')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(session_olustur(API_ID, API_HASH))