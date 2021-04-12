from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message

@Client.on_message(filters.command("muzik",".") & filters.me)
async def muzik(client: Client, message: Message):
    await message.edit_text("Aranıyor...")
    arguman = " ".join(message.command[1:])
    result = await client.get_inline_bot_results("DeezerMusicBot",arguman)
    await message.delete()
    await client.send_inline_bot_result(message.chat.id,result.query_id,result.results[0].id)