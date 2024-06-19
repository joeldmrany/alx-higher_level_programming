#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2]);
if (!args[2]) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
