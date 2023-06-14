#!/usr/bin/node

class Rectangle {
  /* A rectangle class */
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    /* prints a square */
    for (let i = 1; i <= this.height; i++) {
      let chrs = '';
      for (let j = 1; j <= this.width; j++) {
        chrs += 'X';
      }
      console.log(chrs);
    }
  }

  rotate () {
    /* rotates the rectangle */
    const tempValue = this.width;
    this.width = this.height;
    this.height = tempValue;
  }

  double () {
    /* multiplies the width and height by 2 */
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
