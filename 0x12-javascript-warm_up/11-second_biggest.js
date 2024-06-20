#!/usr/bin/node

const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  const arrSlice = args.slice(2);
  console.log(arrSlice.sort(function (a, b) { return b - a; })[1]);
}
