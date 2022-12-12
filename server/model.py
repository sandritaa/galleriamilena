# import sqlalchemy class from the flak-sqlalchemy module 
from flask_sqlalchemy import SQLAlchemy

# create an object from the class sqlalchemy 
db = SQLAlchemy()

# create customer class
class Customer(db.Model):

    # create customers table 
    __tablename__ = 'customers'

    # create attributes
    id = db.Column(db.Integer, autoincrement=True, primaryKey= True)
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
    id = db.Column(db.Integer, autoincrement=True, primaryKey= True)
    date = db.Column(db.DateTime)
    total = db.Column(db.Float)
    # TODO: mandalart #15 add stripe api
    payment_id = db.Column(db.String) 
    status = db.Column(db.String)
    # add foreign keys 
    customer_id = db.Column(db.Integer, db.ForeignKey ('customers.id)'))
    ship_id = db.Column(db.Integer, db.ForeignKey ('shippings.id)'))
    bill_id = db.Column(db.Integer, db.ForeignKey ('billing.id)'))

    # class representation 
    def __repr__(self):
         return f'Order {self.id} {self.date} {self.total} {self.payment_id} {self.status}'

# create mandala class
class Mandala(db.Model):

    # create mandalas table 
    __tablename__ = 'mandalas'

    # create attributes
    id = db.Column(db.Integer, autoincrement=True, primaryKey= True)
    description = db.Column(db.Text)
    dimensions = db.Column(db.String)
    price = db.Column(db.Float) 
    year = db.Column(db.DateTime)
    color = db.Column(db.String)
    in_stock= db.Column(db.Boolean)
     # add foreign keys 
    order_id = db.Column(db.Integer, db.ForeignKey ('orders.id)'), Nullable = True)
   
    # class representation 
    def __repr__(self):
        return f'Art {self.id} {self.description} {self.price} {self.year} {self.color} {self.in_stock}'
