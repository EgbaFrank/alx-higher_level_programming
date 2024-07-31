#!/usr/bin/node
// Prints the number of movies with the character “Wedge Antilles”
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  try {
    const films = JSON.parse(body).results;

    let count = 0;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.endsWith('/18/')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  } catch (err) {
    console.error(err);
  }
});
