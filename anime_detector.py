import asyncio
import pickledb
from google.cloud import vision
from google.cloud.vision_v1 import ImageAnnotatorClient

db = pickledb.load("pfp.db", True)


def check_image_url(image):

    client = ImageAnnotatorClient()
    response = client.annotate_image({
        'image': {'source': {'image_uri': image}},
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
    return has_anime_pfp






def check_asset(asset):
    if db.exists(asset.key):
        return db.get(asset.key)
    else:
        isAnime = check_image_url(asset.url)
        db.set(asset.key, isAnime)
        return isAnime
