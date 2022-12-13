# Galleria Milena

A web application that allows an artist to showcase and sell their artwork

## Background

While there are great applications out there that help small and talented artists show off and sell their work, such as e-commerce platforms or marketplaces, most of these are not fully customizable or come with a fixed cost which can be difficult to cover for a novice in the field. The inspiration for this web application stems from the talented Iranian based artist and friend Shirin Haghi. Using materials like pens, markers and paper, she makes beautiful mandalas come to life. This web application will help her showcase her art to the rest of the world and give her the opportunity to sell it and turn her passion into her profession.

## MVP

- As a user, I want to be able to learn more about the artist
- As a user, I want to be able to add and remove art pieces in the cart
- As a user, I want to be able to complete payments and generate an order

## Tech stack

- **Database:** PostgreSQL, SQLAlchemy
- **Backend:** Python 3, Flask
- **Frontend:** React.js, Sass
- **Payment:** Stripe

### Dependencies

- Python packages:
  - SQLAlchemy
  - Flask
- APIs/external data sources:
  - Stripe API
  - Image hosting
- Browser/client-side dependencies:
  - Sass

## Server installation

To set up the repository, run the following command:

`pip3 install -r requirements.txt`

## Client installation

### Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.
