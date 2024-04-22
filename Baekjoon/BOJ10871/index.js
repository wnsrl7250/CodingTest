const fs = require("fs");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");
let inputs = [];
inputs = input[0].split(" ");
console.log(inputs[2]);

let total = Number(inputs[0]);
let limit = Number(inputs[1]);

let numbers = [];
numbers = input[1].split(" ");

result = "";
for (let i = 0; i < total; i++) {
  if (Number(numbers[i]) < limit) {
    result += numbers[i] + " ";
  }
}

console.log(result);
