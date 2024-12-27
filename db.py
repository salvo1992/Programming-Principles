import pymongo
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = pymongo.MongoClient(MONGO_URI)
db = client.chatbot_jarvis

# Collezioni
utenti_col = db.utenti
conversazioni_col = db.conversazioni
lista_spesa_col = db.lista_spesa

