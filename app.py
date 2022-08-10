from flask import Flask, render_template, json, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

