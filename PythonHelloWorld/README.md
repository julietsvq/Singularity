Python Hello World on Azure Jupyter Notebook: Text Analytics and Translator Text
  
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
		
5. Create a Requirements.txt file locally with content from [Requirements.txt](https://github.com/julietsvq/Singularity/blob/master/PythonHelloWorld/Requirements.txt)

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

2. Add code from [Hello World Python Client Library](https://github.com/julietsvq/Singularity/blob/master/PythonHelloWorld/TextAnalyticsDemo_ClientLibrary.py)

Using the REST API:

1. New > Notebook:

	Notebook name: TextAnalyticsDemo_RESTAPI
	
	Language: Python 3.6

2. Add code from [Hello World REST API](https://github.com/julietsvq/Singularity/blob/master/PythonHelloWorld/TextAnalyticsDemo_RESTAPI.py)
