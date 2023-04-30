from flask import Flask, render_template
app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/quemSomos")
def quemSomos():
    return render_template("quemSomos.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")