"use strict";

// query all like buttons using the class .itemLikeButton
let likeButtons = document.querySelectorAll(".itemLikeButton");

// loop through each button and create an event listener for each
for (let button of likeButtons) {
  button.addEventListener("click", (evt) => {
    // avoid the default behavior to not reload the page
    evt.preventDefault();

    // tokenize the button_id string by _ and get last element in the array which is the item_id as a string
    let buttonIdArray = button.id.split("_");
    let itemId = buttonIdArray.at(-1);

    // do a post request to the server sending the item_id
    fetch("/add-favorite-item", {
      method: "POST",
      body: JSON.stringify({ itemId: itemId }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      // use the response (promise) from the server and convert it to a JSON
      .then((response) => response.json())
      .then((responseJson) => {
        // when the json promise is fulfilled, check if the server is sending a customer_logged_in = True flag
        if (responseJson.customer_logged_in == true) {
          // if the customer is logged in, toggle between like and unlike for the button depending on whether or not the favitem object has been or removed from the db
          if (responseJson.added_item == true) {
            button.innerHTML = "unlike";
          } else if (responseJson.added_item == false) {
            button.innerHTML = "like";
          }
        } else {
          // if the customer is not logged in, redirect the user to the login page
          window.location.href = "/login";
        }
      });
  });
}

// ///////////////////////////////////////////

// query all like buttons using the class .itemCartButton
let cartButtons = document.querySelectorAll(".itemCartButton");

// loop through each button and create an event listener for each
for (let button of cartButtons) {
  button.addEventListener("click", (evt) => {
    // avoid the default behavior to not reload the page
    evt.preventDefault();
    // tokenize the button_id string by _ and get last element in the array which is the item_id as a string
    let buttonIdArray = button.id.split("_");
    let itemId = buttonIdArray.at(-1);

    // do a post request to the server sending the item_id
    fetch("/add-cart-item", {
      method: "POST",
      body: JSON.stringify({ itemId: itemId }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      // use the response (promise) from the server and convert it to a JSON
      .then((response) => response.json())
      .then((responseJson) => {
        // if the customer is logged in, toggle between like and unlike for the button depending on whether or not the favitem object has been or removed from the db
        if (responseJson.added_item == true) {
          button.innerHTML = "remove from cart";
        } else if (responseJson.added_item == false) {
          button.innerHTML = "add to cart";
        }
      });
  });
}

let editCartButton = document.querySelectorAll(".editCartButton");

for (let button of editCartButton) {
  button.addEventListener("click", (evt) => {
    evt.preventDefault();

    let buttonIdArray = button.id.split("_");
    let itemId = buttonIdArray.at(-1);

    fetch("/add-cart-item", {
      method: "POST",
      body: JSON.stringify({ itemId: itemId }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      // use the response (promise) from the server and convert it to a JSON
      .then((response) => response.json())
      .then((responseJson) => {
        let liItem = button.parentElement;
        let ulArtist = liItem.parentElement;

        // if the ul only has one li and one h2 (so 2 elements in total) then delete it
        if (ulArtist.children.length == 2) {
          ulArtist.remove();
        } else {
          liItem.remove();
        }
      });
  });
}

let artistButton = document.querySelector(".artistLikeButton");

if (artistButton != null) {
  artistButton.addEventListener("click", (evt) => {
    // avoid the default behavior to not reload the page
    evt.preventDefault();
    // tokenize the button_id string by _ and get last element in the array which is the artist_id as a string
    let buttonIdArray = artistButton.id.split("_");
    let artistId = buttonIdArray.at(-1);
    // do a post request to the server sending the artist_id
    fetch("/add_fav_artist", {
      method: "POST",
      body: JSON.stringify({ artistId: artistId }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      // use the response (promise) from the server and convert it to a JSON
      .then((response) => response.json())
      .then((responseJson) => {
        // when the json promise is fulfilled, check if the server is sending a customer_logged_in = True flag
        if (responseJson.customer_logged_in == true) {
          // if the customer is logged in, toggle between like and unlike for the button depending on whether or not the favitem object has been or removed from the db
          if (responseJson.added_artist == true) {
            artistButton.innerHTML = "unlike";
          } else if (responseJson.added_artist == false) {
            artistButton.innerHTML = "like";
          }
        } else {
          // if the customer is not logged in, redirect the user to the login page
          window.location.href = "/login";
        }
      });
  });
}
