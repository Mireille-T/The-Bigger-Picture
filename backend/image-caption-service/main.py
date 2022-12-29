from dotenv import load_dotenv
import os
from array import array
from PIL import Image, ImageDraw
import sys
import time
from matplotlib import pyplot as plt
import numpy as np
from pathlib import Path
import urllib.request
import requests, uuid, json

# Import namespaces
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

def GetImageCaption(image_source, language=None):
    global cv_client
    try:
        # Get Configuration Settings
        load_dotenv()
        cog_endpoint = os.getenv('COG_SERVICE_ENDPOINT')
        cog_key = os.getenv('COG_SERVICE_KEY')

        # Get image

        doc_path = '/tmp/image'
        urllib.request.urlretrieve(image_source, doc_path)

        # Authenticate Computer Vision client
        credential = CognitiveServicesCredentials(cog_key) 
        cv_client = ComputerVisionClient(cog_endpoint, credential)

        # Analyze image
        result = AnalyzeImage(doc_path)

        if not language or language == 'en':
            return result
        elif result:
            translation = TranslateText(result.get('result', ''))
            return {'result': translation, 'confidence': result.get('confidence', 0)}
        
    except Exception as ex:
        print(ex)

def AnalyzeImage(image_file):
    # Specify features to be retrieved
    features = [VisualFeatureTypes.description,
            VisualFeatureTypes.tags,
            VisualFeatureTypes.categories,
            VisualFeatureTypes.brands,
            VisualFeatureTypes.objects,
            VisualFeatureTypes.adult]
    
    # Get image analysis opening file as rb for azure data analysis
    with open(image_file, mode="rb") as image_data:
        analysis = cv_client.analyze_image_in_stream(image_data , features)

    # Get image description
    for caption in analysis.description.captions:
        return {"result": caption.text, "confidence": caption.confidence}

def TranslateText(text):
    load_dotenv()
    key = os.getenv('TRANSLATION_SERVICE_KEY')
    endpoint = os.getenv('TRANSLATION_SERVICE_ENDPOINT')
    location = os.getenv('TRANSLATION_SERVICE_LOCATION')
    constructed_url = endpoint + 'translate'

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': ['it']
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    if len(response) > 0:
        translations = response[0].get('translations')
        text = translations[0].get('text', '')
        return text
    return ''
        
def GetThumbnail(image_file):
    print('Generating thumbnail')

def RunMain():
    image_source = ''
    language = ''

    if len(sys.argv) > 2:
        image_source = sys.argv[1]
        language = sys.argv[2]
        image_caption = GetImageCaption(image_source, language)
        print(image_caption)
    elif len(sys.argv) > 1:
        image_source = sys.argv[1]
        image_caption = GetImageCaption(image_source)
        print(image_caption)
    else:
        print("Provide an image URL to run")
        return

if __name__ == "__main__":
    RunMain()