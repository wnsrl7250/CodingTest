const fs = require("fs");
const input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split(" ")
  .map((v) => parseInt(v))
  .sort((a, b) => a - b);
let a = input[0];
let b = input[1];
let c = input[2];
let price = 0;
if (a === b && a === c) {
  price = 10000 + a * 1000;
} else if (a === b || b === c) {
  price = 1000 + b * 100;
} else {
  price = c * 100;
}
console.log(price);
