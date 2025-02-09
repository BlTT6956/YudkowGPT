from pyrogram import Client, filters
from config import settings

bot = Client(settings.name, settings.BOT_ID, settings.BOT_HASH)

@bot.on_message()
async def handler(client, message):
    print(message)

