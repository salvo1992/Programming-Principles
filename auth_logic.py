from flask import Blueprint, render_template, request, redirect, url_for, session
from db import utenti_col
import bcrypt

auth_bp = Blueprint("auth", __name__, template_folder="templates")
from flask import Blueprint, render_template, request, redirect, url_for, session
from db import utenti_col
import bcrypt

auth_bp = Blueprint("auth", __name__, template_folder="templates")

# Registrazione
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if utenti_col.find_one({"email": email}):
            return render_template("register.html", error="Email già registrata.")
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        utenti_col.insert_one({"email": email, "password": hashed_pw})
        return redirect(url_for("auth.login"))
    return render_template("register.html")

# Login
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = utenti_col.find_one({"email": email})
        if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
            session["utente_id"] = str(user["_id"])
            session["email"] = email
            return redirect(url_for("chatbot.chat"))
        return render_template("login.html", error="Credenziali non valide.")
    return render_template("login.html")

# Logout
@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

