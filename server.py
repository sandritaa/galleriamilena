from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db, Customer, Artist, Shipment, Order, Item, FavoriteItem, FavoriteArtist
from jinja2 import StrictUndefined
import crud

app = Flask(__name__)
# TODO: line 7 .gitignore
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined


# create home route
@app.route('/')
def homepage():
    return render_template("index.html",  artists=Artist.query.all())


# create artist gallery route
@app.route('/gallery/<alias>')
def gallery(alias):

    # Given the artist alias, query the artist selected and pass the required info (all of it?) to the template
    artist_user = Artist.query.filter(Artist.alias == alias).first()

    return render_template("artistGallery.html", artist=artist_user)


# create login route
@app.route('/login')
def login():

    # get request from client to retrieve user input in the server
    user_email = request.args.get('email')
    user_password = request.args.get('password')

    # query from the database if the email and password exist under the same account
    customer = Customer.query.filter((Customer.email == user_email) & (
        Customer.password == user_password)).first()
    artist = Artist.query.filter((Artist.email == user_email) & (
        Artist.password == user_password)).first()

    # check if customer query above checks out - if it does, redirect to be below customer route
    if customer:

        # add a session
        session['customer_id'] = customer.customer_id

        #
        customer_route = '/profile/' + \
            str(customer.fname.lower() + customer.lname.lower() +
                '_' + str(customer.customer_id))

        return redirect(customer_route)

    # check if artist query above checks out - if it does, redirect to be below artist route
    elif artist:

        session['artist_id'] = artist.artist_id

        artist_route = '/admin/' + str(artist.alias)

        return redirect(artist_route)
    else:
        return render_template('login.html')


# create customer route
@app.route('/profile/<customer_route>')
def customer_profile(customer_route):

    customer_route_list = customer_route.split('_')
    customer_id = customer_route_list[-1]
    customer_id_int = int(customer_id)

    if session["customer_id"] == customer_id_int:
        customer = Customer.query.get(customer_id_int)

        return render_template("customerProfile.html", customer=customer)
    else:
        return redirect('/login')


# create artist route
@app.route('/admin/<alias>')
def artist_profile(alias):

    artist = Artist.query.filter(Artist.alias == alias).first()

    if session['artist_id'] == artist.artist_id:

        return render_template("artistProfile.html", artist=artist)
    else:
        return redirect('/login')


# create register customer route
@app.route('/profile')
def profile():
    return render_template('createAccount.html')


@app.route('/profile', methods=['POST'])
def create_profile():

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')

    user = Customer.query.filter(Customer.email == email).first()
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.createProfile(fname, lname, email, phone, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")
        return redirect("/login")

        # # create item route
        # @app.route('/gallery/<item>')
        # def item():
        #     return render_template("item.html")

        # # create cart route
        # @app.route('/cart')
        # def cart():
        #     return render_template("cart.html")

        # # create checkout route / order
        # @app.route('/checkout')
        # def checkout():
        #     return render_template("checkout.html")
if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5008)
