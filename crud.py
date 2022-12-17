from model import connect_to_db, db, Customer


def createProfile(fname, lname, email, phone, password):
    """Create and return a new user."""

    user = Customer(fname=fname, lname=lname, email=email,
                    phone=phone, password=password)

    return user


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
