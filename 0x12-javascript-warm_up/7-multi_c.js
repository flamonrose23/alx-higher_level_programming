#!/usr/bin/node
const phrase = 'C is fun';
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let a = 0; a < parseInt(process.argv[2]); a++) {
    console.log(phrase);
  }
}
