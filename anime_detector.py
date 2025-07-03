import asyncio
from google.cloud import vision
from google.cloud.vision_v1 import ImageAnnotatorClient

db = {}

def check_image(url):
    if url in db:
        return db[url]

    client = ImageAnnotatorClient()
    response = client.annotate_image({
        'image': {'source': {'image_uri': url}},
        'features': [
            {
                'type_': vision.Feature.Type.LABEL_DETECTION, 
                'max_results': 50
            }
        ]
        })
    
    has_anime_pfp = False
    for item in response.label_annotations:
        if item.description == "Anime":
            has_anime_pfp = True
            break
    db[url] = has_anime_pfp
    return has_anime_pfp


if __name__ == "__main__":
    check_image("https://cdn.discordapp.com/attachments/755649995021090900/1389870798168264774/elgatobalatro_1.png?ex=6866da4c&is=686588cc&hm=7ef48e0da3b6b001ed3f8ecbaf79e99803a35166c0e0545271c1ad40a9d6169a&")
    check_image("https://cdn.discordapp.com/attachments/755649995021090900/1389870798168264774/elgatobalatro_1.png?ex=6866da4c&is=686588cc&hm=7ef48e0da3b6b001ed3f8ecbaf79e99803a35166c0e0545271c1ad40a9d6169a&")
