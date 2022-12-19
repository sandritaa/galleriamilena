# import sqlalchemy class from the flak-sqlalchemy module
from flask_sqlalchemy import SQLAlchemy

# create an object from the class sqlalchemy
db = SQLAlchemy()


# create customer class
class Customer(db.Model):

    # create customers table
    __tablename__ = 'customers'

    # create attributes
    customer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    password = db.Column(db.String(12))

    # add relationships
    order = db.relationship('Order', back_populates='customer')
    favitem = db.relationship('FavoriteItem', back_populates='customer')
    favartist = db.relationship('FavoriteArtist', back_populates='customer')

    # class representation
    def __repr__(self):
        return f'<Customer customer_id={self.customer_id} fname={self.fname} lname={self.lname} email={self.email} phone={self.phone}>'


# create artist class
class Artist(db.Model):

    # create artists table
    __tablename__ = 'artists'

    # create attributes
    artist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String(12))
    country = db.Column(db.String)
    alias = db.Column(db.String)
    about = db.Column(db.Text)
    logo = db.Column(db.String)
    profile_pic = db.Column(db.String)
    social = db.Column(db.String)

    # add relationships
    item = db.relationship('Item', back_populates='artist')
    order = db.relationship('Order', back_populates='artist')
    favartist = db.relationship('FavoriteArtist', back_populates='artist')

    # class representation

    def __repr__(self):
        return f'<Artist artist_id={self.artist_id} fname={self.fname} lname={self.lname} email={self.email} country={self.country} alias={self.alias}>'


# create shipment class
class Shipment(db.Model):

    # create shipments table
    __tablename__ = 'shipments'

    # create attributes
    shipment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    address1 = db.Column(db.String)
    address2 = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zipcode = db.Column(db.String)
    country = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)

    # class representation
    def __repr__(self):
        return f'<Shipment shipment_id={self.shipment_id} fname={self.fname} lname={self.lname} city={self.city} state={self.state} zipcode={self.zipcode} country={self.country} email={self.email} phone={self.phone}>'


# create order class
class Order(db.Model):

    # create orders table
    __tablename__ = 'orders'

    # create attributes
    order_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.DateTime)
    total = db.Column(db.Float)
    status = db.Column(db.String)
    transaction_id = db.Column(db.String)

    # add foreign keys
    customer_id = db.Column(
        db.Integer, db.ForeignKey('customers.customer_id'))
    shipment_id = db.Column(
        db.Integer, db.ForeignKey('shipments.shipment_id'))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.artist_id'))

    # add relationships
    item = db.relationship('Item', back_populates='order')
    customer = db.relationship('Customer', back_populates='order')
    artist = db.relationship('Artist', back_populates='order')

    # class representation

    def __repr__(self):
        return f'<Order order_id={self.order_id} date={self.date} total={self.total} status={self.status} transaction_id={self.transaction_id}>'


# create item class
class Item(db.Model):

    # create items table
    __tablename__ = 'items'

    # create attributes
    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    description = db.Column(db.Text)
    dimensions = db.Column(db.String)
    price = db.Column(db.Float)
    date = db.Column(db.DateTime)
    color = db.Column(db.String)
    in_stock = db.Column(db.Boolean)
    picture_path = db.Column(db.String)

    # add foreign keys
    order_id = db.Column(db.Integer, db.ForeignKey(
        'orders.order_id'), nullable=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.artist_id'))

    # add relationship
    order = db.relationship('Order', back_populates='item')
    artist = db.relationship('Artist', back_populates='item')
    favitem = db.relationship('FavoriteItem', back_populates='item')

    # class representation

    def __repr__(self):
        return f'<Item item_id={self.item_id} price={self.price} year={self.year} color={self.color} in_stock={self.in_stock}>'


# create favorite items class
class FavoriteItem(db.Model):

    # create fav items table
    __tablename__ = 'favitems'

    # create attributes
    favitem_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    # add foreign keys
    customer_id = db.Column(db.Integer, db.ForeignKey(
        'customers.customer_id'), nullable=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.item_id'))

    # add relationship
    customer = db.relationship('Customer', back_populates='favitem')
    item = db.relationship('Item', back_populates='favitem')

    # class representation

    def __repr__(self):
        return f'<FavoriteItem favitem_id={self.favitem_id} customer_id={self.customer_id} item_id={self.item_id}>'


# create favorite artists class
class FavoriteArtist(db.Model):

    # create fav artists table
    __tablename__ = 'favartists'

    # create attributes
    favartist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    # add foreign keys
    customer_id = db.Column(db.Integer, db.ForeignKey(
        'customers.customer_id'), nullable=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.artist_id'))

    # add relationship
    customer = db.relationship('Customer', back_populates='favartist')
    artist = db.relationship('Artist', back_populates='favartist')

    # class representation

    def __repr__(self):
        return f'<FavoriteArtist favartist_id={self.favartists} customer_id={self.customer_id} artist_id={self.artist_id}>'


def connect_to_db(flask_app, db_uri="postgresql:///galleriadb", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
