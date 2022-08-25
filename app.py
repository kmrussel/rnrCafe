from flask import Flask, render_template, json, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/food-menu")
def foodMenu():
    return render_template("foodMenu.html")

@app.route("/drinks-menu")
def drinksMenu():
    return render_template("drinksMenu.html")

@app.route("/sides-menu")
def sidesMenu():
    return render_template("sidesMenu.html")

@app.route("/about-us")
def aboutUs():
    return render_template("aboutUs.html")

@app.route("/nav")
def nav():
    return render_template("nav.html")

if __name__ == '__main__':
    app.run(host="localhost", port=3000,debug=True)
