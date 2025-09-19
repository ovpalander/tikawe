from flask import Flask
from flask import render_template, request, session
from config import secret_key

app = Flask(__name__)

app.secret_key = secret_key 

@app.route("/")
def index():
    #session["user_id"] = "asd"
    #session["username"] = "KEK"
    del session["user_id"]
    del session["username"]
    return render_template("index.html")
