#!/usr/bin/node

const args = process.argv.slice(2);
const size = +args[0];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < size; ++x) {
    console.log('X'.repeat(size));
  }
}
