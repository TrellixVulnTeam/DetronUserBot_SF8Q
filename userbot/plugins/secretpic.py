from . import *

@bot.on(admin_cmd(pattern="spic"))
async def oho(event):
  if not event.is_reply:
    return await event.edit('Reply to a self distructing pic !.!.!')
  k = await event.get_reply_message()
  pic = await k.download_media()
  await bot.send_file(event.chat_id, pic, caption=f"""
  OwO!! LoL, Destruction Mode Pic Destroyed!!
  Pic captured By ᏞᎬᏀᎬΝᎠᏴϴͲ
🌚🌝
  """)
  await event.delete()
  
CmdHelp("∂ιѕτя ριϲ").add_command(
  "spic", "This Command Can Capture The Self Destruction Picturr"
).add_info(
  "Capture 🤫 Pic."
).add_warning(
  "✅ Harmless Module."
).add()
