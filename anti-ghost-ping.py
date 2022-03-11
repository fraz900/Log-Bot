#fraz900
#01/09/2021
#credit if used
import discord
from discord.ext import commands

TOKEN = "" #log bot token
bot = commands.Bot(command_prefix = "£")

@bot.event
async def on_ready():
    print("ready")
    print(bot.user.name)
    print(bot.user.id)
    print("------")

        
@bot.event
async def on_message_delete(message):
    if "@" in message.content:
        response = f"<@!{message.author.id}> ghost pinged"
        await message.channel.send(response)

@bot.event
async def on_message_edit(before,after):
    if "@" in before.content and "@" not in after.content:
        response = f"<@!{before.author.id}> ghost pinged"
        await before.channel.send(response)

bot.run(TOKEN)




