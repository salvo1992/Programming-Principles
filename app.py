from flask import Flask, redirect, url_for
from auth_logic import auth_bp
from chatbot_logic import chatbot_bp

app = Flask(__name__)
app.secret_key = "secret_key_for_session_management"

# Registra i blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(chatbot_bp)

@app.route("/")
def index():
    return redirect(url_for("auth.login"))

if __name__ == "__main__":
    app.run(debug=True)
