from flask import Flask, render_template, request, flash, session, redirect
# from model import connect_to_db, db, Customer, Order, Item, Shipment, Artist
from jinja2 import StrictUndefined

app = Flask(__name__)
# TODO: line 7 .gitignore
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/gallery/<artist>')
def gallery():
    return render_template("gallery.html")


@app.route('/gallery/<item>')
def homepage():
    return render_template("item.html")


@app.route('/profile/<customer>')
def customer_profile():
    return render_template("customerProfile.html")


@app.route('/profile/<artist>')
def artist_profile():
    return render_template("artistProfile.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
