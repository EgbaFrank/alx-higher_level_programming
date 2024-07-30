#!/usr/bin/node
// Computes the number of tasks completed by user id
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = {};
  for (const user of JSON.parse(body)) {
    if (user.completed === true) {
      if (user.userId in data) {
        data[user.userId]++;
      } else {
        data[user.userId] = 1;
      }
    }
  }
  console.log(data);
});
