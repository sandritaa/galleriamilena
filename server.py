
from flask import Flask, render_template, request, flash, session, redirect, flash
from model import connect_to_db, db
from jinja2 import StrictUndefined
from datetime import datetime
import crud
import helper
import keys


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
    artist = crud.get_all_artists()

    # render an html and pass artists and login_button as data
    return render_template("home.html",  artists=artist, login_button=login_button)


# create home route for POST request
@app.route('/', methods=['POST'])
def profile_logout_and_delete():

    # get data from form - logout or delete account button
    logout = request.form.get('logout') == 'logout'
    delete = request.form.get('delete_account') == 'delete account'

    # if the logout was clicked then set the session keys to None
    if logout:
        session['customer_id'] = None
        session['artist_id'] = None

    # if delete was clicked then delete the account from the db
    elif delete:
        # to delete customer profile, first the dependencies on that customer in the db have to be deleted, so favartists, favitems and order have to remove customer_id
        crud.delete_favartist_by_customer_id(session['customer_id'])
        crud.delete_favitem_by_customer_id(session['customer_id'])
        crud.delete_cartitem_by_customer_id(session['customer_id'])
        crud.update_customer_id_in_order(session['customer_id'])
        crud.delete_customer_profile(session['customer_id'])
        db.session.commit()
        session['customer_id'] = None

    # finally go back to the home route for GET request
    return redirect('/')


# create the dynamic artist gallery route - the dynamic part is given by the artist <alias> of the artist which was selected on the client side
@app.route('/gallery/<alias>')
def gallery(alias):

    # Given the artist alias, query the artist selected and pass the required info (all of it?) to the template
    artist = crud.get_artist_by_alias(alias)

    # get login or logout depending if a customer/artist is logged in or not
    login_button = helper.switch_profile_login(session)

    # favorite item button label for when the page is loaded
    button_like_label = helper.get_favitem_button_label(artist, session)

    # cart item button label for when the page is loaded
    button_cart_label = helper.get_cart_button_label(artist, session)

    # favartist button label for when the page is loaded
    button_favartist_label = helper.get_favartist_button_label_gallery(
        artist, session)

    # render the gallery.html and pass the selected artist, the login button and the favitem button label as data
    return render_template("gallery.html", artist=artist, login_button=login_button, button_like_label=button_like_label, button_cart_label=button_cart_label, button_favartist_label=button_favartist_label)


# create login route
@app.route('/login')
def login():

    # get login or logout depending if a customer/artist is logged in or not
    login_button = helper.switch_profile_login(session)

    # get request from client to retrieve user input in the server
    user_email = request.args.get('email')
    user_password = request.args.get('password')

    # query from the database if the email and password exist under the same account
    customer = crud.get_customer_by_login(user_email, user_password)
    artist = crud.get_artist_by_login(user_email, user_password)

    # if no user or email were entered then re-render the login page
    # could also add this as a requirement in the form (e.g. min length on inputs)
    if not user_email or not user_password:
        return render_template('login.html', login_button=login_button)

    # check if customer query above checks out - if it does, redirect to be below customer route
    elif customer:

        # add the logged in customer to the session
        session['customer_id'] = customer.customer_id
        session.modified = True

        # get the customer route since it is a dynamic route depending on the logged in customer
        customer_route = helper.get_customer_route(customer)

        for item_id in session.get('cartitems', []):

            cart_item_db = crud.get_cartitem(
                session.get('customer_id'), item_id)

            if not cart_item_db:

                cart_item = crud.create_cartitem(
                    session.get('customer_id'), item_id)
                db.session.add(cart_item)
                db.session.commit()

        session['cartitems'] = []
        session.modified = True

        # go to the customer route
        return redirect('/')

    # check if artist query above checks out - if it does, redirect to be below artist route
    elif artist:

        # add the logged in artist to the session
        session['artist_id'] = artist.artist_id
        session.modified = True

        # get the artist route since it is a dynamic route depending on the logged in artist
        artist_route = helper.get_artist_route(artist)

        # empty cart if an artist logs in
        session['cartitems'] = []
        session.modified = True

        # go to the artist route
        return redirect(artist_route)

    # if no artist or customer were found then do not login and re route to the login route
    else:
        return redirect('/login')


# create the dynamic customer profile route - the dynamic part is given by the <customer_route> which is made of the customer fname + lname + _ + id
@app.route('/profile/<customer_route>')
def customer_profile(customer_route):

    # get login or logout depending if a customer/artist is logged in or not
    login_button = helper.switch_profile_login(session)

    # tokenize the customer route so we can get the id
    customer_route_list = customer_route.split('_')

    # retrieve the id and convert it to an integer
    customer_id = customer_route_list[-1]
    customer_id_int = int(customer_id)

    # if a customer is logged in (so if there is an id stored in the session) then go to the customer profile
    if session.get("customer_id", None) == customer_id_int:

        # get the customer by the id that we retrieved from the route
        customer = crud.get_customer_by_id(customer_id_int)

        # render the customer profile and pass the logged in customer to the client
        return render_template("customerProfile.html", customer=customer, login_button=login_button)

    # if no customer is logged in the go to the login page
    else:
        return redirect('/login')


# create the dynamic artist profile route - the dynamic part is given by the <alias> which is made of the artist alias
@app.route('/admin/<alias>')
def artist_profile(alias):
    # get login or logout depending if a customer/artist is logged in or not
    login_button = helper.switch_profile_login(session)

    # get the artist from the alias
    artist = crud.get_artist_by_alias(alias)

    # if the artist is logged in then go then render the artist profile page
    if session['artist_id'] == artist.artist_id:

        # render the page and pass the logged in artist as data
        return render_template("artistProfile.html", artist=artist, login_button=login_button)

    # if no artist is logged in the redirect to the login page
    else:
        return redirect('/login')


# create register customer route
@app.route('/profile')
def new_customer_profile_form():

    # get login or logout depending if a customer/artist is logged in or not
    login_button = helper.switch_profile_login(session)

    # simply render the create account page
    return render_template('createAccount.html', login_button=login_button)


# create new customer profile route as POST request
@app.route('/profile', methods=['POST'])
def create_customer_profile():

    # get data posted from the form on the client side
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')

    # get the customer from their email
    user = crud.get_customer_by_email(email)

    # if a customer with that email was found in the db then tell the user that that email has already been used
    if user:
        flash("Cannot create an account with that email. Try again.")
        return redirect('/profile')

    # otherwise create the new profile with the data received from the form
    else:
        user = crud.create_customer_profile(
            fname, lname, email, phone, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

        # after having created the account redirect to the login route
        return redirect("/login")


# create add item route - GET request
@app.route('/artist_add_item')
def new_item_form():

    # get login or logout depending if a customer/artist is logged in or not
    login_button = helper.switch_profile_login(session)

    # when its a get request just render the html without doing anything
    return render_template('artistAddItem.html', login_button=login_button)


# create add item route - POST request
@app.route('/artist_add_item', methods=['POST'])
def artist_add_item():

    # get the data posted on the form - the item is always in stock if an artist adds it
    description = request.form.get('description')
    dimensions = request.form.get('dimensions')
    price = request.form.get('price')
    date = request.form.get('date')
    color = request.form.get('color')
    in_stock = True
    picture_path = request.form.get('picture_path')

    # convert date to right format
    date = datetime.strptime(date, "%Y-%m-%d")

    # get the artist by using the logged in artist (since they will be the ones adding the item)
    artist = crud.get_artist_by_id(session['artist_id'])

    # create a new item with the data from the form and the logged in artist (since an item belongs to an artist)
    item = crud.create_item(
        description, dimensions, price, date, color, in_stock, picture_path, session['artist_id'])
    db.session.add(item)
    db.session.commit()

    # once the item has been added to the db redirect to the artists profile page
    return redirect('/admin/' + artist.alias)


# create artist order update
@app.route('/artist_order_update', methods=["POST"])
def artist_order_update():

    # get the order_id and convert it to an int from the client (ajax)
    order_id = int(request.json.get('orderId'))
    status_option = request.json.get('statusOption')

    crud.update_order_status_by_id(order_id, status_option)
    db.session.commit()

    helper.twilio_api(order_id)

    return {
        'status_option': status_option
    }


# create route for artist to remove item
@app.route('/artist_remove_item', methods=["POST"])
def artist_remove_item():

    # get the order_id and convert it to an int from the client (ajax)
    item_id = int(request.json.get('itemId'))

    # in order to delete an item, it cannot be part of a cart or it cannot be a favorite item.
    # therefore, first query if it is a cartitem or a favitem and delete these cartitems and favitems
    favitems = crud.get_favitems_by_item_id(item_id)
    cartitems = crud.get_cartitems_by_item_id(item_id)

    # loop through all of the favitems found and delete the like
    for favitem in favitems:
        crud.delete_favitem_by_id(favitem.favitem_id)
        db.session.commit()

    # loop through all of the cartitems found and delete the item for the carts
    for cartitem in cartitems:
        crud.delete_cartitem_by_id(cartitem.cartitem_id)
        db.session.commit()

    # now remove the item
    crud.delete_item_by_id(item_id)
    db.session.commit()

    return {
        'success': True
    }


# create cart item route - POST request
@app.route('/add_cart_item', methods=['POST'])
def add_cart_item():

    # get the item_id and convert it to an int from the client (ajax)
    item_id = int(request.json.get('itemId'))

    # get the customer_id from the session or None if no customer is logged in
    customer_id = session.get("customer_id", None)
    artist_id = session.get("artist_id", None)

    # start by checking if an artist is logged in, if they are not
    if artist_id == None:
        # check if the customer is logged in or not
        # if the customer is NOT logged in - use session to store cartitems
        if customer_id == None:

            if item_id in session.get('cartitems', []):

                session['cartitems'].remove(item_id)
                session.modified = True
                added_item = False

            else:
                # item_id goes into my session
                session.setdefault('cartitems', []).append(item_id)
                session.modified = True
                added_item = True

        # if instead the customer is logged in - used the db to store cartitems
        else:

            # query for a cartitems
            cartitem = crud.get_cartitem(customer_id, item_id)

            # if the item is already in the cart then the item will be removed from the cart
            # use the added_item flag to send back to the front end information on whether an item has
            # been added or removed from the cart
            if cartitem:
                crud.delete_cartitem(customer_id, item_id)
                db.session.commit()
                added_item = False

            else:
                # if the item is not in the cart then the item will be added to the cart
                # use the added_item flag to send back to the front end information on whether an item has
                # been added or removed from the cart
                cart_item = crud.create_cartitem(customer_id, item_id)
                db.session.add(cart_item)
                db.session.commit()
                added_item = True

        # Recalculate cost data since that needs to be updated too
        cost_data = helper.get_cost_data(session)
        total_cost = round(sum(cost_data.values()), 2)

    # if an artist is logged in set everything to false, empty or zero as the artist cannot add items to the cart
    else:
        added_item = False
        cost_data = {}
        total_cost = 0

    return {
        # fetch response
        'added_item': added_item,
        'cost_data': cost_data,
        'total_cost': total_cost
    }


# create favitem route - POST request
@app.route('/add_favorite_item', methods=['POST'])
def add_favorite_item():

    # get the item_id and convert it to an int from the client (ajax)
    item_id = int(request.json.get('itemId'))

    # get the customer_id from the session or None if no customer is logged in
    customer_id = session.get("customer_id", None)

    # check if the customer is logged in.
    if customer_id == None:

        # if they aren't logged in, set both flags to false
        customer_logged_in = False
        added_item = False

    else:

        # if they are logged in, set the customer_logged_in to true
        customer_logged_in = True

        # Query a favorite item using both customer id and item id
        favitem = crud.get_favitem(customer_id, item_id)

        # if there is a favorite item then delete it from the db - otherwise add it
        if favitem:

            # delete the favitem from the db and set the added_item flag to false
            crud.delete_favitem(customer_id, item_id)
            db.session.commit()
            added_item = False

        else:

            # create the favitem and add it ot the db and set the added_item flag to true
            fav_item = crud.create_favitem(customer_id, item_id)
            db.session.add(fav_item)
            db.session.commit()
            added_item = True

    # return both flags to the client (ajax) so it can use them in its eventListeners
    return {
        'customer_logged_in': customer_logged_in,
        'added_item': added_item
    }


# create favartist route - POST request
@app.route('/add_favorite_artist', methods=['POST'])
def add_favorite_artist():

    artist_id = int(request.json.get('artistId'))
    customer_id = session.get('customer_id', None)

    # check if the customer is logged in.
    if customer_id == None:

        # if they aren't logged in, set both flags to false
        customer_logged_in = False
        added_artist = False

    else:

        # if they are logged in, set the customer_logged_in to true
        customer_logged_in = True

        # Query a favorite artist using both customer id and artist id
        favartist = crud.get_favartist(customer_id, artist_id)

        # if there is a favorite artist then delete it from the db - otherwise add it
        if favartist:

            # delete the favartist from the db and set the added_item flag to false
            crud.delete_favartist(customer_id, artist_id)
            db.session.commit()
            added_artist = False

        else:

            # create the favartist and add it ot the db and set the added_item flag to true
            fav_artist = crud.create_favartist(customer_id, artist_id)
            db.session.add(fav_artist)
            db.session.commit()
            added_artist = True

    # return both flags to the client (ajax) so it can use them in its eventListeners
    return {
        'customer_logged_in': customer_logged_in,
        'added_artist': added_artist
    }


# create cart route
@app.route('/cart')
def cart():
    login_button = helper.switch_profile_login(session)

    # get the cart data, cost data and total cost of the order. The cart data, cost data and tax data
    # are stored in dictionaries where the keys are the artists ids since there will be a separate order for each artist
    cart_data = helper.get_cart_data(session)
    cost_data = helper.get_cost_data(session)
    total_cost = round(sum(cost_data.values()), 2)

    return render_template("cart.html", login_button=login_button, cart_data=cart_data, cost_data=cost_data, total_cost=total_cost)


# create checkout route / order
@app.route('/shipping')
def shipping():
    # get login or logout depending if a customer/artist is logged in or not
    login_button = helper.switch_profile_login(session)

    return render_template("shippingDetails.html", login_button=login_button)


# create billing route
@app.route('/billing')
def billing():
    # get login or logout depending if a customer/artist is logged in or not
    login_button = helper.switch_profile_login(session)

    # add to session shipment information
    session['shipment'] = {
        'fname': request.args.get('fname'),
        'lname': request.args.get('lname'),
        'address1': request.args.get('address1'),
        'address2': request.args.get('address2'),
        'city': request.args.get('city'),
        'state': request.args.get('state'),
        'zipcode': request.args.get('zipcode'),
        'country': request.args.get('country'),
        'email': request.args.get('email'),
        'phone': request.args.get('phone'),
    }

    return render_template("billingDetails.html", login_button=login_button, shipping_details=session['shipment'])


# create payment route
@app.route('/payment')
def payment():
    # get login or logout depending if a customer/artist is logged in or not
    login_button = helper.switch_profile_login(session)

    return render_template("paymentDetails.html", login_button=login_button)


# create order review route
@app.route('/order_review')
def order_review():

    # get login or logout depending if a customer/artist is logged in or not
    login_button = helper.switch_profile_login(session)

    # get the cart data, cost data, tax data and total  of the order. The cart data, cost data and tax data
    # are stored in dictionaries where the keys are the artists ids since there will be a separate order for each artist
    cart_data = helper.get_cart_data(session)
    cost_data = helper.get_cost_data(session)
    tax_data = helper.get_tax_data(cost_data)
    total_tax = round(sum(tax_data.values()), 2)
    total_cost = round(sum(cost_data.values()) + sum(tax_data.values()), 2)
    total_items = round(total_cost - total_tax, 2)

    return render_template("orderReview.html", order_data=cart_data, cost_data=cost_data, tax_data=tax_data, total_cost=total_cost, total_tax=total_tax, total_items=total_items, login_button=login_button)


# create order complete route
@app.route('/order_complete')
def order_complete():

    # get login or logout depending if a customer/artist is logged in or not
    login_button = helper.switch_profile_login(session)

    # get the cart data, cost data, tax data and total cost of the order. The cart data, cost data and tax data
    # are stored in dictionaries where the keys are the artists ids since there will be a separate order for each artist
    cart_data = helper.get_cart_data(session)
    cost_data = helper.get_cost_data(session)
    tax_data = helper.get_tax_data(cost_data)
    total_tax = round(sum(tax_data.values()), 2)
    total_cost = round(sum(cost_data.values()) + sum(tax_data.values()), 2)
    total_items = round(total_cost - total_tax, 2)

    # create an empty list to store orders
    orders = []

    # loop through each artist id in the cart_data (which are the same as the ones in cost_data and tax_data)
    for artist_id in cart_data:

        # get the items that are part of the order for each artist id
        order_items = cart_data[artist_id]

        # calculate the subtotal for each order by symming the cost of the order and the tax data
        total_order = round(cost_data[artist_id] + tax_data[artist_id], 2)

        # create a new order in the db with all the information
        order = crud.create_order_by_session(session, artist_id, total_order)
        db.session.add(order)
        db.session.commit()

        # append each order to the orders list
        orders.append(order)

        # send email
        helper.twilio_api(order.order_id)

        # loop through each item in the order
        for order_item in order_items:

            # change the stock value to False as each piece is one of a kind
            in_stock = False

            # update the item stock level
            crud.update_item_with_order_by_id(
                order_item, order.order_id, in_stock)
            db.session.commit()

    # if the customer is logged in
    if session.get('customer_id', None):

        # empty the cart by removing the cartitems in the db for that customer
        crud.delete_cartitem_by_customer_id(session['customer_id'])
        db.session.commit()

    # if the customer is not logged in
    else:

        # empty the cart setting the value of the cartitems key of the session dictionary to an empty list
        session['cartitems'] = []

    return render_template("orderComplete.html", order_data=cart_data, cost_data=cost_data, tax_data=tax_data, total_cost=total_cost, total_tax=total_tax, total_items=total_items, orders=orders, login_button=login_button)


# create route to set the billing the same as the shipping
@app.route('/set_billing_to_shipping')
def set_billing_to_shipping():

    # send only the dictionary in session stored under the key shipment
    return {
        'shipment': session['shipment'],
    }


# create intro route
@app.route('/intro')
def intro():

    return render_template("intro.html")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5002)
