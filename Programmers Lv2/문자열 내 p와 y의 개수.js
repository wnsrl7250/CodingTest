function solution(s) {
  var answer = true;
  let arr = s.toUpperCase().split("");
  let p = 0;
  let y = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "P") {
      p++;
    } else if (arr[i] === "Y") {
      y++;
    }
  }
  p === y ? (answer = true) : (answer = false);

  return answer;
}
