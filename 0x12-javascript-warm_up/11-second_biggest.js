#!/usr/bin/node

const args = process.argv.slice(2);

const numList = args.map(a => +a);

if (numList.length < 2) {
  console.log('0');
} else {
  let i = 1;
  let lrgst = numList[0];
  let sLrgst = null;

  while (i < numList.length) {
    if (numList[i] > lrgst) {
      sLrgst = lrgst;
      lrgst = numList[i];
    } else if (numList[i] > sLrgst && numList[i] !== lrgst) {
      sLrgst = numList[i];
    }
    ++i;
  }
  console.log(`${sLrgst}`);
}
