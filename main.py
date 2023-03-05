#Import libraries
import discord
import configparser
import asyncio

#initial setup
config = configparser.ConfigParser()
config.read("config.ini")
token = config.get("main","token")

#bot setup
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('who'):
        await message.channel.send('your mom')

#run bot
client.run(token)