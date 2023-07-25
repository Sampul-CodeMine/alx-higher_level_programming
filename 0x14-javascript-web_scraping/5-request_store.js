#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filename = process.argv[3];

request
  .get(url)
  .on('err', err => console.log(err))
  .pipe(fs.createWriteStream(filename));
