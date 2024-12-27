from flask import Blueprint, render_template, request, session, redirect, url_for
from db import conversazioni_col, lista_spesa_col
from api_utils import cerca_ricette
import random

chatbot_bp = Blueprint("chatbot", __name__, template_folder="templates")

@chatbot_bp.route("/chat", methods=["GET", "POST"])
def chat():
    if "utente_id" not in session:
        return redirect(url_for("auth.login"))
    
    risposta = None
    if request.method == "POST":
        messaggio = request.form["messaggio"]
        risposta = ""
        if "ricette" in messaggio.lower():
            ingrediente = messaggio.split()[-1]
            ricette = cerca_ricette(ingrediente)
            if ricette:
                risposta = f"Ecco alcune ricette per {ingrediente}: {', '.join(ricette)}"
            else:
                risposta = f"Nessuna ricetta trovata per {ingrediente}."
        else:
            risposta = f"Jarvis: Hai detto '{messaggio}'"

        conversazioni_col.insert_one({
            "utente_id": session["utente_id"],
            "messaggio": messaggio,
            "risposta": risposta
        })

    return render_template("chatbot.html", email=session["email"], risposta=risposta)
