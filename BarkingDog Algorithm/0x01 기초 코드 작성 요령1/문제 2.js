function solution(arr) {
  var answer = 0;
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      arr[i] + arr[j] === 100 ? (answer = 1) : (answer = 0);
    }
  }
  return answer;
}
