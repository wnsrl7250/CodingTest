let fs = require("fs");
input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");
n = +input[0];
arr = input[1].split(" ").map(Number);
x = +input[2];

let occur = [];
let count = 0;
for (let i = 0; i < n; i++) {
  if (occur[x - arr[i]] === 1) {
    count++;
  }
  occur[arr[i]] = 1;
}
console.log(count);
