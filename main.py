#Import libraries
import discord
import configparser
import asyncio
import random
import configparser

from Functions import getRandomTenor

#initial setup
config = configparser.ConfigParser()
config.read("config.ini")
tokens = configparser.ConfigParser()
tokens.read("tokens.ini")
discord_token = tokens.get("tokens", "discord")
tenor_token = tokens.get("tokens", "tenor")

#bot setup
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    # print(client.fetch_user(299736315505803264))
@client.event
async def on_message(message):
    #End if author is bot
    if message.author == client.user:
        return
    
    #Random chimp event
    if random.randint(1, 15) == 1:
        await message.channel.send("RANDOM CHIMP EVENT!!!!!")
        await message.channel.send(getRandomTenor(tenor_token, "chimp"))
        return
    #Shay bullying
    if message.author.id == 708507641034440714:
        if random.randint(1, 100) == 1:
            message.channel.send("HOLY SHIT SHAY JUST SHUT THE FUCK UP PLEASE NO ONE IS TALKING TO YOU")
            return
        
    #Your mom and It's me, I asked responses
    messageUpper = message.content.upper()
    if message.content.upper().startswith('WHO'):
        if message.content.upper().startswith('WHO ASKED'):
            await message.channel.send("RAhttps://cdn.discordapp.com/attachments/755649995021090900/1081862969119485952/EY88shMXgAMhVD4.png")
        else:
            await message.channel.send('your mom')

#run bot
client.run(discord_token) 