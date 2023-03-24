import requests
from json import loads
import random


with open("words.txt") as f:
    words = f.readlines()
    words = [line.strip() for line in words]

def getRandomTenor(token, query):
    r = requests.get(f"https://tenor.googleapis.com/v2/search?q={query}&key={token}&client_key=my_client_key&limit=1&random=true")
    return loads(r.content)["results"][0]["media_formats"]["gif"]["url"]

def getRandomWord():
    return random.choice(words)