# import sqlalchemy class from the flak-sqlalchemy module
from flask_sqlalchemy import SQLAlchemy

# create an object from the class sqlalchemy
db = SQLAlchemy()

# create customer class


class Customer(db.Model):

    # create customers table
    __tablename__ = 'customers'

    # create attributes
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String(11))
    password = db.Column(db.String(10))

    # add relationships
    orders = db.relationship('Order', back_populates='customers')
    items = db.relationship('Customer', back_populates='customers')
    artists = db.relationship('Artist', back_populates='customers')

    # class representation
    def __repr__(self):
        return f'<Customer id={self.id} fname={self.fname} lname={self.lname} email={self.email} phone={self.phone}>'

# create order class


class Order(db.Model):

    # create orders table
    __tablename__ = 'orders'

    # create attributes
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.Date)
    total = db.Column(db.Float)
    status = db.Column(db.String)
    transaction_id = db.Column(db.String)

    # add foreign keys
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id)'))
    ship_id = db.Column(db.Integer, db.ForeignKey('shipments.id)'))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id)'))

    # add relationships
    items = db.relationship('Item', back_populates='orders')
    customers = db.relationship('Customer', back_populates='orders')
    artists = db.relationship('Artist', back_populates='orders')

    # class representation

    def __repr__(self):
        return f'<Order id={self.id} date={self.date} total={self.total} status={self.status} transaction_id={self.transaction_id}>'

# create item class


class Item(db.Model):

    # create items table
    __tablename__ = 'items'

    # create attributes
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    description = db.Column(db.Text)
    dimensions = db.Column(db.String)
    price = db.Column(db.Float)
    year = db.Column(db.Date)
    color = db.Column(db.String)
    in_stock = db.Column(db.Boolean)

    # add foreign keys
    order_id = db.Column(db.Integer, db.ForeignKey(
        'orders.id)'), Nullable=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id)'))

    # add relationship
    orders = db.relationship('Order', back_populates='items')
    customers = db.relationship('Item', back_populates='items')
    artists = db.relationship('Artist', back_populates='items')

    # class representation

    def __repr__(self):
        return f'<Item id={self.id} price={self.price} year={self.year} color={self.color} in_stock={self.in_stock}>'

# create shipment class


class Shipment(db.Model):

    # create shipments table
    __tablename__ = 'shipments'

    # create attributes
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    address1 = db.Column(db.String)
    address2 = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zipcode = db.Column(db.String)
    country = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String(11))

    # add foreign keys
    order_id = db.Column(db.Integer, db.ForeignKey(
        'orders.id)'), Nullable=True)

    # class representation
    def __repr__(self):
        return f'<Shipment id={self.id} fname={self.fname} lname={self.lname} city={self.city} state={self.state} zipcode={self.zipcode} country={self.country} email={self.email} phone={self.phone}>'

# create Artist class


class Artist(db.Model):

    # create artists table
    __tablename__ = 'artists'

    # create attributes
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String(10))
    country = db.Column(db.String)
    alias = db.Column(db.String)
    about = db.Column(db.Text)
    logo = db.Column(db.String)
    profile_pic = db.Column(db.String)
    social = db.Column(db.String)
    navbar_color = db.Column(db.String)
    footer_color = db.Column(db.String)

    # add relationships
    items = db.relationship('Item', back_populates='artists')
    orders = db.relationship('Order', back_populates='artists')

    # class representation
    def __repr__(self):
        return f'<Artist id={self.id} fname={self.fname} lname={self.lname} email={self.email} country={self.country} alias={self.alias}>'


def connect_to_db(flask_app, db_uri="postgresql:///orders", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
