const fs = require("fs");
const input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split(" ")
  .map((el) => parseInt(el));
const result = input.sort((a, b) => a - b).join(" ");
console.log(result);
