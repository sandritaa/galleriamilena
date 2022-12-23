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
        button.classList.add("new-color");
      });

    // change color of button
  });
}
