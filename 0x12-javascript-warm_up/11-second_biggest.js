#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const second = process.argv.sort();
  console.log(second.reverse()[1]);
}
