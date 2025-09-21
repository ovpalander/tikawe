from flask import Flask
from flask import render_template, request, session, flash, redirect
from datetime import datetime
from config import secret_key
import sqlite3
import users
import secrets
import companies
import documents

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

    return redirect("/success")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            pass

        else:
            flash("VIRHE: väärä tunnus tai salasana")
            return redirect("/login")

        session["user_id"] = user_id
        session["username"] = username
        session["csrf_token"] = secrets.token_hex(16)
        
        company_id = users.check_companies(user_id)
        if company_id:
            session["company_id"] = company_id
            return redirect("/")

        else:
            return redirect("/new_company")

    return render_template("login.html")

@app.route("/new_company")
def new_company():
    return render_template("new_company.html")

@app.route("/create_company", methods=["POST"])
def create_company():
    company_name = request.form["company_name"]
    business_id = request.form["business_id"]
    city = request.form["city"]
    address = request.form["address"]
    postal_code = request.form["postal_code"]
    apartment_count = request.form["apartment_count"]
    registration_date = request.form["registration_date"]
    completion_year = request.form["completion_year"]
    
    try:
        company_id = companies.create_company(session["user_id"], company_name, business_id, city, address, postal_code, apartment_count, registration_date, completion_year)
        session["company_id"] = company_id
    except sqlite3.IntegrityError:
        flash("VIRHE: yhtiö on jo olemassa")
        return redirect("/new_company")


    return render_template("index.html")

@app.route("/view_company")
def view_company():
    company = companies.get_company(session["company_id"])
    reg_date = datetime.strptime(company["registration_date"], "%Y-%m-%d").date()
    return render_template("view_company.html", company=company, reg_date=reg_date)

@app.route("/add_company_doc", methods=["GET", "POST"])
def add_company_doc():
    if request.method == "GET":
        return render_template("add_company_doc.html")

    if request.method == "POST":
        filename = request.form["name"]
        file = request.form["file"]
        documents.add_company_doc(session["company_id"], filename, file)
        flash("Dokumentti lisätty onnistuneesti!")
        return redirect("/view_company")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("username", None)
    session.pop("company_id", None)
    session.pop("csrf_token", None)
    return render_template("index.html")
