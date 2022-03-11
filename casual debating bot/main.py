#fraz900
#01/09/2021
#credit if used
import discord
from discord.ext import commands
import os
from datetime import datetime
TOKEN = os.environ["BOT_TOKEN"]
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


@bot.event
async def on_message(ctx):
    if not ctx.author.guild_permissions.administrator:
        channel = bot.get_channel(951922587674488862)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"ctx.author.mention}\n{ctx.content} \n{current_time}")
bot.run(TOKEN)




