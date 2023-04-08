import requests
from json import loads
import random
import openai


with open("words.txt") as f:
    words = f.readlines()
    words = [line.strip() for line in words]

def getRandomTenor(token, query):
    r = requests.get(f"https://tenor.googleapis.com/v2/search?q={query}&key={token}&client_key=my_client_key&limit=1&random=true")
    return loads(r.content)["results"][0]["media_formats"]["gif"]["url"]

def getRandomWord():
    return random.choice(words)

def getDefinition(token, word):
    openai.api_key = token
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f'the word is "{word}". Give me a definition of the word, and respond with only the definiton its self. It should be formated as Word - Word type - Definiton'}]
    )
    return completion["choices"][0]["message"]["content"]