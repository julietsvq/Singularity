from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv
import os

load_dotenv()
subscription_key = os.getenv("TEXT_ANALYTICS_SUBSCRIPTION_KEY")
endpoint  = os.getenv("TEXT_ANALYTICS_ENDPOINT")

text_analytics = TextAnalyticsClient(endpoint=endpoint, credentials=CognitiveServicesCredentials(subscription_key))

documents = [
    {
        "id": "1",
        "text": "¡Esta es el mejor evento del mundo, es genial!"
    },
    {
        "id": "2",
        "text": "I really hate things, they're terrible"
    }
]

sentiment = text_analytics.sentiment(documents=documents)

for document in sentiment.documents:
    print("Document Id:", document.id, ", Sentiment Score:",
          "{:.2f}".format(document.score))

language = text_analytics.detect_language(documents=documents)

for document in language.documents:
    print("Document Id:", document.id, ", Language:",
          document.detected_languages[0].name)


