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
        print ('loggedin as {0}'.format.self(user))
       
    async def on_message(self, message):
        print ('message from {0.author}: {0.message}'.format(message))

client = MyClient()
client.run (TOKEN)
    
#client = discord.Client()

#@client.event
#async def on_message(message):
    # we do not want the bot to reply to itself
#    if message.author == client.user:
#        return

#    if message.content.startswith('!hello'):
#        msg = 'Hello {0.author.mention}'.format(message)
#        await client.send_message(message.channel, msg)
#
#@client.event
#async def on_ready():
#    print('Logged in as')
#    print(client.user.name)
#    print(client.user.id)
#    print('------')
#
#client.run(TOKEN)
