fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    const characterName = data.name;
    document.getElementById('character').textContent = characterName;
  })
  .catch(error => {
    console.error('Error fetching character name:', error);
});
