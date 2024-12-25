import pymongo
import requests
from dotenv import load_dotenv
import os
import random

# Carica variabili ambientali
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
EDAMAM_APP_ID = os.getenv("EDAMAM_APP_ID")
EDAMAM_APP_KEY = os.getenv("EDAMAM_APP_KEY")

# Connessione a MongoDB
client = pymongo.MongoClient(MONGO_URI)
db = client.chatbot_jarvis
utenti_col = db.utenti
conversazioni_col = db.conversazioni

# Funzione per salvare o aggiornare informazioni utente
def salva_informazioni_utente(utente):
    utenti_col.update_one({"nome": utente["nome"]}, {"$set": utente}, upsert=True)

# Funzione per salvare conversazioni
def salva_conversazione(nome, messaggio, risposta):
    conversazioni_col.insert_one({
        "nome": nome,
        "messaggio": messaggio,
        "risposta": risposta
    })

# Funzione per raccogliere informazioni iniziali
def raccogli_informazioni():
    print("Benvenuto! Prima di iniziare, rispondi a qualche domanda.")
    nome = input("Come ti chiami? ").strip()
    if nome:
        print(f"Ciao {nome}! Io sono Jarvis, il tuo assistente virtuale!")
    else:
        nome = "Amico"
        print("Ciao! Non hai inserito un nome, quindi ti chiamerò 'Amico'.")
    
    colore_preferito = input("Qual è il tuo colore preferito? ").strip()
    numero_preferito = input("Qual è il tuo numero preferito? ").strip()
    cibo_preferito = input("Qual è il tuo cibo preferito? ").strip()
    
    utente = {
        "nome": nome,
        "colore_preferito": colore_preferito,
        "numero_preferito": numero_preferito,
        "cibo_preferito": cibo_preferito
    }
    salva_informazioni_utente(utente)
    return utente

# Funzione per cercare ricette usando Edamam API
def cerca_ricette(ingrediente):
    url = f"https://api.edamam.com/search"
    params = {
        "q": ingrediente,
        "app_id": EDAMAM_APP_ID,
        "app_key": EDAMAM_APP_KEY,
        "to": 5  # Limitiamo a 5 risultati
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        ricette = response.json().get("hits", [])
        return [ricetta["recipe"]["label"] for ricetta in ricette]
    else:
        print("Errore nella chiamata all'API delle ricette.")
        return []

# Funzione principale per il chatbot
def chatbot_jarvis():
    utente = raccogli_informazioni()
    
    while True:
        print("\nCosa posso fare per te oggi?")
        print("1. Parlare della temperatura")
        print("2. Suggerire ricette")
        print("3. Raccontare un aneddoto sul cibo")
        print("4. Uscire")
        
        scelta = input("Inserisci il numero della tua scelta: ").strip()
        risposta = ""
        
        if scelta == "1":
            stagione = input("In che stagione siamo? ").strip()
            temperatura = input("Qual è la temperatura attuale in gradi Celsius? ").strip()
            risposta = f"Siamo in {stagione} con una temperatura di {temperatura} °C."
            print(risposta)
        elif scelta == "2":
            ingrediente = input("Quale ingrediente vuoi usare? ").strip()
            ricette = cerca_ricette(ingrediente)
            if ricette:
                risposta = f"Ecco alcune ricette che puoi provare con {ingrediente}: {', '.join(ricette)}."
                print(risposta)
            else:
                risposta = "Mi dispiace, non ho trovato ricette per questo ingrediente."
                print(risposta)
        elif scelta == "3":
            aneddoti = [
                "Lo sapevi che il miele è l'unico alimento che non scade mai?",
                "Il primo cibo mangiato sulla luna è stato purè di mele.",
                "La pizza è uno degli alimenti più antichi, risale a oltre 2000 anni fa!"
            ]
            risposta = random.choice(aneddoti)
            print(risposta)
        elif scelta == "4":
            risposta = f"Arrivederci, {utente['nome']}! A presto!"
            print(risposta)
            break
        else:
            risposta = "Scelta non valida. Riprova."
            print(risposta)
        
        salva_conversazione(utente["nome"], scelta, risposta)

# Avvio del chatbot
if __name__ == "__main__":
    chatbot_jarvis()

