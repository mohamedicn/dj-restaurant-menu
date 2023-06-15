let selectedProducts = JSON.parse(localStorage.getItem('selectedProducts'));

let nameEl = document.getElementById('name');
let priceEl = document.getElementById('price');
let categoryEl = document.getElementById('category');
let imageEl = document.getElementById('image');

selectedProducts.forEach(product => {
  nameEl.textContent = product.name;
  priceEl.textContent = `$${product.price.toFixed(2)}`;
  categoryEl.textContent = product.category;
  imageEl.innerHTML = `<img src="${product.image}" alt="${product.name}">`;
});


