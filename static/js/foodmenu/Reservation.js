const addresses = document.querySelectorAll('#addresses address');
const addressFrom = document.getElementById('address-from');

addresses.forEach((address) => {
  address.addEventListener('click', () => {
    addressFrom.value = address.innerText;
  });
});



// function checkAndSaveFormData() {
//   // Get form values
//   var address = document.getElementById("address-from").value;
//   var phone = document.getElementById("phone").value;
//   var notes = document.getElementById("text").value;

//   // Check if any of the required fields are empty
//   if ( address !== "" && phone !== "") {
//     // Create an object to store form data
//     var formData = {
//       address: address,
//       phone: phone,
//       notes: notes
//     };

//     // Check if there are more than 6 objects in local storage
//     if (localStorage.length > 6) {
//       // Clear the entire local storage
//       localStorage.clear();
//     }
//     for (let index = 1; index <= 3; index++) {
//       localStorage.setItem("formData"+index, JSON.stringify(formData));
//     }
//     // Store form data in local storage
//   }
// }
















// // // ₺
