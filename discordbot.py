from discord.ext import commands
from googletrans import Translator
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
translator = Translator()


@bot.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)
    text_channels.send("Translator is Enabled! | 翻訳機能が有効になりました！")

async def on_message(message):
    if translator.detect(message) == (lang = en, confidence > 0.9):
        await  message.channel.send(translator.translate(message,src='en', dest='jp'))
    elif translator.detect(message) == (lang=jp, confidence > 0.9):
        await  message.channel.send(translator.translate(message,src='jp', dest='en'))
    else:
        await  message.channel.send("please talk in English or Japanese")

@bot.command()


bot.run(token)
