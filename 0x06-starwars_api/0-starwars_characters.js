#!/usr/bin/node
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/';

async function getCharactersOfMovie (movieId) {
  const response = await fetch(`${url}films/${movieId}`);
  const data = await response.json();
  return data.characters;
}

async function DisplayStarWarsCharactersOfMovie (movieId) {
  const charactersArray = await getCharactersOfMovie(movieId);
  for (const characterUrl of charactersArray) {
    const response = await fetch(characterUrl);
    const data = await response.json();
    console.log(data.name);
  }
}

DisplayStarWarsCharactersOfMovie(movieId);
