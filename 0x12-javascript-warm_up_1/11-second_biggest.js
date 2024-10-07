#!/usr/bin/node
const args = process.argv;
if (args.length < 4) {
  console.log('0');
} else {
  let big = parseInt(args[2]);
  for (let i = 2; i < args.length; i++) {
    if (big > parseInt(args[i])) {
      continue;
    } else {
      big = parseInt(args[i]);
    }
  }
  let big2 = -Infinity;
  for (let i = 2; i < args.length; i++) {
    if (parseInt(args[i]) === big) {
      continue;
    } else if (big2 >= parseInt(args[i])) {
      continue;
    } else {
      big2 = parseInt(args[i]);
    }
  }
  console.log(big2);
}
