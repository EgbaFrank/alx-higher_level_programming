#!/usr/bin/node

module.exports = class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; ++i) {
      console.log('X'.repeat(this.width));
    }
  }
};
