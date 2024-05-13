const element = document.getElementById('toggle_header');
element.addEventListener('click', function() {
  const header = document.getElementById('header');
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});