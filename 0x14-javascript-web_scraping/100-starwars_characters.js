#!/usr/bin/node
const req = require('request');
const uid = parseInt(process.argv[2]);
const url = `https://swapi-api.hbtn.io/api/films/${uid}`;

req.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const results = JSON.parse(body);
  const data = results.characters;
  for (const d of data) {
    req.get(d, function (erro, res, bd) {
      if (erro) {
        console.log(erro);
      }
      const d1 = JSON.parse(bd);
      console.log(d1.name);
    });
  }
});
