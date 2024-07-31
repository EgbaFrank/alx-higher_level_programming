#!/usr/bin/node
// Prints all characters of a Star Wars movie
const request = require('request');
const ID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${ID}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    request(character, (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }
      const result = JSON.parse(body).name;
      console.log(result);
    });
  }
});
