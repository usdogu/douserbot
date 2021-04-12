from pyrogram import Client
from os import environ

string_session = environ.get("STRING_SESSSION")
Client(string_session,plugins=dict(root="plugins")).run()