function solution(n) {
  var answer = 1;
  while (2 * answer <= n) {
    answer *= 2;
  }
  return answer;
}
