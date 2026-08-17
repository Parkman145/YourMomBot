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

def sanitize(string: str):
    mapping = {"3": "E", "0": "O", "4": "A", "1":"I", " ":""}

    translation_table = str.maketrans(mapping)
    return string.translate(translation_table).upper()

class MessageCounter:
    counts = {}

    @classmethod
    def check(cls, message: discord.Message) -> bool:
        channel = message.channel
        content = message.content
        if channel in cls.counts:
            if cls.counts[channel][0] == content:
                
                cls.counts[message.channel][1] += 1
                if cls.counts[message.channel][1] == 3:
                    return True 
            else: 
                cls.counts[message.channel][0] = content
                cls.counts[message.channel][1] = 1
        else:
            cls.counts[channel] = [content, 1]

        return False

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return
        message_upper = message.content.upper()
        if MessageCounter.check(message):
            await message.channel.send(message.content)
        if message_upper.startswith("WHO ASKED"):
            print("message")
            await message.channel.send("https://cdn.discordapp.com/attachments/755649995021090900/1081862969119485952/EY88shMXgAMhVD4.png")
            return
        if message_upper.startswith("WHO"):
            await message.channel.send("your mom")
            return
        for word in config.bannedWords:
            if word.upper() in sanitize(message_upper):
                await message.author.timeout(datetime.timedelta(minutes=1))
                print("banned")
                break
        if has_nootice(message_upper):
            await message.reply("https://media.discordapp.net/attachments/755649995021090900/1396029947071697009/nooticing.png?ex=690e4774&is=690cf5f4&hm=83b5b6bb1c2ed54beba61eccb3d22f81d19851d1e1dc1fd277628914cd47760b&=&format=webp&quality=lossless&width=1280&height=1056")
        if random_chance(config.animeChance) and anime_detector.check_image(message.author.avatar.url):
            await message.channel.send("STFU anime pfp")
        if random_chance(config.chimpChance):
            await message.channel.send("RANDOM CHIMP EVENT!!!!!")
            await message.channel.send(getRandomTenor(tenor_token, "chimp"))
        if message.author.id == 691144881543970946 and "luke" in message_upper:
            await message.author.timeout(datetime.timedelta(minutes=1))
        if message_upper == "YES" and random_chance(0.2):
            await message.channel.send("no")
        if message_upper == "NO" and random_chance(0.2):
            await message.channel.send("yes")
        if message_upper == "TYPE SHIT":
            await message.channel.send("shit")
    async def on_member_join(self, user: discord.User):
        if user.id == 480093469818355713:
            guild = self.get_guild(1509394634768646224)
            await guild.ban(user)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)
client.run(discord_token)
