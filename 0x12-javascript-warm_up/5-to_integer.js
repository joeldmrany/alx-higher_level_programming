#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2]);
if (!args[2] || isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
