# Galleria Milena

Galleria Milena is a web application that allows multiple artists to showcase and sell their artwork. As an artist, you can upload your art pieces to the web application using the Cloudinary API and sell them through your own personalized virtual gallery. You can also view all the orders you have in place and send order updates directly to your customer’s inbox using the Twilio SendGrid API. As a customer, you can view all of the artists galleries and purchase a variety items from multiple artists in one transaction. As a subscribed customer, you are also able to like different art pieces, follow artists and keep track of your orders.

![alt text](/static/styles/img/home.png)

## Background

While there are great applications out there that help small and talented artists show off and sell their work, such as e-commerce platforms or marketplaces, most of these come with fees and costs which can be difficult to cover for a novice in the field. The inspiration for this web application stems from the talented Iranian based artist and friend Shirin Haghi. Using materials like pens, markers and paper, she makes beautiful mandalas come to life. This web application will help her and other artists showcase their art to the rest of the world and give them the opportunity to sell it and turn their passion into their profession.

## MVP

- As a user, I want to be able to learn more about the artist
- As a user, I want to be able to add and remove art pieces in the cart
- As a user, I want to be able to like art pieces and artists

## Tech stack

- **Database:** PostgreSQL, SQLAlchemy
- **Backend:** Python 3, Flask
- **Frontend:** JavaScript, Jinja, Bootstrap, HTML, CSS

### Dependencies

- Python packages:
  - SQLAlchemy
  - Flask
- APIs/external data sources:
  - Cloudinary API
  - Twilio SendGrid API
- Browser/client-side dependencies:
  - Bootstrap
  - Cloudinary Upload Widget

## Installation

To set up the repository, run the following command:

`pip3 install -r requirements.txt`
