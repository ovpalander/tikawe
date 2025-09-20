from flask import Flask
from flask import render_template, request, session, flash, redirect
from config import secret_key
import sqlite3
import users
import secrets

app = Flask(__name__)

app.secret_key = secret_key 

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register")
def register():

    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        flash("VIRHE: salasanat eivät ole samat")
        return redirect("/register")

    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        flash("VIRHE: tunnus on jo varattu")
        return redirect("/register")

    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")

        else:
            flash("VIRHE: väärä tunnus tai salasana")
            return redirect("/login")
    return render_template("login.html")

@app.route("/logout")
def logout():
    del session["user_id"]
    del session["username"]
    return render_template("index.html")
