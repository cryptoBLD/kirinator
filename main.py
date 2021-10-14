import discord
from discord.ext import commands

discord_token = open('token.txt')
token = discord_token.read()
discord_token.close()
bot = commands.Bot(command_prefix=".", case_insensitive=True)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('fixing kiri\'s links'))
    print("Bot Ready!")


@bot.event
async def on_message(message):
    kiri = 410485543449919501
    if message.author.id == kiri:
        if message.content[:13] == 'https://media':
            await message.delete()
            b = message.content.split('.')
            a = b[0][:8] + 'cdn.discordapp.com' + b[2][3:] + "." + b[3]
            await message.channel.send(a)

bot.run(token)
