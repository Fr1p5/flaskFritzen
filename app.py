from flask import Flask
from flask import render_template, redirect, url_for, request, session

app = Flask(__name__)

class players:
    def __init__(self, name, points):
        self.name = name
        self.points = points


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
        amount_players = request.form["amount_players"]
        amount_players = int(amount_players)
        print(amount_players)
        return render_template("prestart.html", amount_players=amount_players)

    print("this is the prestart page ")

    return render_template("prestart.html")


@app.route('/add_players', methods=["POST", "GET"])
def add_players():

    print("this is the add players page")
    amount_players = int(request.form["amount_players"])
    print(amount_players)
    print(type(amount_players))

    names = []

    if request.method == "POST":
        for name in range(amount_players):
            print(names)

    return render_template("add_players.html", amount_players=int(amount_players))


@app.route('/start', methods=["POST", "GET"])
def start():

    if request.method == "POST":
        names = []
        name = request.form['name']
        amount_players = request.form['amount_players']

        for i in range(amount_players):
            name[i] = request.form['name']

    print(type(names))
    print(names)

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