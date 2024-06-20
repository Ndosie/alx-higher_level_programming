#!/usr/bin/node

const args = process.argv;
let str = '';

if (isNaN(parseInt(args[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[2]; i++) {
    for (let j = 0; j < args[2]; j++) {
      str += 'X';
    }
    console.log(str);
    str = '';
  }
}
