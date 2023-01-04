import logging

import azure.functions as func
from .main import GetImageCaption
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    image = req.params.get('image')
    language = req.params.get('language')
    if not image or not language:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            image = req_body.get('image')
            language = req_body.get('language')

    if image and language:
        caption = GetImageCaption(image, language)
        return func.HttpResponse(json.dumps(caption))
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
