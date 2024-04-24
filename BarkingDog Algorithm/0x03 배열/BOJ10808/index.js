let fs = require("fs");
input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("");
let str = "abcdefghijklmnopqrstuvwxyz";
let alpha = Array(26).fill(0);

for (let i = 0; i < input.length; i++) {
  alpha[str.indexOf(input[i])]++;
}
console.log(alpha.join(" "));
