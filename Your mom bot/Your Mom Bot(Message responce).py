# Work with Python 3.6
import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv , find_dotenv
import requests
import wget
import time
import random
import json
load_dotenv(find_dotenv())
filename = find_dotenv('DISCORD_TOKEN.env', raise_error_if_not_found=True)
load_dotenv (filename)
print (filename)
TOKEN = os.getenv('DISCORD_TOKEN')

DAAfilename = find_dotenv('DANCE_ART_ASCII(ENCODED).env', raise_error_if_not_found=True)
load_dotenv (DAAfilename)
DanceF= os.getenv('danceframe')
TEST = 'Content tim'
Dance = TEST.encode(encoding = 'ascii')
print(Dance)
ballactive = "false"
serverdata = {}
cwd = os.getcwd()
print(cwd)
responses_file = open("responses.json", "r")
responses = json.load(responses_file)
print(responses)
#x = 1
#danceframealt = ['⠀⠀⠀⠀⣀⣤⠀⠀⠀⠀⣿⠿⣶⠀⠀⠀⠀⣿⣿⣀⠀⠀⠀⣶⣶⣿⠿⠛⣶⠤⣀⠛⣿⣿⣿⣿⣿⣿⣭⣿⣤⠒⠀⠀⠀⠉⣿⣿⣿⣿⠀⠀⠉⣀⠀⠤⣤⣤⣀⣿⣿⣿⣿⣀⠀⠀⣿⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣭⣶⠉⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣭⣿⣿⣿⠀⣿⣿⣿⠀⠀⠀⣉⣿⣿⠿⠀⠿⣿⣿⠀⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⣤⠀⠀⠀⣀⣿⣿⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⠛⠀⠀⠀⠉⣿⣿⠀⠀⠀⠉⣿⠀⠀⠀⠀⠀⠛⣿⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⣛⠀⠀⠀⠀⠀⠀⠛⠿⠿⠿⠀⠀⠀⠛⠛', '⠀⠀⠀⣀⣶⣀⠀⠀⠀⠒⣛⣭⠀⠀⠀⣀⠿⣿⣶⠀⣤⣿⠤⣭⣿⣿⣤⣿⣿⣿⠛⣿⣿⠀⣀⠀⣀⠤⣿⣿⣶⣤⣒⣛⠉⠀⣀⣿⣿⣿⣿⣭⠉⠀⠀⣭⣿⣿⠿⠿⣿⠀⣶⣿⣿⠛⠀⣿⣿⣤⣿⣿⠉⠤⣿⣿⠿⣿⣿⠛⠀⠿⣿⣿⣿⣿⣤⠀⣿⣿⠿⠀⣿⣿⣶⠀⣿⣿⣶⠀⠀⠛⣿⠀⠿⣿⣿⠀⠀⠀⣉⣿⠀⣿⣿⠀⠶⣶⠿⠛⠀⠉⣿⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⠀⠀⣶⣿⠿', '⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠶⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣿⣿⣿⣿⣿⣿⠀⠀⣀⣶⣤⣤⠿⠶⠿⠿⠿⣿⣿⣿⣉⣿⣿⠿⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣤⣿⣿⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⠿⣛⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠿⠀⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⣿⠀⠀⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠀⣿⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿', '⠀⠀⣀⠀⠿⣿⣿⣀⠀⠉⣿⣿⣀⠀⠀⠛⣿⣭⣀⣀⣤⠀⠀⣿⣿⣿⣿⣿⠛⠿⣶⣀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⣉⣶⠀⠀⠉⣿⣿⣿⣿⣀⠀⠀⣿⠉⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣿⣿⠿⠉⣿⣿⣿⣿⠀⣿⣿⠿⠀⠀⣿⣿⣿⣿⣶⣿⣿⠀⠀⠀⠀⣿⣿⣿⠛⣿⣿⣀⠀⠀⠀⣿⣿⣿⣿⣶⣀⠀⣿⣿⠉⠀⠀⠀⠉⠉⠉⠛⠛⠿⣿⣶⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⣀⣶⣿⠛', '⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣶⣿⣿⣿⣶⣶⣤⣶⣶⠶⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⠿⣿⣿⣿⣿⣿⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣤⣤⣀⣤⠿⠉⠀⠉⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⣿⣿⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠛⠿⣿⣿⣿⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠉⠀⠀⠀⠛⠿⣿⣿⣶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀', '⠀⠀⠀⠀⠀⠀⣤⣶⣶⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⠀⠀⠀⣀⣿⣿⠀⠀⠀⠀⠤⣿⠿⠿⠿', '⠀⠀⠀⠀⣀⠀⠀⣶⣿⠿⠀⠀⠀⣀⠀⣤⣤⠀⣶⣿⠀⠀⠀⠀⣿⣿⣿⠛⠛⠿⣤⣀⣶⣿⣤⣤⣤⣤⣤⣿⣿⣿⣀⣤⣶⣭⣿⣶⣀⠉⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠿⠿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠛⠿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣶⣿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉', '⠀⠀⠀⠀⠀⠀⣶⣿⣶⠀⠀⠀⣤⣤⣤⣿⣿⣿⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⣿⣿⣿⣿⣿⣶⠀⠀⠀⠀⣿⠉⠿⣿⣿⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉', '⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿⠀⠀⠀⠀⠀⠀⣿⠛⠀⠀⠀⠀⠀⠀⣭⣶', '⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛', '⠀⠀⠀⣶⣿⣶⠀⠀⠀⣿⣿⣿⣀⠀⣀⣿⣿⣿⣿⣿⣿⣶⣿⠛⣭⣿⣿⣿⣿⠛⠛⠛⣿⣿⣿⣿⠿⠀⠀⠀⠀⣿⣿⣿⠀⠀⣀⣭⣿⣿⣿⣿⣀⠀⠤⣿⣿⣿⣿⣿⣿⠉⠀⣿⣿⣿⣿⣿⣿⠉⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⠉⠛⣿⣿⣶⣤⠀⠀⠉⠿⣿⣿⣤⠀⠀⣀⣤⣿⣿⣿⠀⠒⠿⠛⠉⠿⣿⠀⠀⠀⠀⠀⣀⣿⣿⠀⠀⠀⠀⣶⠿⠿⠛  ']
print(DanceF)
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        user = client.user
        for guild in client.guilds:
            print(guild.name)
            current_guild = client.get_guild(guild.id)
            for channel in current_guild.text_channels:
                print("\t"+channel.name)
                if current_guild.me.permissions_in(channel).send_messages == True:
                    print("\t \t Can send messages in this channel")
                    await channel.send("Bot is online.")
                    break
#        guilds = await client.fetch_guilds(limit=150).flatten()
#        i = 0
#        for guild in guilds:
#            print(guild.id)
#            i = i +1
#            text_channels = guild.channels
#            print(text_channels)
#            for channel in text_channels:
#                print("Analizing guild: "+guild.id)
#                if channel.permisions_for(client).send_messages == "True":
#                    print("Found Channel in server "+guild.name+".Channel id is "+channel.id)
#                else:
#                    print("Could not find channel with message_send permission in server "+guild.name)
#            if guilds == i:
#                return
#        print("Finished Scanning Servers.")
#        for i in (client.guilds):
#            guild = client.guilds[0]
#            guild_channel = guild[i]
#            print(guild_channel)
#        channel = 755649995021090900
#        await channel.send('SYSTEM: YOUR MOM BOT HAS SUCSESSFULLY WENT ONLINE')
        
#        channel = '755649995021090900'


    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    async def on_message(self, message):
        global ballactive
        server_id = message.guild.id
        server_id_str= str(server_id)
        server_file_name = server_id_str+".txt"
        file_exists = os.path.isfile(server_file_name)
        if file_exists == 0:
            server_file = open(server_file_name, "w")
            json_template_file = open("Server Data JSON Template.txt", "r")
            json_template = json_template_file.read()
            server_file.write(json_template)
        server_file = open(server_id_str+".txt", "r")
#        server_data = server_file.read()
        server_data = json.load(server_file)
        print(server_data)
        if message.author == client.user and ballactive != "true":
            return
        channel = message.channel
        if message.content.startswith('say'):
            await channel.send(message.content.replace("say", ""))
        if message.content.startswith('who '):
            if message.content.startswith('who asked'):
                await channel.send('ITS ME. I ASKED. \n https://cdn.discordapp.com/attachments/755649995021090900/760677714796740608/ME._I_ASKED.jpg')
            else:
                
                await channel.send('YOUR MOM LOL!')
        if message.content == 'test':
#            await channel.send("line 1\n\rline 2")
#            class avatar  (discord.Asset                
#            read(message.author.avatar_url)
#            global x
#            await channel.send(x)
            return
        if message.content.startswith('save'):
            f = open('SAV.txt','a')
            f.write(message.content.replace("save", "", 1))
#            print (f.read())
            
        if message.content.startswith('spam'):
            for i in (1,1,10):
                await channel.send(message.content.replace('spam','',1))

        if message.content.startswith('t!8-ball'):
            ballactive = 'true'
            time.sleep(0.5)
            await channel.send("And the 8-Ball says.")
            
        if message.author == client.user and message.content == "And the 8-Ball says." and ballactive == 'true':
            messagecontent = message.content
            print("8-ball started")
            for i in range(2):
                messagecontent = messagecontent+"."
                await message.edit(content = messagecontent)
                time.sleep(1)
                print(i)
            f = open("C:/Users/Parker/source/repos/Your mom bot/8-Ball quotes.txt")
            content = f.readlines()
            for i in range(6):
                print(content[i])
            await channel.send(content[random.randrange(1,len(content))])
#            print (avatar)
#        if message.content.startswith('imitate'):
#            channel = message.channel
#            async for message in channel.history(limit = 1):
#                yield message.content
#                guy = 299736315505803264
#                if message.author == guy:
#                    yield message.content
#                    return
        if message.content.startswith("t!user"):
            print(message.author)
        if message.content.startswith('t!roulette'):
            if message.content.startswith('t!roulette -s'):
                if server_data.update['roulette']['is active'] == 'true':
                    await channel.send ("Roulette has already started.")
                    server_data["roulette"]["requests"] = server_data["roulette"]["requests"]+1
                    if server_data["roulette"]["requests"] >= 3 and server_data["roulette"]["requests"] <= len(responses["roulette"]["stop asking"])+2:
                        responses_cnt = server_data["roulette"]["requests"]-3
                        print(responses_cnt)
                        await channel.send (responses["roulette"]["stop asking"][responses_cnt])
                        if responses_cnt == 4:
                            server_data.update["roulette"]["force target"] = message.author.id
                    else:
                        if random.randrange (1, 2, 1) == 1:
                            time.sleep (1)
                            await channel.send ("dumbass")
                else:
                    server_data.update['roulette']['is active'] = 'true'
                    print(server_data['roulette']['is active'])
            if message.content.startswith('t!roulette -j'):
                if server_data["roulette"]["is active"] == 'true' and server_data["roulette"]["joined"].count(message.author.id):
                    joined = server_data["roulette"]['joined']
                    print(joined)
                    joined.append(message.author.id)
                    print (server_data["roulette"]["joined"][-1])
                    server_data["roulette"]["joined"] = joined
            if message.content.startswith("t!roulette -b"):
                if server_data["roulette"]["force target"] != "null":
                    user = client.get_user(server_data["roulette"]["force target"])
                    await message.guild.ban(user, reason="was annoying")
                else:
                    rand = random.randrange(0, len(server_data["roulette"]['joined']), 1)
                    user = client.get_user(server_data["roulette"]['joined'][rand])
                    await message.guild.ban(user)
                    server_data.pop("roulette")
        if message.content.startswith('pfp'):
            channel = message.channel
            msg = message.content
            if message.content.startswith("pfp -s"):
                msg = message.content.replace ('-s', '')
                save = 'true'

            else:
                save = 'false'
            if len(message.mentions) == 0:
                user = message.author
                pfp = user.avatar_url
                print (pfp)
                await channel.send (pfp)
                if save == 'true':
                    r = requests.request("get", pfp)
#                    os.system('print %cd% print %userprofile% && cd %userprofile%\Desktop\"Discord Bot Folder" && curl -o '+user.name+"_ProfilePicture.png "+ str(pfp))
                    r
            else:
                userlst = message.mentions
                for x in userlst:
                    user = x
                    pfp = user.avatar_url
                    print (pfp)
                    await channel.send (pfp)

        with open(server_file.name, 'w') as json_file:
            json.dump(server_data, json_file)
#commands
#        if message.content.startswith('t!dance'):
            "nothing so far"
#
#       if message.content.startswith('t!imitate'):
#            mentions = message.mentions
#            target = mentions[0]
#            for x in target:
#                print(target)
#            channel = message.channel
#            author = message.author
#            print (author)
#            imitatemsg1a = 'Hey guys look, I\'m '
#            imitatemsg1 = imitatemsg1a + target[0]
#            
#            await channel.send('Hey guys look, I\'m' + target[1] )
client = MyClient()
client.run(TOKEN)