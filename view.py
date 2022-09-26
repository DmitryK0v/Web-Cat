from flask import render_template
from app import app


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/cats.html")
def cats():
    return render_template("cats.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/Our_Cats.html")
def our_cats():
    return render_template("Our_Cats.html")
