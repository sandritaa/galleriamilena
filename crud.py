from model import connect_to_db, db, Customer, Artist, Item, FavoriteItem, CartItem, FavoriteArtist, Order
from sqlalchemy import func

#####################################################################
# CUSTOMER


# get customer by email
def get_customer_by_email(email):
    return Customer.query.filter(Customer.email == email).first()


# get customer by login
def get_customer_by_login(user_email, user_password):
    return Customer.query.filter((Customer.email == user_email) & (
        Customer.password == user_password)).first()


# get customer by id
def get_customer_by_id(customer_id):
    return Customer.query.get(customer_id)


# create new customer
def create_customer_profile(fname, lname, email, phone, password):
    return Customer(fname=fname, lname=lname, email=email,
                    phone=phone, password=password)


# delete customer
def delete_customer_profile(customer_id):
    Customer.query.filter(Customer.customer_id == customer_id).delete()


#####################################################################
# ARTIST

# get all artists
def get_all_artists():
    return Artist.query.all()


# get artist by id
def get_artist_by_id(artist_id):
    return Artist.query.get(artist_id)


#  get artist by login
def get_artist_by_login(email, password):
    return Artist.query.filter((Artist.email == email) & (
        Artist.password == password)).first()


# get artist by alias
def get_artist_by_alias(alias):
    return Artist.query.filter(Artist.alias == alias).first()


# create artist profile to seed database
def create_artist_profile(fname, lname, email, password, country, alias, about, profile_pic):
    return Artist(fname=fname, lname=lname, email=email, password=password, country=country,
                  alias=alias, about=about, profile_pic=profile_pic)


#####################################################################
# FAVORITE ARTIST

# get favorite artist
def get_favartist(customer_id, artist_id):
    return FavoriteArtist.query.filter((FavoriteArtist.artist_id == artist_id) & (FavoriteArtist.customer_id == customer_id)).first()


# create favorite artist
def create_favartist(customer_id, artist_id):
    return FavoriteArtist(customer_id=customer_id, artist_id=artist_id)


# delete favorite artist
def delete_favartist(customer_id, artist_id):
    FavoriteArtist.query.filter((FavoriteArtist.customer_id ==
                                 customer_id) & (FavoriteArtist.artist_id == artist_id)).delete()


# delete favorite artist by customer id
def delete_favartist_by_customer_id(customer_id):
    FavoriteArtist.query.filter(
        FavoriteArtist.customer_id == customer_id).delete()


#####################################################################
# ITEM

# get item by id
def get_item_by_id(item_id):
    return Item.query.get(item_id)


# create new item
def create_item(description, dimensions, price, date, color, in_stock, picture_path, artist_id):
    return Item(description=description, dimensions=dimensions, price=price,
                date=date, color=color, in_stock=in_stock, picture_path=picture_path, artist_id=artist_id)


# delete item by id
def delete_item_by_id(item_id):
    Item.query.filter((Item.item_id ==
                       item_id)).delete()


# update item with order_id
def update_item_with_order_by_id(item, order_id, in_stock):
    Item.query.filter(Item.item_id == item.item_id).update(
        {'order_id': order_id, 'in_stock': in_stock})


#####################################################################
# FAVORITE ITEM

# get favorite item by id
def get_favitem(customer_id, item_id):
    return FavoriteItem.query.filter((FavoriteItem.customer_id == customer_id) & (
        FavoriteItem.item_id == item_id)).first()


# get favorite items by item id
def get_favitems_by_item_id(item_id):
    return FavoriteItem.query.filter((FavoriteItem.item_id == item_id)).all()


# create favorite item
def create_favitem(customer_id, item_id):
    return FavoriteItem(customer_id=customer_id, item_id=item_id)


# delete favorite item
def delete_favitem(customer_id, item_id):
    FavoriteItem.query.filter((FavoriteItem.customer_id ==
                              customer_id) & (FavoriteItem.item_id == item_id)).delete()


# delete favorite item by id
def delete_favitem_by_id(favitem_id):
    FavoriteItem.query.filter((FavoriteItem.favitem_id == favitem_id)).delete()


# delete favorite item by customer id
def delete_favitem_by_customer_id(customer_id):
    FavoriteItem.query.filter(FavoriteItem.customer_id == customer_id).delete()


#####################################################################
# CART ITEMS

# get cart item
def get_cartitem(customer_id, item_id):
    return CartItem.query.filter(
        (CartItem.customer_id == customer_id) & (CartItem.item_id == item_id)).first()


# get cart item by customer_id
def get_cartitem_by_customer_id(customer_id):
    return CartItem.query.filter(CartItem.customer_id == customer_id).all()


# get cart items by item id
def get_cartitems_by_item_id(item_id):
    return CartItem.query.filter((CartItem.item_id == item_id)).all()


# create a cart item
def create_cartitem(customer_id, item_id):
    return CartItem(customer_id=customer_id, item_id=item_id)


# delete cart item
def delete_cartitem(customer_id, item_id):
    CartItem.query.filter((CartItem.customer_id ==
                           customer_id) & (CartItem.item_id == item_id)).delete()


# delete cart item by id
def delete_cartitem_by_id(cartitem_id):
    CartItem.query.filter((CartItem.cartitem_id == cartitem_id)).delete()


# delete cart item by customer id
def delete_cartitem_by_customer_id(customer_id):
    CartItem.query.filter(CartItem.customer_id == customer_id).delete()


#####################################################################
# ORDER

# get order by id
def get_order_by_id(order_id):
    return Order.query.get(order_id)


# create order using the session dictionary
def create_order_by_session(session, artist_id, totalOrder):
    return Order(
        status='order received',
        date=func.now(),
        total=totalOrder,
        fname=session['shipment']['fname'],
        lname=session['shipment']['lname'],
        address1=session['shipment']['address1'],
        address2=session['shipment']['address2'],
        city=session['shipment']['city'],
        state=session['shipment']['state'],
        zipcode=session['shipment']['zipcode'],
        country=session['shipment']['country'],
        email=session['shipment']['email'],
        phone=session['shipment']['phone'],
        customer_id=session.get('customer_id', None),
        artist_id=artist_id
    )


# update order status by id
def update_order_status_by_id(order_id, status_option):
    Order.query.filter(Order.order_id == order_id).update(
        {'status': status_option})


# update customer id in order
def update_customer_id_in_order(customer_id):
    Order.query.filter(Order.customer_id == customer_id).update(
        {'customer_id': None})


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
