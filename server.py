from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db, Customer, Artist, Shipment, Order, Item, FavoriteItem, FavoriteArtist
from jinja2 import StrictUndefined

app = Flask(__name__)
# TODO: line 7 .gitignore
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    return render_template("index.html",  artists=Artist.query.all())


@app.route('/login')
def login():

    # get request from client to retrieve user input in the server
    user_email = request.args.get('email')
    user_password = request.args.get('password')

    # query from the database if the email and password exist under the same account
    customer = Customer.query.filter((Customer.email == user_email) & (
        Customer.password == user_password)).first()

    print(customer)

    if customer:

        customer_route = '/profile/' + str(customer.customer_id)
        return redirect(customer_route)
    else:
        return render_template("login.html")


@ app.route('/gallery/<alias>')
def gallery(alias):

    # Given the artist alias, query the artist selected and pass the required info (all of it?) to the template
    artist = Artist.query.filter(Artist.alias == alias).first()

    return render_template("artistGallery.html", artist=artist)


# @app.route('/gallery/<item>')
# def homepage():
#     return render_template("item.html")


@app.route('/profile/<customer_id>')
def customer_profile(customer_id):

    customer = Customer.query.get(customer_id)

    return render_template("customerProfile.html", customer=customer)


# @app.route('/profile/<artist>')
# def artist_profile():
#     return render_template("artistProfile.html")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5007)
