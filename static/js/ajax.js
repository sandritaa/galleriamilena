"use strict";

// FAVORITE ITEM IN GALLERY - BUTTON EVENT
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
    fetch("/add_favorite_item", {
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

// CART ITEM IN GALLERY - BUTTON EVENT
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
    fetch("/add_cart_item", {
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

// REMOVE CART ITEM FROM CART - BUTTON EVENT
// query all like buttons using the class .editCartButton
let removeItemCartButton = document.querySelectorAll(".removeItemCartButton");

// loop through each button and create an event listener for each
for (let button of removeItemCartButton) {
  button.addEventListener("click", (evt) => {
    // avoid the default behavior to not reload the page
    evt.preventDefault();
    // tokenize the button_id string by _ and get last element in the array which is the item_id as a string
    let buttonIdArray = button.id.split("_");
    let itemId = buttonIdArray.at(-1);
    let artistId = buttonIdArray.at(-2);

    // do a post request to the server sending the item_id
    fetch("/add_cart_item", {
      method: "POST",
      body: JSON.stringify({ itemId: itemId }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      // use the response (promise) from the server and convert it to a JSON
      .then((response) => response.json())
      .then((responseJson) => {
        // Get cost data and total cost from the response from the server
        let costData = responseJson.cost_data;
        let totalCost = responseJson.total_cost;

        // Get elements to remove - get the card of the artist
        let cartCard = document.getElementById("cartCard_" + artistId);

        // Then modify the cost for the right artist
        cartCard.lastElementChild.innerHTML =
          "<b>Subtotal: </b>$" + costData[artistId];

        // Update total - get cartSummary first
        let cartTotal = document.getElementById("cartTotalCost");
        cartTotal.innerHTML = "<b>Total: </b>$" + totalCost;

        // if the cardBody only has one h5, one p and one cartItemCard (the one that is being removed) then delete it
        if (cartCard.children.length <= 3) {
          cartCard.remove();
        } else {
          let cartItemCard = document.getElementById("cartItemCard_" + itemId);
          cartItemCard.remove();
        }
        // if the total cost is zero, reload the page
        if (totalCost <= 0) {
          window.location.reload();
        }
      });
  });
}

// FOLLOW ARTIST FROM HOME AND GALLERY - BUTTON EVENT
// query all like buttons using the class .artistLikeButton
let artistButton = document.querySelectorAll(".artistLikeButton");

// loop through each button and create an event listener for each
for (let button of artistButton) {
  button.addEventListener("click", (evt) => {
    // avoid the default behavior to not reload the page
    evt.preventDefault();
    // tokenize the button_id string by _ and get last element in the array which is the artist_id as a string
    let buttonIdArray = button.id.split("_");
    let artistId = buttonIdArray.at(-1);
    // do a post request to the server sending the artist_id
    fetch("/add_favorite_artist", {
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
            button.innerHTML = "Unfollow";
          } else if (responseJson.added_artist == false) {
            button.innerHTML = "Follow";
          }
        } else {
          // if the customer is not logged in, redirect the user to the login page
          window.location.href = "/login";
        }
      });
  });
}

// UPDATE ORDER STATUS FROM ARTIST ADMIN PAGE - BUTTON EVENT
// query all like buttons using the class .statusButton
let statusButton = document.querySelectorAll(".statusButton");

// loop through each button and create an event listener for each
for (let button of statusButton) {
  button.addEventListener("change", (evt) => {
    // avoid the default behavior to not reload the page
    evt.preventDefault();
    // tokenize the button_id string by _ and get last element in the array which is the order_id and status a string
    let buttonIdArray = button.id.split("_");
    let orderId = buttonIdArray.at(-1);
    let statusElement = document.getElementById("status" + "_" + orderId);
    let statusOption = statusElement.value;
    // do a post request to the server sending the order_id and order status
    fetch("/artist_order_update", {
      method: "POST",
      body: JSON.stringify({ orderId: orderId, statusOption: statusOption }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      // use the response (promise) from the server and convert it to a JSON
      .then((response) => response.json())
      .then((responseJson) => {
        // modify the status of the order
        statusElement.value = responseJson.status_option;
      });
  });
}

// REMOVE ITEM FROM ARTIST ADMIN PAGE - BUTTON EVENT
// query all like buttons using the class .removeItemButton
let removeItemButton = document.querySelectorAll(".removeItemButton");

// loop through each button and create an event listener for each
for (let button of removeItemButton) {
  button.addEventListener("click", (evt) => {
    // avoid the default behavior to not reload the page
    evt.preventDefault();
    // tokenize the button_id string by _ and get last element in the array which is the item_id as a string
    let buttonIdArray = button.id.split("_");
    let itemId = buttonIdArray.at(-1);
    // do a post request to the server sending the item_id
    fetch("/artist_remove_item", {
      method: "POST",
      body: JSON.stringify({ itemId: itemId }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      // use the response (promise) from the server and convert it to a JSON
      .then((response) => response.json())
      .then((responseJson) => {
        // get the correct element to remove
        let removeItemCard = document.getElementById(
          "removeItemCard_" + itemId
        );
        // remove the item
        removeItemCard.remove();
      });
  });
}

// SET BILLING EQUAL TO SHIPPING
// query checkbox
let billingIsShipping = document.getElementById("billingIsShipping");

if (billingIsShipping) {
  billingIsShipping.addEventListener("click", (evt) => {
    // avoid the default behavior to not reload the page
    evt.preventDefault();
    // do a get request from the server to get shipping information
    fetch("/set_billing_to_shipping", {
      method: "GET",
    })
      // use the response (promise) from the server and convert it to a JSON
      .then((response) => response.json())
      .then((responseJson) => {
        // get all input fields
        let inputs = document.querySelectorAll(
          "form input[type='text'], form input[type='email']"
        );

        // if the checkbox is marked then unmark it and set all the fields to enabled and empty the value
        if (billingIsShipping.checked) {
          // uncheck the checkmark
          billingIsShipping.checked = false;
          // loop through every field of the inputs
          for (let input of inputs) {
            // for each input set it to enabled by setting disabled to false
            input.disabled = false;
            // for each input set the value to an empty string
            input.value = "";
          }
          // if the checkbox is unmarked then mark it and set all the fields to the same as the shipping
        } else {
          // check the checkmark
          billingIsShipping.checked = true;
          // loop through every field of the inputs
          for (let input of inputs) {
            // for each input set it to disabled by setting disabled to true
            input.disabled = true;
            // for each input set the value to the value stored in the shipment disctionary sent by the server
            // and using as keys the name attribute of the input (which is the same as the one in the dictionaru)
            input.value = responseJson.shipment[input.name];
          }
        }
      });
  });
}
