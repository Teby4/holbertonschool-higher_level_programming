const element = document.getElementById('add_item');
element.addEventListener('click', function() {
const newListElement = document.createElement('li');
  newListElement.textContent = 'Item';
  document.querySelector('.my_list').appendChild(newListElement);
});