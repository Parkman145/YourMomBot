# Work with Python 3.6
import os
import asyncio
from discord import commands
from dotenv import load_dotenv , find_dotenv
load_dotenv(find_dotenv())
filename = find_dotenv('DISCORD_TOKEN.env', raise_error_if_not_found=True)
load_dotenv (filename)
print (filename)
TOKEN = os.getenv('DISCORD_TOKEN')


import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(TOKEN)
