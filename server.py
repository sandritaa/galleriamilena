from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db, Customer, Artist, Shipment, Order, Item, FavoriteItem, FavoriteArtist
from jinja2 import StrictUndefined
import crud
import helper

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined


# create home route
@app.route('/')
def homepage():

    login_button = helper.switch_profile_login(session)
    artist = crud.get_artist()

    return render_template("index.html",  artists=artist, login_button=login_button)


# create logout and delete account route
@app.route('/', methods=['POST'])
def logout_delete():

    logout = request.form.get('logout') == 'logout'
    delete = request.form.get('delete_account') == 'delete account'

    if logout:
        print('logged out')
        session['customer_id'] = None
        session['artist_id'] = None

    elif delete:
        crud.deleteProfileById(session['customer_id'])
        db.session.commit()

    return redirect('/')


# create artist gallery route
@app.route('/gallery/<alias>')
def gallery(alias):

    # Given the artist alias, query the artist selected and pass the required info (all of it?) to the template
    artist_user = crud.get_artist_alias(alias)

    login_button = helper.switch_profile_login(session)

    return render_template("gallery.html", artist=artist_user, login_button=login_button, customer_id=session.get('customer_id', None))


# create login route
@app.route('/login')
def login():

    # get request from client to retrieve user input in the server
    user_email = request.args.get('email')
    user_password = request.args.get('password')

    # query from the database if the email and password exist under the same account
    customer = crud.get_customer_login(user_email, user_password)
    artist = crud.get_artist_login(user_email, user_password)

    if not user_email or not user_password:
        return render_template('login.html')

    # check if customer query above checks out - if it does, redirect to be below customer route
    elif customer:

        # add a session
        session['customer_id'] = customer.customer_id

        # get customer route
        customer_route = helper.get_customer_route(customer)

        return redirect(customer_route)

    # check if artist query above checks out - if it does, redirect to be below artist route
    elif artist:

        session['artist_id'] = artist.artist_id

        artist_route = helper.get_artist_route(artist)

        return redirect(artist_route)
    else:

        return redirect('/login')


# create customer route
@app.route('/profile/<customer_route>')
def customer_profile(customer_route):

    customer_route_list = customer_route.split('_')
    customer_id = customer_route_list[-1]
    customer_id_int = int(customer_id)

    if session["customer_id"] == customer_id_int:
        customer = crud.get_customer_id(customer_id_int)

        return render_template("customerProfile.html", customer=customer)
    else:
        return redirect('/login')


# create artist route
@app.route('/admin/<alias>')
def artist_profile(alias):

    artist = crud.get_artist_alias(alias)

    if session['artist_id'] == artist.artist_id:

        return render_template("artistProfile.html", artist=artist)
    else:
        return redirect('/login')


# create register customer route
@app.route('/profile')
def profile():
    return render_template('createAccount.html')


# create new customer profile route
@app.route('/profile', methods=['POST'])
def create_profile():

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')

    user = crud.get_customer_email()
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.createProfile(fname, lname, email, phone, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")
        return redirect("/login")


# create cart route
@app.route('/cart')
def cart():
    login_button = helper.switch_profile_login(session)
    return render_template("cart.html", login_button=login_button)


# create add time route - get request
@app.route('/addItem', methods=['GET'])
def newItemForm():

    return render_template('addItem.html')


# create add item route - post request
@app.route('/addItem', methods=['POST'])
def addItem():

    description = request.form.get('description')
    dimensions = request.form.get('dimensions')
    price = request.form.get('price')
    date = request.form.get('date')
    color = request.form.get('color')
    in_stock = True  # request.form.get('in_stock')
    picture_path = request.form.get('picture_path')

    artist = crud.get_artist_id(session['artist_id'])

    item = crud.createItem(
        description, dimensions, price, date, color, in_stock, picture_path, session['artist_id'])
    db.session.add(item)
    db.session.commit()
    flash("new item has been created")

    return redirect('/admin/' + artist.alias)

    # # create item route
    # @app.route('/gallery/<item>')
    # def item():
    #     return render_template("item.html")

    # # create checkout route / order
    # @app.route('/checkout')
    # def checkout():
    #     return render_template("checkout.html")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5008)
