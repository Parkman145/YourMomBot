# bot.py
import os

import discord
import asyncio
from dotenv import load_dotenv , find_dotenv
import aiohttp
load_dotenv(find_dotenv())
filename = find_dotenv('DISCORD_TOKEN.env', raise_error_if_not_found=True)
load_dotenv (filename)
print (filename)
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
#class discord
#aiohttp.request('http', 'https://discord.com/api')
CONNECTION = aiohttp.BaseConnector()

discord.Client(connect)
#ws = discord.()
print (DISCORD_TOKEN)
discord.gateway
    

#discord.gateway.DiscordWebSocket.identify(DISCORD_TOKEN)#
#print (getattr(discord,), getattr(DiscordWebSocket,token))
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(DISCORD_TOKEN)