#!/usr/bin/node
// Prints the title of a Star Wars movie
const request = require('request');
const ID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${ID}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body).title;
  console.log(data);
});
