from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask("__name__")

app.config["MYSQL_Host"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "fatec"
app.config["MYSQL_DB"] = "Unes"

mysql = MySQL(app)

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
    if request.method == "POST":
        ema, ass, des= request.form["email"],  request.form["assunto"], request.form["descricao"]

        conn = mysql.connection
        conn.cursor().execute(f"insert into Contato(email_contato, assunto_contato, descricao_contato) values('{ema}', '{ass}', '{des}');")
        conn.commit()
        conn.cursor().close()

    return render_template("contato.html")