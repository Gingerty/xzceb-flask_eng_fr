from machinetranslation import translator
from flask import Flask, render_template, request
import json
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench(english_text):
    """Function trnalsates english top french
    """
    french = language_translator.translate(
        text = english_text,
        model_id= 'en-fr').get_result()
    return french.get("translations")[0].get("translation")

@app.route("/frenchToEnglish")
def frenchToEnglish(french_text):
    """Function trnalsates english top french
    """
    english = language_translator.translate(
        text = french_text,
        model_id= 'fr-en').get_result()
    return english.get("translations")[0].get("translation")
@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
