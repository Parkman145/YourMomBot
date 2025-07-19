# This example requires the 'message_content' intent.

import discord
import configparser
import datetime
import json
from Functions import *
from types import SimpleNamespace
import anime_detector

# initial setup
tokens = configparser.ConfigParser()
tokens.read("tokens.ini")
discord_token = tokens.get("tokens", "discord")
tenor_token = tokens.get("tokens", "tenor")

with open("config.json") as f:
    config = f.read()
config = json.loads(config, object_hook=lambda d: SimpleNamespace(**d))

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        message_upper = message.content.upper()
        if message_upper.startswith("WHO ASKED"):
            print("message")
            await message.channel.send("https://cdn.discordapp.com/attachments/755649995021090900/1081862969119485952/EY88shMXgAMhVD4.png")
            return
        if message_upper.startswith("WHO"):
            await message.channel.send("your mom")
            return
        if "JOB" in message_upper or "EMPLOY" in message_upper:
            await message.author.timeout(datetime.timedelta(minutes=1))
        if "NOTICE" in message_upper or "NOTICING" in message_upper or "NOOTICING" in message_upper:
            await message.reply(stickers=[client.get_sticker(1396033094439407666)])
        if random_chance(config.animeChance) and anime_detector.check_image(message.author.avatar.url):
            await message.channel.send("STFU anime pfp")
        if random_chance(config.chimpChance):
            await message.channel.send("RANDOM CHIMP EVENT!!!!!")
            await message.channel.send(getRandomTenor(tenor_token, "chimp"))
            
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(discord_token)