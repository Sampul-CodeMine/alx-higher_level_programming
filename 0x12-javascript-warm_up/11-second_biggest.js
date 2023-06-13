#!/usr/bin/node
function secondBiggest (arr) {
  if (arr.length <= 3) {
    return (0);
  }
  const secondBig = arr.map(Number)
    .slice(2, arr.length)
    .sort((a, b) => a - b);
  return (secondBig[secondBig.length - 2]);
}

console.log(secondBiggest(process.argv));
