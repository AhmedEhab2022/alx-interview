#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/';

async function getCharactersOfMovie (movieId) {
  return await new Promise((resolve, reject) => {
    request(`${url}films/${movieId}`, (error, response, body) => {
      if (error) {
        reject(error);
      }
      resolve(JSON.parse(body).characters);
    });
  });
}

async function DisplayStarWarsCharactersOfMovie (movieId) {
  const charactersArray = await getCharactersOfMovie(movieId);
  for (const characterUrl of charactersArray) {
    await new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        }
        console.log(JSON.parse(body).name);
        resolve(JSON.parse(body).name);
      });
    });
  }
}

DisplayStarWarsCharactersOfMovie(movieId);
