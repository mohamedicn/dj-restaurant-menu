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
    
    
    let selectedProducts = [];
    function addToCart(name, price, category, Image) { 
      const product = {
        name: name,
        price: price,
        category: category,
        Image: Image,
      };
      console.log(product)
      selectedProducts.push(product);
      
      // Update the value of the mySpan element
      const mySpan = document.getElementById('mySpan');
      mySpan.innerText = parseInt(mySpan.innerText) + 1;
    }
       
        // set the selectedProducts array in local storage
        window.localStorage.setItem('selectedProducts', JSON.stringify(selectedProducts));
        
  function removeCart(name, price, category, Image) {
      const product = {
        name: name,
        price: price,
        category: category,
        Image: Image,
  };
  // Find the index of the product in the selectedProducts array
  const index = selectedProducts.findIndex(p => p.name === product.name);
  
  // If the product is found, remove it from the array
  if (index !== -1) {
    selectedProducts.splice(index, 1);
    
    // Update the value of the mySpan element
    const mySpan = document.getElementById('mySpan');
    mySpan.innerText = parseInt(mySpan.innerText) - 1;
  }
}







let popup = document.getElementById('popup');
function OpenPopup() {
    popup.classList.add('open-popup');
}
function ClosePopup() {
    popup.classList.remove('open-popup');
}

