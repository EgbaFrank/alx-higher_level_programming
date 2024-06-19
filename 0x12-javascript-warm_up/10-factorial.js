#!/usr/bin/node

function factorial (x) {
  if (x === 1 || x === 0 || x < 0 || isNaN(x)) { return (1); }

  return (x * factorial(x - 1));
}

const args = process.argv.slice(2);
const num = +args[0];

console.log(`${factorial(num)}`);
