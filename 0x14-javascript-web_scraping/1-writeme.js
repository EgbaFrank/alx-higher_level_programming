#!/usr/bin/node
// Writes a string to a file
const fs = require('fs');
const file = process.argv[2]; // file to be written to
const data = process.argv[3]; // data to be written

fs.writeFile(file, data, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
