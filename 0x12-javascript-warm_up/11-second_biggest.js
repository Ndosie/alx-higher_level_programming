#!/usr/bin/node

const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  if (args[3] > args[2]) {
    console.log(args[3]);
  } else {
    console.log(args[2]);
  }
}
