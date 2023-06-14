#!/usr/bin/node

const SquareP = require('./5-square');

class Square extends SquareP {
  /* Square class extending from SquareP class as Parent class
   * which in turn extends from the Rectangle class */
  charPrint (c) {
    if (c === undefined) c = 'X';
    for (let i = 1; i <= this.height; i++) {
      let chrs = '';
      for (let j = 1; j <= this.width; j++) {
        chrs += c;
      }
      console.log(chrs);
    }
  }
}

module.exports = Square;
