from flask import Flask, render_template, json, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/food-menu")
def food():
    return render_template("foodMenu.html")

@app.route("/drinks-menu")
def drinks():
    return render_template("drinksMenu.html")

@app.route("/about-us")
def aboutUs():
    return render_template("aboutUs.html")

if __name__ == '__main__':
    app.run(debug=True)