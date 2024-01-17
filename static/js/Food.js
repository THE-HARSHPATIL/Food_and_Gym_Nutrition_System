let cartIsOpen = false;
const cartContainer = document.getElementById("cart-container");
const cartButton = document.querySelector(".cart-button");

// Function to open the cart sidebar
function openCart() {
    cartIsOpen = true;
    cartContainer.style.right = "0";
}

// Function to close the cart sidebar
function closeCart() {
    cartIsOpen = false;
    cartContainer.style.right = "-300px";
}

let cartItems = [];

function addToCart(productName, price) {
    const item = { productName, price };
    cartItems.push(item);

    updateCartUI();
}

function removeItem(index) {
    cartItems.splice(index, 1);
    updateCartUI();
}

function updateCartUI() {
    const cartItemsList = document.getElementById("cart-items");
    const cartTotal = document.getElementById("cart-total");
    cartItemsList.innerHTML = "";

    let total = 0;

    cartItems.forEach((item, index) => {
        const listItem = document.createElement("li");
        const removeButton = document.createElement("span");
        removeButton.className = "remove-button";
        removeButton.innerHTML = "Remove";
        removeButton.onclick = function() {
            removeItem(index);
        };

        listItem.innerText = `${item.productName} - ${item.price} Kcal `;
        listItem.appendChild(removeButton);
        cartItemsList.appendChild(listItem);
        total += item.price;
    });

    cartTotal.innerText = total;
}
function showPopup(popupId) {
  document.getElementById(popupId).style.display = "flex";
}

// Function to close a specific popup
function closePopup(popupId) {
  document.getElementById(popupId).style.display = "none";
}

// Add event listeners to each "Show Popup" button
const showPopupButtons = document.querySelectorAll(".showPopupButton");
showPopupButtons.forEach((button, index) => {
  button.addEventListener("click", () => {
      showPopup(`popupContainer${index + 1}`);
  });
});