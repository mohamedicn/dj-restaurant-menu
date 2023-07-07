var address = document.getElementById("address").value ;
var phone = document.getElementById("phone").value; 
var notes = document.getElementById("not_if_any").value; 


function showForm(formNumber){ //
  // Hide all payment forms
  var forms = document.getElementsByClassName("payment-form");
  for (var i = 0; i < forms.length; i++) {
    forms[i].style.display = "none";
  }  
// Show the selected payment form
  var selectedForm = document.getElementById("form" + formNumber);
  selectedForm.style.display = "block";

}


