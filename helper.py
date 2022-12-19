from model import Customer, Artist


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
