# import sqlalchemy class from the flak-sqlalchemy module
from flask_sqlalchemy import SQLAlchemy

# create an object from the class sqlalchemy
db = SQLAlchemy()

# create customer class


class Customer(db.Model):

    # create customers table
    __tablename__ = 'customers'

    # create attributes
    id = db.Column(db.Integer, autoincrement=True, primaryKey=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String(11))
    password = db.Column(db.String(10))

    # class representation
    def __repr__(self):
        return f'Customer {self.id} {self.fname} {self.lname} {self.email} {self.phone}'

# create order class


class Order(db.Model):

    # create orders table
    __tablename__ = 'orders'

    # create attributes
    id = db.Column(db.Integer, autoincrement=True, primaryKey=True)
    date = db.Column(db.Date)
    total = db.Column(db.Float)
    status = db.Column(db.String)
    transaction_id = db.Column(db.String)

    # add foreign keys
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id)'))
    ship_id = db.Column(db.Integer, db.ForeignKey('shipments.id)'))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id)'))

    # class representation
    def __repr__(self):
        return f'Order {self.id} {self.date} {self.total} {self.status} {self.transaction_id}'

# create item class


class Item(db.Model):

    # create items table
    __tablename__ = 'items'

    # create attributes
    id = db.Column(db.Integer, autoincrement=True, primaryKey=True)
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

    # class representation

    def __repr__(self):
        return f'Item {self.id} {self.price} {self.year} {self.color} {self.in_stock}'

# create shipment class


class Shipment(db.Model):

    # create shipments table
    __tablename__ = 'shipments'

    # create attributes
    id = db.Column(db.Integer, autoincrement=True, primaryKey=True)
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
        return f'Shipment {self.id} {self.fname} {self.lname} {self.city} {self.state} {self.zipcode} {self.country} {self.email} {self.phone}'

# create invoice class


class Artist(db.Model):

    # create invoices table
    __tablename__ = 'artists'

    # create attributes
    id = db.Column(db.Integer, autoincrement=True, primaryKey=True)
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

    # class representation
    def __repr__(self):
        return f'Invoice {self.id} {self.fname} {self.lname} {self.email} {self.country} {self.alias}'
