#!/usr/bin/node
const number = process.argv[2];

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    let addon = '';
    for (let j = 0; j < number; j++) {
      addon += 'X';
    }
    console.log(addon);
  }
}
