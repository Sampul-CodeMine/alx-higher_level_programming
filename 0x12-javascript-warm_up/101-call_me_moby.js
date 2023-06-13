#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let itr = 0; itr < x; itr++) theFunction();
};
