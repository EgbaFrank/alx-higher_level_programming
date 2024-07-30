#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.writeFile(file, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
