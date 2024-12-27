import requests
from dotenv import load_dotenv
import os

load_dotenv()
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")

def cerca_ricette(ingrediente):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "query": ingrediente.strip(),
        "number": 5,
        "apiKey": SPOONACULAR_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return [ricetta["title"] for ricetta in response.json().get("results", [])]
    return []
