# Work with Python 3.6
import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv , find_dotenv
load_dotenv(find_dotenv())
filename = find_dotenv('DISCORD_TOKEN.env', raise_error_if_not_found=True)
load_dotenv (filename)
print (filename)
TOKEN = os.getenv('DISCORD_TOKEN')




class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        channel = '755649995021090900'
    '''
        await channel.send('SYSTEM: YOUR MOM BOT HAS SUCSESSFULLY WENT ONLINE')
    '''
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.startswith('say'):
            channel = message.channel
            await channel.send(message.content.replace("say", ""))
        if message.content.startswith('who'):
            if message.content.startswith('who asked'):
                channel = message.channel
                await channel.send('ITS ME. I ASKED.')
            else:


                channel = message.channel
                await channel.send('YOUR MOM LOL!')

client = MyClient()
client.run(TOKEN)