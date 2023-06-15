// Get all table buttons
const tableButtons = document.querySelectorAll('.location-table button');
// Get the text-table input field
const textTableInput = document.querySelector('input[name="text-table"]');

  tableButtons.forEach(button => {
    button.addEventListener('click', () => {
      // Clear the current value of the text-table input
      textTableInput.value = '';
        
      // Set the value of the text-table input to the button's ID
      if (textTableInput.value != null) {
        textTableInput.value += ` The ID Of Table IS  :${button.textContent}`;
      } else {
        textTableInput.value += '';
      }
    });
  });



  const form = document.getElementById('booking-form');
  form.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent the form from submitting
    if (confirm('Are you sure you want to submit the form?')) {
      form.submit(); // Submit the form
      alert('Your request has been received'); // Show a confirmation message
    }
  });



