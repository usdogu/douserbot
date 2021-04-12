from pyrogram import Client
import ini
ini_file = ini.parse(open("config.ini").read())
Client(ini_file["pyrogram"]["string_session"],plugins=dict(root="plugins")).run()