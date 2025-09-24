import requests
from json import loads
import random

def random_chance(chance: float) -> bool:
    return random.random() <= chance

def getRandomTenor(token, query):
    r = requests.get(f"https://tenor.googleapis.com/v2/search?q={query}&key={token}&client_key=my_client_key&limit=1&random=true")
    return loads(r.content)["results"][0]["media_formats"]["gif"]["url"]
    
def has_nootice(string: str):
    string = string.upper()
    base = "NOTIC"
    curr = 0
    for char in string:
        if curr == 2 and char == "O":
            continue
        if char != base[curr]:
            curr = 0
        if char == base[curr]:
            if curr == 4:
                return True
            curr += 1
    return False