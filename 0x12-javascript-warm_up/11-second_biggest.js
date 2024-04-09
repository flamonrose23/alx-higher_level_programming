#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const lst = process.argv.sort();
  console.log(lst.reverse()[1]);
}
