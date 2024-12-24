# Esercizio 1: Saluto Personalizzato
# Questo programma raccoglie il nome dell'utente e genera un saluto personalizzato.

# Passaggi:
# 1. Usa la funzione input() per chiedere il nome all'utente.
# 2. Controlla che l'input non sia vuoto o composto solo da spazi.
# 3. Genera un saluto personalizzato con il nome fornito dall'utente.
# 4. Se l'input è vuoto, usa un messaggio predefinito.

nome = input("Inserisci il tuo nome: ").strip()
if nome:
    print(f"Ciao, {nome}! Benvenuto!")
else:
    print("Ciao! Non hai inserito un nome, ma sei comunque il benvenuto!")

# Esercizio 2: Convertitore di Temperatura
# Questo programma trasforma i gradi Celsius inseriti dall'utente in gradi Fahrenheit.

# Passaggi:
# 1. Usa input() per chiedere la temperatura in gradi Celsius.
# 2. Converte l'input in un numero float.
# 3. Applica la formula di conversione Fahrenheit = (Celsius * 9/5) + 32.
# 4. Arrotonda il risultato a due decimali.
# 5. Gestisci errori in caso di input non numerico.

try:
    celsius = float(input("Inserisci la temperatura in gradi Celsius: "))
    fahrenheit = round((celsius * 9/5) + 32, 2)
    print(f"{celsius} °C corrispondono a {fahrenheit} °F.")
except ValueError:
    print("Errore: Assicurati di inserire un numero valido.")

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
