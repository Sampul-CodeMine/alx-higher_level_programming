#!/usr/bin/node

const list = require('./100-data.js').list;
const listTwo = list.map((n, index)=> n * index);

console.log(list);
console.log(listTwo);
