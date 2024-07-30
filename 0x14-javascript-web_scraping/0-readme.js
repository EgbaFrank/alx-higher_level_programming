#!/usr/bin/node
// Reads and prints the content of a file

const fs = require('fs');
const file = process.argv[2]; // file to be read

fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
