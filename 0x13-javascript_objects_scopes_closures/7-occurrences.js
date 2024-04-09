#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((number, curent) => curent === searchElement ? number + 1 : number, 0);
};
