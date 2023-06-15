const addresses = document.querySelectorAll('#addresses address');
const result = document.getElementById('result');
const addressFrom = document.getElementById('address-from');


addresses.forEach((address, index) => {
  address.addEventListener('click', () => {
    const distance = (index + 1) * 1; // assume each address is 1 km apart
    const time = distance * 6 + 30; // 6 minutes per km + 30 minutes preparation
    const cost = distance * 0.75;
    result.innerText = `Meal will be delivered in ${time} minutes \nand cost $${cost.toFixed(2)}`;
    result.style.backgroundColor = '#FFF';
    result.style.textAlign = 'center';
    // setTimeout(() => {
    //   result.style.display = 'none';
    // }, 5000); // Hide the result after 5 seconds
  });
});


addresses.forEach((address) => {
  address.addEventListener('click', () => {
    addressFrom.value = address.innerText;
  });
});






















// ₺
