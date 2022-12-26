from flask import Flask, render_template, request, flash, session, redirect, flash
from model import connect_to_db, db, FavoriteItem
from jinja2 import StrictUndefined
import crud
import helper


# create the flask app
app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined


# create home route for GET request
@app.route('/')
def homepage():

    # get login or logout depending if a customer/artist is logged in or not
    login_button = helper.switch_profile_login(session)

    # query all artists to display on homepage
    artist = crud.get_artist()

    # render an html and pass artists and login_button as data
    return render_template("index.html",  artists=artist, login_button=login_button)


# create home route for POST request
@app.route('/', methods=['POST'])
def logout_delete():

    # get data from form - logout or delete account button
    logout = request.form.get('logout') == 'logout'
    delete = request.form.get('delete_account') == 'delete account'

    # if the logout was clicked then set the session keys to None
    if logout:
        print('logged out')
        session['customer_id'] = None
        session['artist_id'] = None

    # if delete was clicked then delete the account from the db
    elif delete:
        crud.deleteProfileById(session['customer_id'])
        db.session.commit()

    # finally go back to the home route for GET request
    return redirect('/')


# create the dynamic artist gallery route - the dynamic part is given by the artist <alias> of the artist which was selected on the client side
@app.route('/gallery/<alias>')
def gallery(alias):

    # Given the artist alias, query the artist selected and pass the required info (all of it?) to the template
    artist_user = crud.get_artist_alias(alias)

    # get login or logout depending if a customer/artist is logged in or not
    login_button = helper.switch_profile_login(session)

    # favourite logic
    button_label_dict = {}
    for item in artist_user.item:
        button_label_dict[item.item_id] = 'no'
        for favitem in item.favitem:
            if session.get('customer_id', None) == favitem.customer_id:
                button_label_dict[favitem.item_id] = 'yes'

    # render the gallery.html and pass the selected artist, the login button and the logged in customer (if any - if not pass None) as data
    return render_template("gallery.html", artist=artist_user, login_button=login_button, button_label_dict=button_label_dict)


# create login route
@app.route('/login')
def login():

    # get request from client to retrieve user input in the server
    user_email = request.args.get('email')
    user_password = request.args.get('password')

    # query from the database if the email and password exist under the same account
    customer = crud.get_customer_login(user_email, user_password)
    artist = crud.get_artist_login(user_email, user_password)

    # if no user or email were entered then re-render the login page
    # could also add this as a requirement in the form (e.g. min length on inputs)
    if not user_email or not user_password:
        return render_template('login.html')

    # check if customer query above checks out - if it does, redirect to be below customer route
    elif customer:

        # add the logged in customer to the session
        session['customer_id'] = customer.customer_id

        # get the customer route since it is a dynamic route depending on the logged in customer
        customer_route = helper.get_customer_route(customer)

        # go to the customer route
        return redirect(customer_route)

    # check if artist query above checks out - if it does, redirect to be below artist route
    elif artist:

        # add the logged in artist to the session
        session['artist_id'] = artist.artist_id

        # get the artist route since it is a dynamic route depending on the logged in artist
        artist_route = helper.get_artist_route(artist)

        # go to the artist route
        return redirect(artist_route)

    # if no artist or customer were found then do not login and re route to the login route
    else:
        return redirect('/login')


# create the dynamic customer profile route - the dynamic part is given by the <customer_route> which is made of the customer fname + lname + _ + id
@app.route('/profile/<customer_route>')
def customer_profile(customer_route):

    # tokenize the customer route so we can get the id
    customer_route_list = customer_route.split('_')

    # retrieve the id and convert it to an integer
    customer_id = customer_route_list[-1]
    customer_id_int = int(customer_id)

    # if a customer is logged in (so if there is an id stored in the session) then go to the customer profile
    if session["customer_id"] == customer_id_int:

        # get the customer by the id that we retrieved from the route
        customer = crud.get_customer_id(customer_id_int)

        # render the customer profile and pass the logged in customer to the client
        return render_template("customerProfile.html", customer=customer)

    # if no customer is logged in the go to the login page
    else:
        return redirect('/login')


# create the dynamic artist profile route - the dynamic part is given by the <alias> which is made of the artist alias
@app.route('/admin/<alias>')
def artist_profile(alias):

    # get the artist from the alias
    artist = crud.get_artist_alias(alias)

    # if the artist is logged in then go then render the artist profile page
    if session['artist_id'] == artist.artist_id:

        # render the page and pass the logged in artist as data
        return render_template("artistProfile.html", artist=artist)

    # if no artist is logged in the redirect to the login page
    else:
        return redirect('/login')


# create register customer route
@app.route('/profile')
def profile():

    # simply render the create account page
    return render_template('createAccount.html')


# create new customer profile route as POST request
@app.route('/profile', methods=['POST'])
def create_profile():

    # get data posted from the form on the client side
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')

    # get the customer from their email
    user = crud.get_customer_email()

    # if a customer with that email was found in the db then tell the user that that email has already been used
    if user:
        flash("Cannot create an account with that email. Try again.")

    # otherwise create the new profile with the data received from the form
    else:
        user = crud.createProfile(fname, lname, email, phone, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

        # after having created the account redirect to the login route
        return redirect("/login")


# TODO: create cart route
@app.route('/cart')
def cart():
    login_button = helper.switch_profile_login(session)
    return render_template("cart.html", login_button=login_button)


# create add item route - GET request
@app.route('/addItem', methods=['GET'])
def newItemForm():

    # when its a get request just render the html without doing anything
    return render_template('addItem.html')


# create add item route - POST request
@app.route('/addItem', methods=['POST'])
def addItem():

    # get the data posted by the form
    description = request.form.get('description')
    dimensions = request.form.get('dimensions')
    price = request.form.get('price')
    date = request.form.get('date')
    color = request.form.get('color')
    in_stock = True  # request.form.get('in_stock')
    picture_path = request.form.get('picture_path')

    # get the artist by using the logged in artist (since they will be the ones adding the item)
    artist = crud.get_artist_id(session['artist_id'])

    # create a new item with the data from the form and the logged in artist (since an item belongs to an artist)
    item = crud.create_item(
        description, dimensions, price, date, color, in_stock, picture_path, session['artist_id'])
    db.session.add(item)
    db.session.commit()
    flash("new item has been created")

    # once the item has been added to the db redirect to the artists profile page
    return redirect('/admin/' + artist.alias)


# create favitem route - POST request
@app.route('/add-favorite-item', methods=['POST'])
def add_fav_item():

    # add a favorite item to the database
    item_id = request.json.get('itemId')
    customer_id = session.get("customer_id", None)

    # check if customer is login - if its not, redirect to login
    if customer_id == None:
        return redirect('/login')

    else:
        # Query a favorite item using both customer id and item id
        favitem = FavoriteItem.query.filter((FavoriteItem.customer_id == customer_id) & (
            FavoriteItem.item_id == item_id)).first()

        if favitem:
            crud.delete_fav_item(customer_id, item_id)
            db.session.commit()
            switch = False
        else:

            fav_item = crud.create_fav_item(customer_id, item_id)
            db.session.add(fav_item)
            db.session.commit()
            switch = True

        return {
            'success': True,
            'status': switch
        }


# create checkout route / order
@app.route('/checkout')
def checkout():
    return render_template("checkout.html")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5001)
