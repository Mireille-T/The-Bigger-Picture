from dotenv import load_dotenv
import os
from array import array
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
from azure.cosmos import CosmosClient
import os
import uuid


def save_image_caption_to_cosmosdb(container, image_url, caption, confidence, language):
    item = {
        "id": str(uuid.uuid4()),
        "partitionKey": "ImageCaptions",
        "image_url": image_url,
        "caption": caption,
        "confidence": confidence,
        "language": language,
    }
    container.create_item(item)


def find_image_caption(container, image_url, language):
    query = f"SELECT * FROM c WHERE c.image_url = '{image_url}' AND c.language = '{language}'"
    items = list(container.query_items(query, enable_cross_partition_query=True))

    if len(items) > 0:
        return items[0]
    else:
        return None


def initialize_cosmosdb_client():
    cosmosdb_account_uri = os.getenv("COSMOSDB_ACCOUNT_URI")
    cosmosdb_account_key = os.getenv("COSMOSDB_ACCOUNT_KEY")
    cosmosdb_database_name = os.getenv("COSMOSDB_DATABASE_NAME")
    cosmosdb_container_name = os.getenv("COSMOSDB_CONTAINER_NAME")

    client = CosmosClient(cosmosdb_account_uri, cosmosdb_account_key)

    # Create the database if it doesn't exist
    database = client.create_database_if_not_exists(cosmosdb_database_name)

    # Create the container if it doesn't exist
    container = database.create_container_if_not_exists(
        cosmosdb_container_name, partition_key="/id"
    )

    return container


def GetImageCaption(image_source, language="en"):
    global cv_client
    try:
        # Get Configuration Settings
        load_dotenv()
        container = initialize_cosmosdb_client()
        cog_endpoint = os.getenv("COG_SERVICE_ENDPOINT")
        cog_key = os.getenv("COG_SERVICE_KEY")

        # Check if image already exists
        existing_caption = find_image_caption(container, image_source, language)
        if existing_caption:
            return {
                "result": existing_caption["caption"],
                "confidence": existing_caption["confidence"],
            }

        # Analyze image
        features = "caption,read"
        model_version = "latest"
        caption_language = "en"
        api_version = "2023-02-01-preview"
        gender_neutral_caption = "true"

        url = f"{cog_endpoint}/computervision/imageanalysis:analyze?features={features}&model-version={model_version}&language={caption_language}&api-version={api_version}&gender-neutral-caption={gender_neutral_caption}"

        payload = {"url": image_source}
        headers = {
            "Ocp-Apim-Subscription-Key": cog_key,
            "Content-Type": "application/json",
        }
        response = requests.request(
            "POST", url, headers=headers, data=json.dumps(payload)
        )

        if not response:
            return None

        response = response.json()
        if not response:
            return None

        caption_result = response.get("captionResult")
        caption_text, caption_confidence = (
            caption_result["text"],
            caption_result["confidence"],
        )

        read_result = response.get("readResult")
        text_result = read_result["content"]

        alt_text = caption_text
        if alt_text and len(text_result) > 10:
            alt_text = f"{caption_text}, text in image: {text_result}"
        alt_text = alt_text.replace("\n", " ")

        if language != "en":
            translation = TranslateText(alt_text, language)
            result = {
                "result": translation,
                "confidence": caption_confidence,
            }
            return result

        if caption_result:
            save_image_caption_to_cosmosdb(
                container,
                image_source,
                alt_text,
                caption_confidence,
                language,
            )
        return {
            "result": alt_text,
            "confidence": caption_confidence,
        }

    except Exception as ex:
        print(ex)


def TranslateText(text, language):
    load_dotenv()
    key = os.getenv("TRANSLATION_SERVICE_KEY")
    endpoint = os.getenv("TRANSLATION_SERVICE_ENDPOINT")
    location = os.getenv("TRANSLATION_SERVICE_LOCATION")
    constructed_url = endpoint + "translate"

    params = {"api-version": "3.0", "from": "en", "to": [language]}

    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Ocp-Apim-Subscription-Region": location,
        "Content-type": "application/json",
        "X-ClientTraceId": str(uuid.uuid4()),
    }

    body = [{"text": text}]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    if len(response) > 0:
        translations = response[0].get("translations")
        text = translations[0].get("text", "")
        return text
    return ""


def RunMain():
    image_source = ""
    language = ""

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
