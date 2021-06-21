from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Cukup Kirim Url Youtube"
    await message.reply_text(helptxt)
