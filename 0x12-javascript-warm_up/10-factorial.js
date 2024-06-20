#!/usr/bin/node

function factorial (n) {
  if (n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
const args = process.argv;

if (isNaN(parseInt(args[2]))) {
  console.log(1);
} else {
  console.log(factorial(parseInt(args[2])));
}
