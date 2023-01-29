from model import Customer, Artist
import crud
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

#####################################################################
# LOGIN


# switch button between login, profile and admin
def switch_profile_login(session):

    # create an empty dictionary where the data will be stored
    button = {}

    # if a customer is logged in then change the button to 'profile' and calculate the route
    if session.get('customer_id', None):
        button['label'] = 'profile'
        customer = crud.get_customer_by_id(session['customer_id'])
        button['route'] = get_customer_route(customer)
    # if an artist is logged in then change the button to 'admin' and calculate the route
    elif session.get('artist_id', None):
        button['label'] = 'admin'
        artist = Artist.query.get(session['artist_id'])
        button['route'] = get_artist_route(artist)
    # otherwise leave 'login' as a label and set the route back to the login route
    else:
        button['label'] = 'login'
        button['route'] = '/login'
    return button


#####################################################################
# CUSTOMER


# get the dynamic route of a customer profile
def get_customer_route(customer):
    customer_route = '/profile/' + \
        str(customer.fname.lower() + customer.lname.lower() +
            '_' + str(customer.customer_id))
    return customer_route

#####################################################################
# ARTIST


# get the dynamic route of an artist profile
def get_artist_route(artist):
    artist_route = '/admin/' + str(artist.alias)
    return artist_route

#####################################################################
# FAVITEM


# get the label of the favorite item button (like or unlike)
def get_favitem_button_label(artist, session):

    # favorite logic for when the page is loaded
    button_favitem_label = {}

    # go through every item of the artist
    for item in artist.item:

        # for each item, add a label with an item_id as the key of a dictionary and set it 'like'
        button_favitem_label[item.item_id] = 'like'

        # go through every favitem of a specific item
        for favitem in item.favitem:

            # check if the customer id of the favitem is the same of the customer that is logged in (if any)
            if session.get('customer_id', None) == favitem.customer_id:

                # if its is, set the value in the dictionary of the key item_id to 'unlike'
                button_favitem_label[favitem.item_id] = 'unlike'

    return button_favitem_label

#####################################################################
# FAVARTIST


# get the label of the favorite artist button (follow or unfollow) in gallery.html
def get_favartist_button_label_gallery(artist, session):
    # favorite logic for when the page is loaded
    button_favartist_label = {}

    # for each item, add a label with an item_id as the key of a dictionary and set it 'like'
    button_favartist_label[artist.artist_id] = 'Follow'

    # go through every item of the artist
    for favartist in artist.favartist:

        # check if the customer id of the favitem is the same of the customer that is logged in (if any)
        if session.get('customer_id', None) == favartist.customer_id:

            # if its is, set the value in the dictionary of the key item_id to 'unlike'
            button_favartist_label[favartist.artist_id] = 'Unfollow'

    return button_favartist_label


#####################################################################
# CART


# get the label for cart items button when the page is first loaded (add to cart or remove from cart)
def get_cart_button_label(artist, session):

    # create an empty dictionary where the labels will be stored
    button_cart_label = {}

    # go through every item of the artist
    for item in artist.item:

        # for each item, add a label with an item_id as the key of a dictionary and set it 'like'
        button_cart_label[item.item_id] = 'add to cart'

        # check if customer is logged in
        # if it is use the db to get the correct labels
        if session.get('customer_id', None):

            # go through every favitem of a specific item
            for cartitem in item.cartitem:

                # check if the customer id of the favitem is the same of the customer that is logged in (if any)
                if session.get('customer_id', None) == cartitem.customer_id:

                    # if its is, set the value in the dictionary of the key item_id to 'unlike'
                    button_cart_label[cartitem.item_id] = 'remove from cart'

        # if the customer is not logged in use the session to get the right labels
        else:

            # check if item has been added to cart  for someone not logged in
            if item.item_id in session.get('cartitems', []):

                # if its is, set the value in the dictionary of the key item_id to 'unlike'
                button_cart_label[item.item_id] = 'remove from cart'

    return button_cart_label


# get the cart data in an organized dictionary which separates the cart items by artist
def get_cart_data(session):

    # create an emprty dictionary where the cart items will be stored and organized by artist
    cart_data = {}

    # if the customer is logged in
    if session.get('customer_id', None):

        # get the cartitems of the customer that is logged in
        cartitems = crud.get_cartitem_by_customer_id(session['customer_id'])

        # loop through all the cartitems found and add them under the artist_id key in the dictionary created previosuly
        for cartitem in cartitems:
            cart_data.setdefault(cartitem.item.artist_id,
                                 []).append(cartitem.item)

    # if the customer is not logged in
    else:

        # loop through all the item_ids added to the session dictionary under the key cartitems
        for item_id in session.get('cartitems', []):

            # for every item query the entire item
            item = crud.get_item_by_id(item_id)

            # if an item exists then add it to the cart_data dictionary under the correct artist_id key
            if item:
                cart_data.setdefault(item.artist_id, []).append(item)

    return cart_data


# get the cost data in an organized dictionary which separates the cart items by artist
def get_cost_data(session):

    # create an empty dictionary where all the cost data will be stored
    cost_data = {}

    # if the customer logged in
    if session.get('customer_id', None):

        # get the cartitems of the customer that is logged in
        cartitems = crud.get_cartitem_by_customer_id(session['customer_id'])

        # loop through all the cartitems found and add the cost rounded to two digits under the artist_id key in the dictionary created previosuly
        for cartitem in cartitems:
            cost_data[cartitem.item.artist_id] = round(cost_data.get(
                cartitem.item.artist_id, 0) + cartitem.item.price, 2)

    # if customer not logged in
    else:

        # loop through all the item_ids added to the session dictionary under the key cartitems
        for item_id in session.get('cartitems', []):

            # for every item query the entire item
            item = crud.get_item_by_id(item_id)

            # if an item exists then add the cost rounded to two digits under the artist_id key in the dictionary created previosuly
            if item:
                cost_data[item.artist_id] = round(cost_data.get(
                    item.artist_id, 0) + item.price, 2)

    return cost_data


# get the total tax to apply to the cost for each artist - apply a flat 9% tax rate
def get_tax_data(cost_data):

    # create an empty dictionary where the tax data will be stored
    tax_data = {}

    # loop through the cost_data dictionary where the keys are the artist_ids of the items in the cart and calculate a 9% tax to the subtotals of each artist
    for artist_id in cost_data:
        tax_data[artist_id] = round(cost_data[artist_id] * 9/100, 2)

    return tax_data


# get the order data separated by artist
def order_data(session):

    # create an empty list where the orders will be stored
    orders_dict = []

    # if a customer is logged in
    if session.get('customer_id', None):

        # query the customer object
        customer = crud.get_customer_by_id(session.get('customer_id'))

        # loop through each item added to the cart of the logged in customer
        for cartitem in customer.cartitem:

            # get the item corresponding of each cartitem and create a new dictionary with all required information for the client
            item = cartitem.item
            dict = {
                'item_id': item.item_id,
                'price': item.price,
                'dimensions': item.dimensions,
                'picture_path': item.picture_path,
                'alias': item.artist.alias
            }

            # append this dictionary to the list originally created
            orders_dict.append(dict)

    # if customer is not logged in
    else:

        # loop through each item_id added to the session dictionary under the key cartitems
        for item_id in session.get('cartitems', []):

            # query the item correspnding to each item_id and create a new dictionary with all required information for the client
            item = crud.get_item_by_id(item_id)
            dict = {
                'item_id': item.item_id,
                'price': item.price,
                'dimensions': item.dimensions,
                'picture_path': item.picture_path,
                'alias': item.artist.alias
            }

            # append this dictionary to the list originally created
            orders_dict.append(dict)

    return orders_dict

#####################################################################
# SENDGRID API


def twilio_api(order_id):

    #  Get order from db
    order = crud.get_order_by_id(order_id)

    # Write message
    message = f"Thank you for your order!\n\nPlease see below the updated status of order number {order.order_id}:\n\nStatus: {order.status}"

    # Send email via SendGrid
    from_email = Email("milenasatelier@gmail.com")
    to_email = "aprender.link@gmail.com"
    subject = "Galleria Milena - Order Update"
    content = Content(
        "text/plain",
        message
    )
    mail = Mail(from_email, to_email, subject, content)

    sg = SendGridAPIClient(os.environ.get('SENDGRID_KEY'))

    response = sg.send(mail)
