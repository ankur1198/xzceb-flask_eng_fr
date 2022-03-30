"""Peer graded Assognment"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = 'EcujH7-LjcsfOy4DzGTn00oWmBfL-wzKTavt4UAQAMw9'
url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/113e5b0a-69a2-4f4e-b8d3-a47985310cd6'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishText):
    """Translates From English to French"""
    #englishText = input()
    frenchText = language_translator.translate(
         text=englishText,
         model_id= 'en-fr').get_result()
    return frenchText.get("translations")[0].get("translation")
    

def french_to_english(frenchText):
    """Translates From French to English"""
    #frenchText = input()
    englishText = language_translator.translate(
        text=frenchText,
        model_id= 'fr-en').get_result()
    return englishText.get("translations")[0].get("translation") 
    
print()
print("\n")