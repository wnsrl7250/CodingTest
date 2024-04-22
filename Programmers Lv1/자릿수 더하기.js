function solution(n) {
  var answer = 0;
  let arr = String(n).split("");
  for (let i = 0; i < arr.length; i++) {
    answer += Number(arr[i]);
  }

  return answer;
}

// 다른 사람 풀이
// return (n+"").split("").reduce((acc, curr) => acc + parseInt(curr), 0)
// (n+"")으로 문자열로 변환
// for문 대신 reduce메서드로 계산
