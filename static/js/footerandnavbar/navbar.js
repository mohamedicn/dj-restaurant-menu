let navbar = document.querySelector('.navbar');
let menu = document.querySelector('#menu-btn');
let cartItem = document.querySelector('.cart-items-container');
let searchForm = document.querySelector('.search-form');
let search_btn = document.querySelector('#search-btn');
let cart_btn = document.querySelector('#cart-btn');



menu.onclick = () =>{
  navbar.classList.toggle('active');
  searchForm.classList.remove('active');
  cartItem.classList.remove('active');
}



search_btn.onclick = () =>{
  searchForm.classList.toggle('active');
  navbar.classList.remove('active');
  cartItem.classList.remove('active');
}


cart_btn.onclick = () =>{
  cartItem.classList.toggle('active');
  navbar.classList.remove('active');
  searchForm.classList.remove('active');
}