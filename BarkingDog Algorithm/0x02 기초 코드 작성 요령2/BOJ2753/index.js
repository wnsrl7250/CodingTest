const fs = require("fs");
const input = fs.readFileSync(__dirname + "/input.txt").toString();

let year = Number(input);
console.log(year);
if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
  console.log(1);
} else {
  console.log(0);
}
