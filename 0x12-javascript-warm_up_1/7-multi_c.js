#!/usr/bin/node
const args = process.argv;
const x = parseInt(args[2]);
for (let i = 0; i < x; i++) {
  if (x < 0) {
    break;
  }
  console.log('C is fun');
}
