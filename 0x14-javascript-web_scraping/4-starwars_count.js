#!/usr/bin/node
// Prints the number of movies with the character “Wedge Antilles”
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;

  let count = 0;
  for (const film of films) {
    if (film.characters.includes(characterUrl)) {
      count++;
    }
  }
  console.log(count);
});
