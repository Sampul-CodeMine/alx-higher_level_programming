#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

const firstFile = fs.readFileSync(args[2]).toString();
const secondFile = fs.readFileSync(args[3]).toString();

fs.writeFileSync(args[4], firstFile + secondFile);
