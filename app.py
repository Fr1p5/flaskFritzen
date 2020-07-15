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

@app.route('/start')
def start():
    return render_template("start.html")

@app.route('/start', methods=['POST'])
def start_post():
    amount_players = request.form['int']
    return amount_players

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/settings')
def settings():
    return render_template("settings.html")

if __name__ == "__main__":
    app.run(debug=True)