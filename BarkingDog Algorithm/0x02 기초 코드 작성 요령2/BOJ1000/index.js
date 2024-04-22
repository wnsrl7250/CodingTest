const fs = require("fs");
let input = fs.readFileSync(__dirname + "/input.txt").toString();
let inputs = input.split(" ");
let A = Number(inputs[0]);
let B = Number(inputs[1]);

console.log(A + B);
