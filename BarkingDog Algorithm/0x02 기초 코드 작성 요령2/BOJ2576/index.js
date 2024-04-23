const fs = require("fs");
const input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n")
  .map((v) => +v)
  .sort((a, b) => a - b);
let odd = [];
for (const i of input) {
  if (i % 2 !== 0) {
    odd.push(i);
  }
}

if (odd.length === 0) {
  console.log(-1);
} else {
  let sum = odd.reduce((pre, cur) => pre + cur);
  let min = odd[0];
  console.log(sum);
  console.log(min);
}
