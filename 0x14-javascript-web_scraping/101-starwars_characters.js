#!/usr/bin/node
// Prints all characters of a Star Wars movie
const request = require('request');
const ID = process.argv[2];
const target = `https://swapi-api.alx-tools.com/api/films/${ID}/`;

function requestPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        return reject(error);
      }
      resolve(JSON.parse(body).name);
    });
  });
}

const characterPromises = [];

request(target, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const characters = JSON.parse(body).characters;

  // characters.map(character => requestPromise(character));
  // a more succinct method

  for (const character of characters) {
    const characterPromise = requestPromise(character);
    characterPromises.push(characterPromise);
  }

  Promise.all(characterPromises)
    .then(results => {
      results.forEach(result => {
        console.log(result);
      });
    })
    .catch(err => {
      console.error(err);
    });
});
