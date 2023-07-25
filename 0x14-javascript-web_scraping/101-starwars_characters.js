#!/usr/bin/node
const request = require('request');
const uid = parseInt(process.argv[2]);
const url = `https://swapi-api.hbtn.io/api/films/${uid}`;

const display = (charas, num) => {
  request(charas[num], (err, res, body) => {
    if (!err) {
      console.log(JSON.parse(res.body).name);
      if ((num + 1) < charas.length) display(charas, (num + 1));
    }
  });
};
request(url, async (err, resp, body) => {
  if (err === null) display(JSON.parse(body).characters, 0);
});
