from model import Customer, Artist
import crud


def switch_profile_login(session):

    button = {}
    if session.get('customer_id', None):
        button['label'] = 'profile'
        customer = Customer.query.get(session['customer_id'])
        button['route'] = get_customer_route(customer)
    elif session.get('artist_id', None):
        button['label'] = 'admin'
        artist = Artist.query.get(session['artist_id'])
        button['route'] = get_artist_route(artist)
    else:
        button['label'] = 'login'
        button['route'] = '/login'
    return button


def get_customer_route(customer):
    customer_route = '/profile/' + \
        str(customer.fname.lower() + customer.lname.lower() +
            '_' + str(customer.customer_id))
    return customer_route


def get_artist_route(artist):
    artist_route = '/admin/' + str(artist.alias)
    return artist_route


def get_like_button_label(artist, session):

    # favorite logic for when the page is loaded
    button_like_label = {}

    # go through every item of the artist
    for item in artist.item:

        # for each item, add a label with an item_id as the key of a dictionary and set it 'like'
        button_like_label[item.item_id] = 'like'

        # go through every favitem of a specific item
        for favitem in item.favitem:

            # check if the customer id of the favitem is the same of the customer that is logged in (if any)
            if session.get('customer_id', None) == favitem.customer_id:

                # if its is, set the value in the dictionary of the key item_id to 'unlike'
                button_like_label[favitem.item_id] = 'unlike'

    return button_like_label


def get_favartist_button_label(artist, session):
    # favorite logic for when the page is loaded
    button_favartist_label = {}

    # for each item, add a label with an item_id as the key of a dictionary and set it 'like'
    button_favartist_label[artist.artist_id] = 'like'

    # go through every item of the artist
    for favartist in artist.favartist:

        # check if the customer id of the favitem is the same of the customer that is logged in (if any)
        if session.get('customer_id', None) == favartist.customer_id:

            # if its is, set the value in the dictionary of the key item_id to 'unlike'
            button_favartist_label[favartist.artist_id] = 'unlike'

    return button_favartist_label


def get_cart_button_label(artist, session):
    # cart logic for when the page is loaded
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
            if item.item_id in session.get('cartItems', []):

                # if its is, set the value in the dictionary of the key item_id to 'unlike'
                button_cart_label[item.item_id] = 'remove from cart'

    return button_cart_label


def get_cart_data(session):

    cart_data = {}

    # customer logged in
    if session.get('customer_id', None):

        cart_items = crud.get_cartitem_by_customer(session['customer_id'])

        for cart_item in cart_items:

            cart_data.setdefault(cart_item.item.artist_id,
                                 []).append(cart_item.item)

    # customer not logged in
    else:
        for item_id in session['cartItems']:
            item = crud.get_item_by_id(item_id)
            cart_data.setdefault(item.artist_id, []).append(item)

    return cart_data


def order_data(session):

    orders_dict = []

    # customer logged in
    if session.get('customer_id', None):
        customer = crud.get_customer_by_id(session.get('customer_id'))
        for cartitem in customer.cartitem:
            item = cartitem.item
            dict = {
                'item_id': item.item_id,
                'price': item.price,
                'dimensions': item.dimensions,
                'picture_path': item.picture_path,
                'alias': item.artist.alias
            }
            orders_dict.append(dict)

    # customer not logged in
    else:

        for item_id in session['cartItems']:
            item = crud.get_item_by_id(item_id)
            dict = {
                'item_id': item.item_id,
                'price': item.price,
                'dimensions': item.dimensions,
                'picture_path': item.picture_path,
                'alias': item.artist.alias
            }
            cart_data.append(dict)

    return cart_data
