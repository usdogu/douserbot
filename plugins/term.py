import asyncio
from pyrogram import Client, filters
from pyrogram.methods.decorators import on_disconnect
from pyrogram.types.messages_and_media.message import Message
from io import BytesIO

@Client.on_message(filters.command("term",".")  & filters.me)
async def term(client: Client, message: Message):
    arguman = " ".join(message.command[1:])
    await message.edit_text("Komut Çalıştırılıyor...")
    ps = await asyncio.create_subprocess_shell(arguman,stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await ps.communicate()
    e = stderr.decode("utf-8")
    
    if e:
      await message.edit_text(f"Hata Oluştu:\n{e}")
      return
    o = stdout.decode("utf-8")
    if len(o) > 4096:
        with BytesIO(str.encode(o,encoding="utf-8")) as out_file:
            out_file.name = "exec.text"
            await message.reply_document(
                document=out_file,
                caption=arguman,
                disable_notification=True
            )
    else:
        await message.edit_text(o)