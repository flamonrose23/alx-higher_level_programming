#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (array, curent) {
    array.push(curent);
    return array;
  }, []);
};
