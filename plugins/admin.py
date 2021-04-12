from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
from pyrogram.types.user_and_chats.chat_permissions import ChatPermissions
from pyrogram.types.user_and_chats.user import User


@Client.on_message(filters.command("ban", ".") & filters.me)
async def ban(client: Client, message: Message):
    await message.edit_text("Banlanıyor...")
    await client.kick_chat_member(message.chat.id,message.reply_to_message.from_user.id)
    mention = GetUserMentionable(message.reply_to_message.from_user)
    await message.edit_text(f"{mention} Banlandı")


# https://github.com/athphane/userbot/blob/e3c75acb06f2bc4e00f0cfcb0271ae5796aa2a8c/userbot/helpers/PyroHelpers.py#L36
def GetUserMentionable(user: User):
    """ Get mentionable text of a user."""
    if user.username:
        username = "@{}".format(user.username)
    else:
        if user.last_name:
            name_string = "{} {}".format(user.first_name, user.last_name)
        else:
            name_string = "{}".format(user.first_name)

        username = "<a href='tg://user?id={}'>{}</a>".format(user.id, name_string)

    return username

@Client.on_message(filters.command("mute", ".") & filters.me)
async def mute(client: Client, message: Message):
    await message.edit_text("Muteleniyor...")
    await client.restrict_chat_member(message.chat.id,message.reply_to_message.from_user.id,ChatPermissions())