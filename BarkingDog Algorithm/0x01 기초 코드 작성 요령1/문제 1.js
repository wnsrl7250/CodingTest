function solution(n) {
  var answer = 0;
  for (let i = 1; i <= n; i++) {
    if (i % 3 === 0 || i % 5 === 0) {
      answer += i;
    }
  }
  return answer;
}
