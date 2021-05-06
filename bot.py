import discord
from discord.ext import commands

TOKEN = 'ODM4OTYxNDQyNDY3ODcyNzc4.YJCtuw.uKNmVngm-BNm3KCG3wMYlkzkMQE'

client = commands.Bot(command_prefix = '.')
client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))


client.run(TOKEN)