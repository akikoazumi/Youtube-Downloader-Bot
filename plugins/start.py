from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/akarida")],
     ])


    welcomed = f"Hai <b>{message.from_user.first_name}</b>\nsaya adalah bot pengunduh video Youtube Cukup kirim tautan video saja"

    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
