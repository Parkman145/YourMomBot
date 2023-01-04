def get(image):
    import google
    import io
    import os
    #from dotenv import load_dotenv
    #load_dotenv(dotenv_path=r"C:\Users\Parker\source\repos\Your mom bot\Your mom bot\environment.env")

    # Imports the Google Cloud client library
    from google.cloud import vision
    from google.cloud.vision_v1 import ImageAnnotatorClient

    # Instantiates a client
    client = ImageAnnotatorClient()

    # The name of the image file to annotate
    #file_name = os.path.abspath('beadcate.jpg')

    # Loads the image into memory
    #with io.open(file_name, 'rb') as image_file:
    #    content = image_file.read()

    #image = vision.Image(content=content)
    response = client.annotate_image({
        'image': {'source': {'image_uri': image}},
        'features': [
            {
                'type_': vision.Feature.Type.LABEL_DETECTION, 
                'max_results': 50
            }
        ]
        })
    # Performs label detection on the image file
    #response = client.label_detection(image=image)
    labels = response.label_annotations
    return response
#    print('Labels:')
#    for label in labels:
#        print(label.description)