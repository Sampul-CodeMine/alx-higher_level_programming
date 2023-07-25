#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const uid = 18;

request(url, (err, res, body) => {
  if (!err) {
    const data = JSON.parse(body).results;
    console.log(data.reduce((total, ele) => {
      return ele.characters.find((character) => character.endsWith(`/${uid}/`)) ? total + 1 : total;
    }, 0));
  } else {
    console.log(err);
  }
});
