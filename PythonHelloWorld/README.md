##Python Hello World on Azure Jupyter Notebook: Text Analytics and Translator Text
  
  1. In the Azure portal, create a Text Analytics resource and write down its key and endpoint.
	
	2. Go to https://notebooks.azure.com and sign in. 
	
	3. My Projects > + New Project
	
		Project name: CognitiveServicesDemo
		Project ID: cognitiveservicesdemo
		Public project: (cleared)
		Create a README.md: (cleared)
		
	4. Create an .env file locally with the following content: 
	 
		TEXT_ANALYTICS_SUBSCRIPTION_KEY=[text_analytics_key]
		TEXT_ANALYTICS_ENDPOINT=[text_analytics_endpoint]
    TRANSLATOR_SUBSCRIPTION_KEY=[translator_key]
    TRANSLATOR_ENDPOINT=[translator_endpoint]
		
	5. Create a Requirements.txt file locally with the following content: 
	
		python-dotenv
		requests
		azure-cognitiveservices-language-textanalytics
		azure-cognitiveservices-vision-face

	6. Click Upload > From Computer and then: 
		Select the .env file you just created and Upload.
		Select the Requirements.txt file you just created and Upload.
		
	7. Click Project Settings > Environment > Add
		Select operation: Requirements.txt
		File: select the Requirements.txt file you uploaded
		Python version: 3.6
		
	8. You will probably need to stop and run your project server for the requirements to be installed.
	
	Using the Client Libraries:
	
		1. New > Notebook:
			Notebook name: TextAnalyticsDemo_ClientLibrary
			Language: Python 3.6
			
		2. Add the following code: 
		
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
		
	Using the REST API:
	
		1. New > Notebook:
			Notebook name: TextAnalyticsDemo_RESTAPI
			Language: Python 3.6
			
		2. Add the following code: 
		
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

