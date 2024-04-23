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

//다른사람풀이
// yut을 선언할때 map메서드 뒤에 reduce메서드로 배열원소의 합 구함 .reduce((pre, cur) => pre + cur);
// 합을 구하면 굳이 yut배열을 for문으로 돌 필요 없이 if문으로 답을 구한다
