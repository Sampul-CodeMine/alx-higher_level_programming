#!/usr/bin/node
const request = require('request');
const uid = parseInt(process.argv[2]);
const url = `https://swapi-api.alx-tools.com/api/films/${uid}`;
request(url, (err, resp, body) => {
  console.log(err || JSON.parse(body).title);
});
