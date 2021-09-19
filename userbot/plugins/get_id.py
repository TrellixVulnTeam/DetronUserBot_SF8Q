"""Get ID of any Telegram media, or any user
Syntax: .get_id"""
from telethon import events
from telethon.utils import pack_bot_file_id
from DETRONBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
CmdHelp("get_id").add_command(
    "get_id", None, "Get id of any group / channel / any user"
).add()

@bot.on(admin_cmd("get_id"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        chat = await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await event.edit("Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(str(event.chat_id), str(r_msg.sender_id), bot_api_file_id))
        else:
            await event.edit("Current Chat ID: `{}`\nFrom User ID: `{}`".format(str(event.chat_id), str(r_msg.sender_id)))
    else:
        await event.edit("Current Chat ID: `{}`".format(str(event.chat_id)))
