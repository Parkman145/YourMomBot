#Import libraries
import discord
import configparser
import asyncio

#initial setup
config = configparser.ConfigParser()
config.read("config.ini")
with open("token.txt", "r") as f:
    token = f.read()

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
    if message.author == client.user:
        return
    messageUpper = message.content.upper()
    if message.content.upper().startswith('WHO'):
        if message.content.upper().startswith('WHO ASKED'):
            await message.channel.send("https://cdn.discordapp.com/attachments/755649995021090900/1081862969119485952/EY88shMXgAMhVD4.png")
        else:
            await message.channel.send('your mom')

#run bot
client.run(token) 