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


@app.route('/add_players', methods=["POST", "GET"])
def add_players():

    print("this is the add players page")
    names = []

    if request.method == "POST":

        name = request.form['name']
        print(name)

        for i in range(3):
            names.append(name)
            print(names)
            return render_template("add_players.html")

    else:
        return render_template("add_players.html")

    return render_template("add_players.html")


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