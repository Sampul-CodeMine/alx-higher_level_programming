#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];
const content = process.argv[3];
const modes = { encoding: 'utf-8', flag: 'w' };
try {
  fs.writeFile(filepath, content, modes, (err, res) => {
    if (err) console.log(err);
  });
} catch (err) {
  console.log(err);
}
