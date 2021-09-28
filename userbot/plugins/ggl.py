
from telethon import events
import os
import requests
import json
from ULTRONBOT.utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd("ggl (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://lmgtfy.com/?q={}%26iie=1".format(input_str.replace(" ","+"))
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("[{}]({})\n`Thank me Later 🙃` ".format(input_str,response_api.rstrip()))
    else:
        await event.edit("something is wrong. please try again later.")


from userbot.cmdhelp import CmdHelp
CmdHelp("google").add_command(
       'ggl', None, '.ggl search query'
).add()
