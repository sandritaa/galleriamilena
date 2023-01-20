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
        // Get cost data and total cost
        let costData = responseJson.cost_data;
        let totalCost = responseJson.total_cost;

        // Get elements to remove
        let ulItem = button.parentElement.parentElement;
        let sectionItem =
          ulItem.parentElement.parentElement.parentElement.parentElement;
        let cardBody = sectionItem.parentElement;

        // Update subtotal - first get the artist id
        let artistString =
          sectionItem.parentElement.firstElementChild.innerHTML;
        let artistIdArray = artistString.split(" ");
        let artistId = artistIdArray.at(-1);
        cardBody.lastElementChild.innerHTML =
          "Subtotal: $" + costData[artistId];

        // Update total - get cartSummary first
        let cartSummary = cardBody.parentElement.lastElementChild;
        cartSummary.lastElementChild.firstElementChild.innerHTML =
          "Total: $" + totalCost;
        // if the cardBody  only has one h2, one hr, one br, one section and one p
        //  (so less or equal to 4 elements in total) then delete it
        if (cardBody.children.length <= 5) {
          cardBody.remove();
        } else {
          sectionItem.remove();
        }

        // if the total cost is zero, reload the page
        if (totalCost <= 0) {
          window.location.reload();
        }
      });
  });
}

let artistButton = document.querySelectorAll(".artistLikeButton");

for (let button of artistButton) {
  {
    button.addEventListener("click", (evt) => {
      // avoid the default behavior to not reload the page
      evt.preventDefault();
      // tokenize the button_id string by _ and get last element in the array which is the artist_id as a string
      let buttonIdArray = button.id.split("_");
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
}

let statusButton = document.querySelectorAll(".statusButton");
for (let button of statusButton) {
  button.addEventListener("click", (evt) => {
    evt.preventDefault();

    let buttonIdArray = button.id.split("_");
    let orderId = buttonIdArray.at(-1);

    let statusElement = document.getElementById("status" + "_" + orderId);
    let statusOption = statusElement.value;

    fetch("/artistUpdateOrder", {
      method: "POST",
      body: JSON.stringify({ orderId: orderId, statusOption: statusOption }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((responseJson) => {
        statusElement.value = responseJson.status_option;
      });
  });
}

let removeItemButton = document.querySelectorAll(".removeItemButton");

for (let button of removeItemButton) {
  button.addEventListener("click", (evt) => {
    evt.preventDefault();

    let buttonIdArray = button.id.split("_");
    let itemId = buttonIdArray.at(-1);

    fetch("/artistRemoveItem", {
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

        // if the ul only has one li and one h2 (so 2 elements in total) then delete it

        liItem.remove();
      });
  });
}
