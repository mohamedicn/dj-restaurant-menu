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
    
    
 

let popup = document.getElementById('popup');
function OpenPopup() {
    popup.classList.add('open-popup');
}
function ClosePopup() {
    popup.classList.remove('open-popup');
}

  // Get the button elements
  var addButton = document.getElementById("addButton");
  var decreaseButton = document.getElementById("decreaseButton");

  // Add click event listeners to the buttons
  addButton.addEventListener("click", handleAdd);
  decreaseButton.addEventListener("click", handleDecrease);

  function handleAdd(event) {
    event.preventDefault();
   }
   function handleDecrease(event) {
    event.preventDefault();
   }
    

