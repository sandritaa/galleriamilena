
from model import *
from datetime import datetime
import os
import json
import crud


# Drop and create db
os.system('dropdb galleriadb')
os.system('createdb galleriadb')


# Connect to the db and create tables
if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    db.create_all()

# Open the json with mockdata and parse it
# Second argument "r" -> read permission - can only read file
with open("static/data/mockdata.json", "r") as json_file:
    mockdata = json.load(json_file)

# Seed artists in database
artists = mockdata['artists']
for artist in artists:
    db.session.add(crud.create_artist_profile(fname=artist['fname'], lname=artist['lname'], email=artist['email'], password=artist['password'],
                   country=artist['country'], alias=artist['alias'], about=artist['about'], profile_pic=artist['profile_pic']))
db.session.commit()

# Seed customers in database
customers = mockdata['customers']
for customer in customers:
    db.session.add(crud.create_customer_profile(
        fname=customer['fname'], lname=customer['lname'], email=customer['email'], phone=customer['phone'], password=customer['password']))
db.session.commit()

# Seed items in database
items = mockdata['items']
for item in items:
    db.session.add(crud.create_item(description=item['description'], dimensions=item['dimensions'], price=item['price'], date=datetime.strptime(
        item['date'], "%Y-%m-%d"), color=item['color'], in_stock=item['in_stock'], picture_path=item['picture_path'], artist_id=item['artist_id']))
db.session.commit()
