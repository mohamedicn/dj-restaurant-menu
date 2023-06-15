let list = document.querySelectorAll(".list li");
let box = document.querySelectorAll(".box");

list.forEach((el)=>{
    el.addEventListener("click" , (e)=>{
        list.forEach((el1)=>{
            el1.style.color = "#fff";
        })
        e.target.style.color = "#ff8000"
        box.forEach((el2)=>{
            el2.style.display = "none";
        })
        document.querySelectorAll(e.target.dataset.color).forEach((el3)=>{
          el3.style.display = "flex";
        })
      })
    })
    
    
    function addToCart(name, price, category) {
      const product = { name, price, category };
      const cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
      if (cartItems.length < 12 ) {
        cartItems.push(product);
        localStorage.setItem('cartItems', JSON.stringify(cartItems));
        updateCartCount();
      } else {
        const alertBox = document.getElementById('alertBox');
        alertBox.innerText = 'You can only add up to 12 items to your cart.';
        alertBox.classList.add('show');
        setTimeout(() => {
          alertBox.classList.remove('show');
        }, 4500);
        updateCartCount();
      }
    }
    
    
    function removeCart(name, price, category) {
      const product = { name, price, category };
      const cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
      const index = cartItems.findIndex(p => p.name === product.name && p.price === product.price && p.category === product.category);
      if (index !== -1) {
        cartItems.splice(index, 1);
        localStorage.setItem('cartItems', JSON.stringify(cartItems));
        updateCartCount();
      }
    }
    
    function updateCartCount() {
      const cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
      const mySpan = document.getElementById('mySpan');
      mySpan.innerText = cartItems.length;
      
    }
    



    // $(document).ready(function() {
    //   $('#fetch-data-btn').click(function() {
    //     $.ajax({
    //       url: '{% url "fetch_data" %}',
    //       type: 'GET',
    //       dataType: 'json',
    //       success: function(data) {
    //         // Handle the response data and update the page
    //       }
    //     });
    //   });
    // });


let popup = document.getElementById('popup');
function OpenPopup() {
    popup.classList.add('open-popup');
}
function ClosePopup() {
    popup.classList.remove('open-popup');
}

