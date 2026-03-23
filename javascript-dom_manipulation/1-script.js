// When the user clicks on the element with id "red_header",
// update the text color of the <header> element to red
document.querySelector('#red_header').addEventListener('click', function () {
  document.querySelector('header').style.color = '#FF0000';
});
