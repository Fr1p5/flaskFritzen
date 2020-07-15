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

@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        return render_template("start.html")

    if request.form["submit"] == "submit":
        amount_players = request.form["amount_players"]
        succes = process(amount_players)
        return render_template("start.html", nameLoop="succesful" if succes else "Failed")

    else:
        return render_template(404)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/settings')
def settings():
    return render_template("settings.html")

if __name__ == "__main__":
    app.run(debug=True)