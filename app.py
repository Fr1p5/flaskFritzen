from flask import Flask
from flask import render_template, redirect, url_for, request, session

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template("login.html")
    if request.method == 'POST':
        return render_template("home.html")

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/prestart', methods=["POST", "GET"])
def prestart():
    if request.method == "POST":
        user = request.form["amount_players"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("prestart.html")

@app.route('/start', methods=["POST", "GET"])
def start():
    return render_template("start.html")
        
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route("/game")
def game():
    return render_template("game.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/settings')
def settings():
    return render_template("settings.html")

if __name__ == "__main__":
    app.run(debug=True)