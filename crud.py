from model import connect_to_db, db, Customer, Item


def createProfile(fname, lname, email, phone, password):
    """Create and return a new user."""

    user = Customer(fname=fname, lname=lname, email=email,
                    phone=phone, password=password)

    return user


def deleteProfileById(id):
    Customer.query.filter(Customer.customer_id == id).delete()


def createItem(description, dimensions, price, date, color, in_stock, picture_path, artist_id):

    item = Item(description=description, dimensions=dimensions, price=price,
                date=date, color=color, in_stock=in_stock, picture_path=picture_path, artist_id=artist_id)

    return item


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
