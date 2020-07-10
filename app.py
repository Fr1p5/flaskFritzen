from flask import Flask
from flask import render_template, redirect, url_for, request, session

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")
    if request.method == 'POST':
        return render_template("home.html")
    

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)