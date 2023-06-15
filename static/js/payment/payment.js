// Retrieve the data from local storage
const selectedProducts = JSON.parse(localStorage.getItem('cartItems'));

const right = document.getElementById('right');
const left = document.getElementsByClassName('left');

// Function to calculate the total price of all selected products
const calculateTotalPrice = () => {
  const totalPrice = selectedProducts.reduce((total, product) => total + parseFloat(product.price), 0);
  return totalPrice.toFixed(2);
};

// Update the total-products paragraph with the total price
const totalProductsElement = document.getElementById('total-products');
totalProductsElement.textContent = `Your Total Price Is: ${calculateTotalPrice()} $`;

selectedProducts.forEach((product, index) => {
  const { name, price, category, image } = product;
  
  const productContainer = document.createElement('div');
  productContainer.classList.add('product');
  
  const nameElement = document.createElement('h3');
  nameElement.textContent = name;
  productContainer.appendChild(nameElement);
  
  const priceElement = document.createElement('section');
  priceElement.textContent = price;
  productContainer.appendChild(priceElement);
  
  const categoryElement = document.createElement('article');
  categoryElement.textContent = category;
  productContainer.appendChild(categoryElement);

  const removeButton = document.createElement('button');
  removeButton.textContent = 'Remove';
  removeButton.addEventListener('click', () => {
    // Remove the product from the HTML
    productContainer.remove();
    // Remove the product from the local storage
    selectedProducts.splice(index, 1);
    localStorage.setItem('cartItems', JSON.stringify(selectedProducts));
    // Update the total-products paragraph with the new total price
    totalProductsElement.textContent = `Your Total Price Is: ${calculateTotalPrice()} $`;
  });
  productContainer.appendChild(removeButton);
  
  right.appendChild(productContainer);
});







  // $(document).ready(function() {
  //   $('#fetch-data-btn').click(function() {
  //     $.ajax({
  //       url: '{% url "fetch_data" %}',
  //       type: 'GET',
  //       dataType: 'json',
  //       success: function(data) {
  //         // Create HTML for each item and append it to a container element
  //         var container = $('#menu-container');
  //         container.empty();
  //         for (var i = 0; i < data.data.length; i++) {
  //           var item = data.data[i];
  //           var html = '<div>';
  //           html += '<h3>' + item.name + '</h3>';
  //           html += '<p>Price: ' + item.price + '</p>';
  //           html += '<img src="' + item.image_url + '" alt="' + item.name + '">';
  //           html += '<p>Category: ' + item.category + '</p>';
  //           html += '</div>';
  //           container.append(html);
  //         }
  //       }
  //     });
  //   });
  // });












const paymentMethods = document.getElementById('payment-methods');
const paypalImg = paymentMethods.querySelector('img[alt="PayPal"]');
const pttImg = paymentMethods.querySelector('img[alt="PTT"]');
const mastercardImg = paymentMethods.querySelector('img[alt="Mastercard"]');

paypalImg.addEventListener('click', function() {
  window.location.href = 'https://www.paypal.com';
});

pttImg.addEventListener('click', function() {
  window.location.href = 'https://www.pttbank.com';
});

mastercardImg.addEventListener('click', function() {
  window.location.href = 'https://www.mastercard.com';
});
