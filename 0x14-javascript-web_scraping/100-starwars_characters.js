#!/usr/bin/node
const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);
request(starWarsUri, function (_err, _res, body) {
  const characters = JSON.parse(body).characters;

  for (let x = 0; x < characters.length; ++x) {
    request(characters[x], function (_cErr, _cRes, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});
