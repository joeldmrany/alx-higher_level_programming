#!/usr/bin/node
const args = process.argv;
const x = parseInt(args[2]);
for (let i = 0; i < x; i++) {
  for (let j = 0; j < x; j++) {
    if (x < 0) {
      break;
    }
    process.stdout.write('X');
  }
  process.stdout.write('\n');
}
