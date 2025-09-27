import requests
from agents import function_tool
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")


@function_tool
def translate_text(text: str, target_lang: str, source_lang: str = "en") -> str:
    api_key = GOOGLE_API_KEY
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {"key": api_key, "q": text, "target": target_lang, "source": source_lang}
    response = requests.post(url, params=params)
    translated_text = response.json()["data"]["translations"][0]["translatedText"]
    return translated_text
