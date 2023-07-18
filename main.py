#Import libraries
import asyncio
import discord
from discord.ext import commands, tasks
from discord import app_commands
import datetime
import configparser
import random
import json
import os
from shutil import copy
from datetime import date
from Functions import *

# setup config
if not os.path.exists("config.json"):
    
    copy("defaultconfig.json", "config.json")

# initial setup
tokens = configparser.ConfigParser()
tokens.read("tokens.ini")
discord_token = tokens.get("tokens", "discord")
tenor_token = tokens.get("tokens", "tenor")
openai_token = tokens.get("tokens", "openai")
with open("config.json") as f:
    config = json.load(f)
    
#bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
async def broadcastWOTD():
    wotd = getRandomWord()
    for channel_id in config["globalConfig"]["wotdBroadcastChannels"]:
        channel = await bot.fetch_channel(channel_id)
        definition = getDefinition(wotd)
        await channel.send(definition)





# If no tzinfo is given then UTC is assumed.
time = datetime.time(hour=config["globalConfig"]["wotdTime"][0], minute=config["globalConfig"]["wotdTime"][1])


# @bot.tree.command(name = "getuserpfp")
# async def getuserpfp(interaction: discord.Interaction):
#     await interaction.response.send_message("Hello!")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'We have logged in as {bot.user}')
    await bot.add_cog(scheduler(bot))
    
@bot.event
async def on_message(message):
    #End if author is bot
    if message.author == bot.user:
        return
    
    #Han Ban
    if message.channel.id in config["globalConfig"]["hanChannel"] and message.content !=  "https://tenor.com/view/jisung-han-jisung-stray-kids-skz-skz-jisung-gif-19153372":
        await message.guild.kick(message.author, reason="not that one han gif")

    #Random chimp event
    if  random.random() < config["globalConfig"]["chimpChance"]:
        await message.channel.send("RANDOM CHIMP EVENT!!!!!")
        await message.channel.send(getRandomTenor(tenor_token, "chimp"))
        return
    #Shay bullying
    if message.author.id == 708507641034440714:
        if random.random() < config["globalConfig"]["bullyChance"]:
            await message.channel.send("HOLY SHIT SHAY JUST SHUT THE FUCK UP PLEASE NO ONE IS TALKING TO YOU")
            return
        
    #Your mom and It's me, I asked responses
    messageUpper = message.content.upper()
    if message.content.upper().startswith('WHO'):
        if message.content.upper().startswith('WHO ASKED'):
            await message.channel.send("https://cdn.discordapp.com/attachments/755649995021090900/1081862969119485952/EY88shMXgAMhVD4.png")
        else:
            await message.channel.send('your mom')

class scheduler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.broadcastWOTD.start()

    def cog_unload(self):
        self.broadcastWOTD.cancel()

    @tasks.loop(time=time)
    async def broadcastWOTD(self):
        if date.today().isoformat() in config["globalConfig"]["birthdays"].keys():
            for birthday in config["globalConfig"]["birthdays"][date.today().isoformat()]:
                person = birthday["person"]
                channel_id = birthday["channel"]
                channel = await bot.fetch_channel(channel_id)
                birthdaygif = getRandomTenor(tenor_token, "birthday")
                await channel.send(f"Happy birthday {person}!!!!!")
                await channel.send(birthdaygif)

        
        wotd = getDefinition(openai_token, getRandomWord())
        for channel_id in config["globalConfig"]["wotdBroadcastChannels"]:
            channel = await bot.fetch_channel(channel_id)
            await channel.send(wotd)
    



#run bot
bot.run(discord_token) 