const fs = require("fs");
const input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .trim()
  .split("\n");

for (let i = 0; i < input.length; i++) {
  let yut = input[i].split(" ").map((v) => +v);
  let count = 0;
  for (let j = 0; j < yut.length; j++) {
    if (Number(yut[j]) === 1) count++;
  }
  if (count === 4) {
    console.log("E");
  } else if (count === 3) {
    console.log("A");
  } else if (count === 2) {
    console.log("B");
  } else if (count === 1) {
    console.log("C");
  } else {
    console.log("D");
  }
}
