function solution(n) {
  var answer = 0;
  for (let i = 1; i * i <= n; i++) {
    if (i * i === n) {
      answer = 1;
    }
  }
  return answer;
}
