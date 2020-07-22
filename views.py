@app.route('/login')
def login():
    return render_template("login.html")
    if request.method == 'POST':
        return render_template("home.html")

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/prestart', methods=["POST", "GET"])
def prestart(amount_players):
    if request.method == "POST":
        amount_players = request.form["amount_players"]
        print(amount_players)
        return amount_players
    else:
        return render_template("prestart.html")
    return amount_players

@app.route('/start', methods=["POST", "GET"])
def start():
    if request.method == "POST":
        for i in amount_players:
            print("name number: {}".format(amount_players))
        else:
            return redirect(url_for("user", usr=user))
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