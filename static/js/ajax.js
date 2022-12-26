// TODO: add ajax logic for fav buttons

"use strict";

// query all like buttons using the class .itemLikeButton
let likeButtons = document.querySelectorAll(".itemLikeButton");

for (let button of likeButtons) {
  button.addEventListener("click", (evt) => {
    evt.preventDefault();
    // button.classList.remove("new-color");
    let buttonIdArray = button.id.split("_");
    let itemId = buttonIdArray.at(-1);

    fetch("/add-favorite-item", {
      method: "POST",
      body: JSON.stringify({ itemId: itemId }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((responseJson) => {
        // Check if the server is sending a success = True flag
        if (responseJson.customer_logged_in == true) {
          if (responseJson.added_item == true) {
            button.innerHTML = "unlike";
          } else if (responseJson.added_item == false) {
            button.innerHTML = "like";
          }
        } else {
          // redirect the user to the login page
          window.location.href = "/login";
        }
      });
  });
}
