import asyncio
from userbot.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from . import *
@bot.on(admin_cmd(pattern="byeall"))
async def _(event):
	await event.edit("Guys I Gotta Go!")
	await asyncio.sleep(1)
	await event.edit("""
	
┏━━┳┓╋╋┏┳━━━┓
┃┏┓┃┗┓┏┛┃┏━━┛
┃┗┛┗┓┗┛┏┫┗━━┓
┃┏━┓┣┓┏┛┃┏━━┛
┃┗━┛┃┃┃╋┃┗━━┓
┗━━━┛┗┛╋┗━━━┛
""")
CmdHelp("bye").add_command(
	'byeall', None, 'Say Bye to U all in anmation'
).add()
