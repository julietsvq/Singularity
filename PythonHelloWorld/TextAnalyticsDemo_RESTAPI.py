import requests
from pprint import pprint
from dotenv import load_dotenv
import os
import uuid

load_dotenv()
subscription_key = os.getenv("TEXT_ANALYTICS_SUBSCRIPTION_KEY")
endpoint  = os.getenv("TEXT_ANALYTICS_ENDPOINT")

documents = {"documents": [
    {"id": "1", "text": "Esta charla es excelente."},
    {"id": "2", "text": "I hate this thing."},
    {"id": "3", "text": "这是一个用中文写的文件"}
]}

sentiment_url = endpoint + "/text/analytics/v2.1/sentiment"

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
sentiment = requests.post(sentiment_url, headers=headers, json=documents)
sentiments = sentiment.json()
pprint(sentiments)

language_api_url = endpoint + "/text/analytics/v2.1/languages"

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
language = requests.post(language_api_url, headers=headers, json=documents)
languages = language.json()
pprint(languages)

translator_subscription_key = os.getenv("TRANSLATOR_SUBSCRIPTION_KEY")
translator_endpoint  = os.getenv("TRANSLATOR_ENDPOINT")

body = [{
    'text': '这是一个用中文写的文件'
}]


headers = {
    'Ocp-Apim-Subscription-Key': translator_subscription_key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

path = '/translate?api-version=3.0'
params = '&to=es'
constructed_url = 'https://api.cognitive.microsofttranslator.com' + path + params

request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()
response





