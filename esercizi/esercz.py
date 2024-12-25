# Esercizio 1: Saluto Personalizzato
# Questo programma raccoglie il nome dell'utente e genera un saluto personalizzato.

# Passaggi:
# 1. Usa la funzione input() per chiedere il nome all'utente.
# 2. Controlla che l'input non sia vuoto o composto solo da spazi.
# 3. Genera un saluto personalizzato con il nome fornito dall'utente.
# 4. Se l'input è vuoto, usa un messaggio predefinito.

# nome = input("Inserisci il tuo nome: ").strip()
# if nome:
#     print(f"Ciao, {nome}! Benvenuto!")
# else:
#     print("Ciao! Non hai inserito un nome, ma sei comunque il benvenuto!")





# Esercizio 2: Convertitore di Temperatura
# Questo programma trasforma i gradi Celsius inseriti dall'utente in gradi Fahrenheit.

# Passaggi:
# 1. Usa input() per chiedere la temperatura in gradi Celsius.
# 2. Converte l'input in un numero float.
# 3. Applica la formula di conversione Fahrenheit = (Celsius * 9/5) + 32.
# 4. Arrotonda il risultato a due decimali.
# 5. Gestisci errori in caso di input non numerico.

# try:
#     celsius = float(input("Inserisci la temperatura in gradi Celsius: "))
#     fahrenheit = round((celsius * 9/5) + 32, 2)
#     print(f"{celsius} °C corrispondono a {fahrenheit} °F.")
# except ValueError:
#     print("Errore: Assicurati di inserire un numero valido.")




# Esercizio 3: Calcolatrice Geometrica
# Questo programma calcola l'area e il perimetro di un rettangolo.

# Passaggi:
# 1. Chiedi all'utente di inserire lunghezza e larghezza.
# 2. Valida che i valori siano numeri positivi.
# 3. Calcola area = lunghezza * larghezza.
# 4. Calcola perimetro = 2 * (lunghezza + larghezza).
# 5. Mostra i risultati in modo chiaro.

try:
    lunghezza = float(input("Inserisci la lunghezza del rettangolo: "))
    larghezza = float(input("Inserisci la larghezza del rettangolo: "))
    if lunghezza > 0 and larghezza > 0:
        area = lunghezza * larghezza
        perimetro = 2 * (lunghezza + larghezza)
        print(f"L'area del rettangolo è {area:.2f} e il perimetro è {perimetro:.2f}.")
    else:
        print("Errore: Lunghezza e larghezza devono essere numeri positivi.")
except ValueError:
    print("Errore: Assicurati di inserire valori numerici validi.")

# Esercizio 4: Generatore di Password Sicure
# Questo programma genera password complesse in base alla lunghezza specificata dall'utente.

# Passaggi:
# 1. Chiedi all'utente di specificare la lunghezza della password.
# 2. Valida che la lunghezza sia un numero intero maggiore o uguale a 8.
# 3. Genera una password casuale che includa almeno:
#    - 1 lettera maiuscola
#    - 1 lettera minuscola
#    - 1 numero
#    - 1 carattere speciale
# 4. Stampa la password generata.

import random
import string

try:
    lunghezza = int(input("Inserisci la lunghezza desiderata per la password (minimo 8): "))
    if lunghezza >= 8:
        caratteri = (
            random.choices(string.ascii_uppercase, k=1) +
            random.choices(string.ascii_lowercase, k=1) +
            random.choices(string.digits, k=1) +
            random.choices(string.punctuation, k=1) +
            random.choices(string.ascii_letters + string.digits + string.punctuation, k=lunghezza - 4)
        )
        random.shuffle(caratteri)
        password = ''.join(caratteri)
        print(f"La tua password generata è: {password}")
    else:
        print("Errore: La lunghezza minima per la password è 8 caratteri.")
except ValueError:
    print("Errore: Inserisci un numero intero valido.")

# Esercizio 5: Convertitore Universale di Unità
# Questo programma converte tra diverse unità di lunghezza e peso.

# Passaggi:
# 1. Chiedi all'utente di specificare unità di origine, unità di destinazione e valore da convertire.
# 2. Valida che il valore sia numerico.
# 3. Esegui la conversione supportata usando un dizionario di fattori di conversione.
# 4. Mostra il risultato della conversione.

conversioni_lunghezza = {
    "m_to_cm": 100, "m_to_km": 0.001, "m_to_mm": 1000,
    "cm_to_m": 0.01, "km_to_m": 1000, "mm_to_m": 0.001,
    "m_to_in": 39.37, "m_to_ft": 3.281
}

conversioni_peso = {
    "kg_to_g": 1000, "kg_to_mg": 1e6, "kg_to_lb": 2.205,
    "g_to_kg": 0.001, "mg_to_kg": 1e-6, "lb_to_kg": 0.4536
}

try:
    tipo = input("Che tipo di conversione vuoi fare? (lunghezza/peso): ").strip().lower()
    if tipo == "lunghezza":
        unita_origine = input("Inserisci l'unità di origine (m, cm, km, mm, in, ft): ").strip().lower()
        unita_destinazione = input("Inserisci l'unità di destinazione (m, cm, km, mm, in, ft): ").strip().lower()
        valore = float(input("Inserisci il valore da convertire: "))
        chiave_conversione = f"{unita_origine}_to_{unita_destinazione}"
        if chiave_conversione in conversioni_lunghezza:
            risultato = valore * conversioni_lunghezza[chiave_conversione]
            print(f"{valore} {unita_origine} corrispondono a {risultato:.2f} {unita_destinazione}.")
        else:
            print("Errore: Conversione non supportata.")
    elif tipo == "peso":
        unita_origine = input("Inserisci l'unità di origine (kg, g, mg, lb): ").strip().lower()
        unita_destinazione = input("Inserisci l'unità di destinazione (kg, g, mg, lb): ").strip().lower()
        valore = float(input("Inserisci il valore da convertire: "))
        chiave_conversione = f"{unita_origine}_to_{unita_destinazione}"
        if chiave_conversione in conversioni_peso:
            risultato = valore * conversioni_peso[chiave_conversione]
            print(f"{valore} {unita_origine} corrispondono a {risultato:.2f} {unita_destinazione}.")
        else:
            print("Errore: Conversione non supportata.")
    else:
        print("Errore: Tipo di conversione non valido.")
except ValueError:
    print("Errore: Assicurati di inserire un valore numerico valido.")


#PROGRAMMING FUNDAMENTALS 2

# Esercizio 1: Controllo Numeri Pari/Dispari
# Questo programma determina se un numero è pari o dispari.

# Passaggi:
# 1. Chiedi all'utente di inserire un numero intero.
# 2. Usa l'operatore modulo per controllare la parità.
# 3. Stampa un messaggio che indica se il numero è pari o dispari.
# 4. Gestisci input non numerici.

try:
    numero = int(input("Inserisci un numero intero: "))
    if numero % 2 == 0:
        print(f"Il numero {numero} è pari.")
    else:
        print(f"Il numero {numero} è dispari.")
except ValueError:
    print("Errore: Inserisci un numero intero valido.")

# Esercizio 2: Calcolatrice Fattoriale
# Questo programma calcola il fattoriale di un numero.

# Passaggi:
# 1. Chiedi all'utente di inserire un numero intero non negativo.
# 2. Usa un ciclo for per calcolare il fattoriale.
# 3. Gestisci il caso di zero e numeri negativi.
# 4. Applica un limite per evitare overflow.

try:
    numero = int(input("Inserisci un numero intero non negativo: "))
    if numero < 0:
        print("Errore: Il fattoriale non è definito per numeri negativi.")
    elif numero > 20:  # Limite per evitare overflow
        print("Errore: Numero troppo grande per calcolare il fattoriale.")
    else:
        fattoriale = 1
        for i in range(1, numero + 1):
            fattoriale *= i
        print(f"Il fattoriale di {numero} è {fattoriale}.")
except ValueError:
    print("Errore: Inserisci un numero intero valido.")

# Esercizio 3: Setaccio per Numeri Primi
# Questo programma trova tutti i numeri primi in un intervallo specificato.

# Passaggi:
# 1. Chiedi all'utente di inserire l'intervallo di ricerca.
# 2. Usa un algoritmo con cicli annidati per verificare la primalità.
# 3. Stampa i numeri primi trovati.

try:
    inizio = int(input("Inserisci l'inizio dell'intervallo: "))
    fine = int(input("Inserisci la fine dell'intervallo: "))
    if inizio < 2:
        inizio = 2
    numeri_primi = []
    for numero in range(inizio, fine + 1):
        primo = True
        for divisore in range(2, int(numero**0.5) + 1):
            if numero % divisore == 0:
                primo = False
                break
        if primo:
            numeri_primi.append(numero)
    print(f"I numeri primi nell'intervallo {inizio}-{fine} sono: {numeri_primi}")
except ValueError:
    print("Errore: Inserisci valori numerici validi per l'intervallo.")

# Esercizio 4: Calcolatrice Interattiva
# Questo programma esegue operazioni di base tramite un menu interattivo.

# Passaggi:
# 1. Mostra un menu con 4 operazioni principali.
# 2. Chiedi all'utente di selezionare un'opzione.
# 3. Esegui l'operazione scelta e gestisci eccezioni (divisione per zero, input non validi).
# 4. Permetti di ripetere le operazioni o uscire dal programma.

def calcolatrice():
    while True:
        print("\nMenu Calcolatrice:")
        print("1. Addizione")
        print("2. Sottrazione")
        print("3. Moltiplicazione")
        print("4. Divisione")
        print("5. Esci")
        try:
            scelta = int(input("Scegli un'operazione (1-5): "))
            if scelta == 5:
                print("Uscita dal programma.")
                break
            elif scelta in [1, 2, 3, 4]:
                num1 = float(input("Inserisci il primo numero: "))
                num2 = float(input("Inserisci il secondo numero: "))
                if scelta == 1:
                    print(f"Risultato: {num1 + num2}")
                elif scelta == 2:
                    print(f"Risultato: {num1 - num2}")
                elif scelta == 3:
                    print(f"Risultato: {num1 * num2}")
                elif scelta == 4:
                    if num2 != 0:
                        print(f"Risultato: {num1 / num2}")
                    else:
                        print("Errore: Divisione per zero non permessa.")
            else:
                print("Errore: Scelta non valida. Riprova.")
        except ValueError:
            print("Errore: Inserisci valori numerici validi.")

calcolatrice()

# Esercizio 5: Analizzatore Studenti
# Questo programma gestisce un elenco di studenti e analizza i loro voti.

# Passaggi:
# 1. Permetti all'utente di inserire dati per più studenti (nome e voti).
# 2. Implementa funzioni per calcolare la media, ordinare gli studenti e identificare la media più alta/bassa.
# 3. Gestisci parità nei risultati.

studenti = []
while True:
    nome = input("Inserisci il nome dello studente (o 'fine' per terminare): ").strip()
    if nome.lower() == 'fine':
        break
    try:
        voti = list(map(float, input(f"Inserisci i voti di {nome}, separati da spazi: ").split()))
        if voti:
            studenti.append((nome, voti))
        else:
            print("Errore: Inserisci almeno un voto.")
    except ValueError:
        print("Errore: Inserisci solo numeri validi per i voti.")

def calcola_media(voti):
    return sum(voti) / len(voti)

if studenti:
    medie = [(nome, calcola_media(voti)) for nome, voti in studenti]
    medie_ordinate = sorted(medie, key=lambda x: x[1], reverse=True)
    print("\nClassifica Studenti per Media:")
    for nome, media in medie_ordinate:
        print(f"{nome}: {media:.2f}")
    migliore = medie_ordinate[0]
    peggiore = medie_ordinate[-1]
    print(f"\nStudente con la media più alta: {migliore[0]} con {migliore[1]:.2f}")
    print(f"Studente con la media più bassa: {peggiore[0]} con {peggiore[1]:.2f}")
else:
    print("Nessun dato sugli studenti inserito.")


#Programmazione Orientata agli Oggetti

# Esercizio 1: Registro Studenti con Dizionari
# Questo programma gestisce le informazioni degli studenti utilizzando i dizionari.

studenti = []

def aggiungi_studente(nome, eta, voti):
    studenti.append({"nome": nome, "eta": eta, "voti": voti})

def calcola_media_voti(nome):
    for studente in studenti:
        if studente["nome"] == nome:
            voti = studente["voti"]
            return sum(voti) / len(voti) if voti else 0
    return None

def stampa_informazioni():
    for studente in studenti:
        print(f"Nome: {studente['nome']}, Età: {studente['eta']}, Voti: {studente['voti']}")

# Esempio di utilizzo
aggiungi_studente("Mario", 18, [8, 9, 7])
aggiungi_studente("Anna", 20, [6, 7, 8])
stampa_informazioni()
print(f"Media voti di Mario: {calcola_media_voti('Mario')}")

# Esercizio 2: Classe Geometrica per Cerchio
import math

class Cerchio:
    def __init__(self, raggio):
        if raggio <= 0:
            raise ValueError("Il raggio deve essere maggiore di zero.")
        self.raggio = raggio

    def area(self):
        return math.pi * self.raggio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raggio

    def diametro(self):
        return 2 * self.raggio

# Esempio di utilizzo
cerchio = Cerchio(5)
print(f"Area: {cerchio.area():.2f}, Perimetro: {cerchio.perimetro():.2f}, Diametro: {cerchio.diametro():.2f}")

# Esercizio 3: Sistema di Gestione Clienti
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.acquisti = []

    def registra_acquisto(self, importo):
        self.acquisti.append(importo)

    def totale_speso(self):
        return sum(self.acquisti)

    def genera_report(self):
        return f"Cliente: {self.nome}, Totale speso: {self.totale_speso():.2f}"

# Esempio di utilizzo
cliente = Cliente("Giulia")
cliente.registra_acquisto(50.5)
cliente.registra_acquisto(20.0)
print(cliente.genera_report())

# Esercizio 4: Sistema Bancario con Ereditarietà
class BankAccount:
    def __init__(self, titolare, saldo=0):
        self.titolare = titolare
        self.saldo = saldo

    def deposito(self, importo):
        self.saldo += importo

    def prelievo(self, importo):
        if self.saldo - importo < 0:
            raise ValueError("Saldo insufficiente.")
        self.saldo -= importo

    def get_balance(self):
        return self.saldo

class SavingsAccount(BankAccount):
    def __init__(self, titolare, saldo=0, tasso_interesse=0.01):
        super().__init__(titolare, saldo)
        self.tasso_interesse = tasso_interesse

    def applica_interessi(self):
        self.saldo += self.saldo * self.tasso_interesse

class CurrentAccount(BankAccount):
    def __init__(self, titolare, saldo=0, limite_scoperto=500):
        super().__init__(titolare, saldo)
        self.limite_scoperto = limite_scoperto

    def prelievo(self, importo):
        if self.saldo - importo < -self.limite_scoperto:
            raise ValueError("Limite di scoperto superato.")
        self.saldo -= importo

# Esempio di utilizzo
conto_risparmio = SavingsAccount("Luca", 1000)
conto_risparmio.applica_interessi()
print(f"Saldo dopo interessi: {conto_risparmio.get_balance():.2f}")

conto_corrente = CurrentAccount("Marco", 200)
conto_corrente.prelievo(600)
print(f"Saldo dopo prelievo: {conto_corrente.get_balance():.2f}")

# Esercizio 5: Sistema di Prenotazione Astratto
from abc import ABC, abstractmethod

class Reservation(ABC):
    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def check_availability(self):
        pass

    @abstractmethod
    def confirm_reservation(self):
        pass

class FlightReservation(Reservation):
    def calculate_price(self):
        return 150

    def check_availability(self):
        return True

    def confirm_reservation(self):
        return "Prenotazione volo confermata."

class HotelReservation(Reservation):
    def calculate_price(self):
        return 100

    def check_availability(self):
        return True

    def confirm_reservation(self):
        return "Prenotazione hotel confermata."

class RestaurantReservation(Reservation):
    def calculate_price(self):
        return 50

    def check_availability(self):
        return True

    def confirm_reservation(self):
        return "Prenotazione ristorante confermata."

# Esempio di utilizzo
volo = FlightReservation()
hotel = HotelReservation()
ristorante = RestaurantReservation()

print(volo.confirm_reservation())
print(hotel.confirm_reservation())
print(ristorante.confirm_reservation())


#ADVANCED OBJECT ORIENTED PROGRAMMING


# Esercizio 1: Gestione Base delle Eccezioni
# Questo programma gestisce eccezioni comuni nelle operazioni matematiche.

def divisione(a, b):
    try:
        risultato = a / b
        print(f"Risultato: {risultato}")
    except ZeroDivisionError:
        print("Errore: Divisione per zero non permessa.")
    except TypeError:
        print("Errore: Assicurati che entrambi gli input siano numeri.")

def conversione_tipo(valore):
    try:
        numero = float(valore)
        print(f"Valore convertito: {numero}")
    except ValueError:
        print("Errore: Impossibile convertire l'input in un numero.")

# Esempio di utilizzo
divisione(10, 2)
divisione(10, 0)
divisione("10", 2)
conversione_tipo("123.45")
conversione_tipo("abc")

# Esercizio 2: Eccezioni Personalizzate
# Questo programma utilizza eccezioni personalizzate per gestire errori specifici.

class ValidationError(Exception):
    def __init__(self, messaggio):
        super().__init__(f"Errore di validazione: {messaggio}")

class AuthenticationError(Exception):
    def __init__(self, messaggio):
        super().__init__(f"Errore di autenticazione: {messaggio}")

class AuthorizationError(Exception):
    def __init__(self, messaggio):
        super().__init__(f"Errore di autorizzazione: {messaggio}")

def autentica(utente, password):
    if utente != "admin":
        raise AuthenticationError("Utente non riconosciuto.")
    if password != "1234":
        raise AuthenticationError("Password errata.")

def valida_dati(dati):
    if not isinstance(dati, dict):
        raise ValidationError("I dati devono essere un dizionario.")
    if "nome" not in dati or "eta" not in dati:
        raise ValidationError("Dati incompleti: nome e età sono obbligatori.")

# Esempio di utilizzo
try:
    autentica("admin", "1234")
    valida_dati({"nome": "Mario", "eta": 30})
    print("Operazione completata con successo.")
except (AuthenticationError, ValidationError) as e:
    print(e)

# Esercizio 3: Polimorfismo e Metodi Speciali
# Questo programma utilizza il polimorfismo per calcolare area e perimetro di forme geometriche.

import math

class FormaGeometrica:
    def area(self):
        raise NotImplementedError("Metodo area() non implementato.")

    def perimeter(self):
        raise NotImplementedError("Metodo perimeter() non implementato.")

    def __str__(self):
        return "Forma geometrica generica."

class Quadrato(FormaGeometrica):
    def __init__(self, lato):
        self.lato = lato

    def area(self):
        return self.lato ** 2

    def perimeter(self):
        return 4 * self.lato

    def __str__(self):
        return f"Quadrato con lato {self.lato}."

class Cerchio(FormaGeometrica):
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return math.pi * self.raggio ** 2

    def perimeter(self):
        return 2 * math.pi * self.raggio

    def __str__(self):
        return f"Cerchio con raggio {self.raggio}."

# Esempio di utilizzo
forme = [Quadrato(4), Cerchio(3)]
for forma in forme:
    print(forma)
    print(f"Area: {forma.area():.2f}, Perimetro: {forma.perimeter():.2f}")

# Esercizio 4: Introspezione e Riflessività
# Questo programma utilizza introspezione per analizzare oggetti dinamicamente.

def analizza_oggetto(obj):
    print(f"Tipo dell'oggetto: {type(obj)}")
    print("Attributi:")
    for attr in dir(obj):
        if not attr.startswith("__"):
            print(f" - {attr}")
    print("Metodi:")
    for metodo in dir(obj):
        if callable(getattr(obj, metodo)) and not metodo.startswith("__"):
            print(f" - {metodo}")

# Esempio di utilizzo
analizza_oggetto(Cerchio(5))


# FILE OPERATIONS AND DATA STRUCTURES 

# Esercizio 1: Gestione di File di Testo
# Questo programma esegue operazioni di base su file di testo.

def leggi_file(nome_file):
    try:
        with open(nome_file, 'r') as file:
            contenuto = file.read()
        print(contenuto)
    except FileNotFoundError:
        print("Errore: Il file non esiste.")
    except IOError as e:
        print(f"Errore durante la lettura del file: {e}")

def scrivi_file(nome_file, contenuto):
    try:
        with open(nome_file, 'w') as file:
            file.write(contenuto)
        print("Scrittura completata.")
    except IOError as e:
        print(f"Errore durante la scrittura del file: {e}")

def aggiungi_file(nome_file, contenuto):
    try:
        with open(nome_file, 'a') as file:
            file.write(contenuto)
        print("Aggiunta completata.")
    except IOError as e:
        print(f"Errore durante l'aggiunta al file: {e}")

# Esempio di utilizzo
scrivi_file("esempio.txt", "Questo è un file di esempio.\n")
aggiungi_file("esempio.txt", "Aggiunta di un'altra riga.\n")
leggi_file("esempio.txt")

# Esercizio 2: Analisi dei Dati da File CSV
# Questo programma analizza dati da un file CSV.

import csv

def carica_csv(nome_file):
    try:
        with open(nome_file, 'r') as file:
            lettore = csv.DictReader(file)
            dati = [riga for riga in lettore]
        return dati
    except FileNotFoundError:
        print("Errore: Il file non esiste.")
        return []
    except IOError as e:
        print(f"Errore durante la lettura del file CSV: {e}")
        return []

def calcola_statistiche(dati, colonna):
    try:
        valori = [float(riga[colonna]) for riga in dati if riga[colonna]]
        media = sum(valori) / len(valori)
        massimo = max(valori)
        minimo = min(valori)
        return {"media": media, "massimo": massimo, "minimo": minimo}
    except KeyError:
        print("Errore: Colonna non trovata.")
        return None
    except ValueError:
        print("Errore: Valori non numerici nella colonna.")
        return None

def filtra_dati(dati, colonna, valore):
    return [riga for riga in dati if riga.get(colonna) == valore]

# Esempio di utilizzo
dati_csv = carica_csv("esempio.csv")
if dati_csv:
    print(calcola_statistiche(dati_csv, "Prezzo"))
    filtrati = filtra_dati(dati_csv, "Categoria", "Elettronica")
    print(filtrati)

# Esercizio 3: Gestione di Conti Bancari con JSON
# Questo programma gestisce conti bancari utilizzando file JSON.

import json

class ContoBancario:
    def __init__(self, titolare, saldo=0):
        self.titolare = titolare
        self.saldo = saldo

    def deposito(self, importo):
        self.saldo += importo

    def prelievo(self, importo):
        if self.saldo - importo < 0:
            raise ValueError("Saldo insufficiente.")
        self.saldo -= importo

    def to_dict(self):
        return {"titolare": self.titolare, "saldo": self.saldo}

    @staticmethod
    def from_dict(dati):
        return ContoBancario(dati["titolare"], dati["saldo"])

def carica_conti(nome_file):
    try:
        with open(nome_file, 'r') as file:
            dati = json.load(file)
        return [ContoBancario.from_dict(conti) for conti in dati]
    except FileNotFoundError:
        print("Errore: Il file non esiste.")
        return []
    except json.JSONDecodeError:
        print("Errore: File JSON non valido.")
        return []

def salva_conti(nome_file, conti):
    try:
        with open(nome_file, 'w') as file:
            json.dump([conto.to_dict() for conto in conti], file)
        print("Dati salvati correttamente.")
    except IOError as e:
        print(f"Errore durante il salvataggio dei dati: {e}")

# Esempio di utilizzo
conti = carica_conti("conti.json")
if conti:
    conti[0].deposito(100)
    salva_conti("conti.json", conti)


# DOCD AND EXTERNAL PACKAGES 

# Esercizio 1: Documentazione del Codice
# Questo modulo include un esempio di codice ben documentato.

def addizione(a, b):
    """Calcola la somma di due numeri.

    Args:
        a (float): Il primo numero.
        b (float): Il secondo numero.

    Returns:
        float: La somma dei due numeri.

    Raises:
        TypeError: Se uno degli argomenti non è un numero.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Entrambi gli argomenti devono essere numeri.")
    return a + b

class Rettangolo:
    """Classe che rappresenta un rettangolo.

    Attributes:
        base (float): La lunghezza della base del rettangolo.
        altezza (float): L'altezza del rettangolo.
    """

    def __init__(self, base, altezza):
        """Inizializza un'istanza della classe Rettangolo.

        Args:
            base (float): La base del rettangolo.
            altezza (float): L'altezza del rettangolo.

        Raises:
            ValueError: Se base o altezza sono valori non positivi.
        """
        if base <= 0 or altezza <= 0:
            raise ValueError("Base e altezza devono essere numeri positivi.")
        self.base = base
        self.altezza = altezza

    def area(self):
        """Calcola l'area del rettangolo.

        Returns:
            float: L'area del rettangolo.
        """
        return self.base * self.altezza

    def perimetro(self):
        """Calcola il perimetro del rettangolo.

        Returns:
            float: Il perimetro del rettangolo.
        """
        return 2 * (self.base + self.altezza)

# Esempio di utilizzo
def esempio_rettangolo():
    """Esempio di utilizzo della classe Rettangolo."""
    rettangolo = Rettangolo(5, 10)
    print(f"Area: {rettangolo.area()} Perimetro: {rettangolo.perimetro()}")

esempio_rettangolo()

# Esercizio 2: Interazione con API REST
import requests

def fetch_weather_data(city):
    """Recupera i dati meteo per una città utilizzando un'API REST.

    Args:
        city (str): Il nome della città.

    Returns:
        dict: I dati meteo ricevuti dall'API.

    Raises:
        requests.exceptions.RequestException: Se c'è un problema di rete.
    """
    api_key = "your_api_key_here"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la richiesta: {e}")
        return None

# Esempio di utilizzo
def esempio_api():
    """Esempio di utilizzo della funzione fetch_weather_data."""
    city = "Rome"
    dati_meteo = fetch_weather_data(city)
    if dati_meteo:
        print(f"Meteo a {city}: {dati_meteo['weather'][0]['description']}, Temperatura: {dati_meteo['main']['temp']} °C")

esempio_api()
