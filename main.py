from pyrogram import Client
import os

string_session = os.getenv("STRING_SESSION")
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
Client(string_session,api_id,api_hash, plugins=dict(root="plugins")).run()
