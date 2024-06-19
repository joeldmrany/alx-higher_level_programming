#!/usr/bin/node
const args = process.argv;
function add (a, b) {
  return (a + b);
}
const sum = add(parseInt(args[2]), parseInt(args[3]));
console.log(sum);
