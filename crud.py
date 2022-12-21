from model import connect_to_db, db, Customer, Artist, Item

# CUSTOMER

# return customer email


def get_customer_email(email):
    return Customer.query.filter(Customer.email == email).first()

#  return customer login details


def get_customer_login(user_email, user_password):
    customer = Customer.query.filter((Customer.email == user_email) & (
        Customer.password == user_password)).first()
    return customer

# return customer id (integer)


def get_customer_id(customer_id_int):
    return Customer.query.get(customer_id_int)

# create and return a new user


def createProfile(fname, lname, email, phone, password):
    user = Customer(fname=fname, lname=lname, email=email,
                    phone=phone, password=password)
    return user

# delete customer profile


def deleteProfileById(id):
    return Customer.query.filter(Customer.customer_id == id).delete()


# ARTIST

# return all artists
def get_artist():
    return Artist.query.all()

# return artists ids


def get_artist_id():
    return Artist.query.get(session['artist_id'])

#  return artist login details


def get_artist_login(user_email, user_password):
    artist = Artist.query.filter((Artist.email == user_email) & (
        Artist.password == user_password)).first()
    return artist

# return alias


def get_artist_alias(alias):
    return Artist.query.filter(Artist.alias == alias).first()


# ITEM

# create and return a new item
def createItem(description, dimensions, price, date, color, in_stock, picture_path, artist_id):

    item = Item(description=description, dimensions=dimensions, price=price,
                date=date, color=color, in_stock=in_stock, picture_path=picture_path, artist_id=artist_id)

    return item


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
