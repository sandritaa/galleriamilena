from model import Customer


def switch_profile_login(session):

    button = {}
    if session['customer_id']:
        button['label'] = 'profile'
        customer = Customer.query.get(session['customer_id'])
        button['route'] = get_customer_route(customer)
    else:
        button['label'] = 'login'
        button['route'] = '/login'

    return button


def get_customer_route(customer):
    customer_route = '/profile/' + \
        str(customer.fname.lower() + customer.lname.lower() +
            '_' + str(customer.customer_id))
    return customer_route
