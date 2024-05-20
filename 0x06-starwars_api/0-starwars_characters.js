const url = 'https://swapi-api.alx-tools.com/api/';

async function getCharactersOfFilm (movieId) {
  const response = await fetch(`${url}films/${movieId}`);
  const data = await response.json();
  return data.characters;
}

async function getStarWarsCharacters () {
  const movieId = process.argv[2];
  const charactersArray = await getCharactersOfFilm(movieId);
  for (const charactersUrl of charactersArray) {
    const response = await fetch(charactersUrl);
    const data = await response.json();
    console.log(data.name);
  }
}

getStarWarsCharacters();
