#!/usr/bin/node
function fact (a) {
  if (a === 0 || a === 1) {
    return (1);
  } else {
    return (a * fact(a - 1));
  }
}
const args = process.argv;
if (!args[2]) {
  console.log('1');
} else {
  const num = fact(parseInt(args[2]));
  console.log(num);
}
