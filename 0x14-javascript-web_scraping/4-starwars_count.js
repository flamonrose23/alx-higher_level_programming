#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

let number = 0;
request(url, function (err, resp, body) {
  if (resp.statusCode === 200) {
    for (const result of JSON.parse(body).results) {
      for (const character of result.characters) {
        if (character.includes('18')) {
          number++;
        }
      }
    }
  } else {
    console.error(err);
  }
  console.log(number);
});
