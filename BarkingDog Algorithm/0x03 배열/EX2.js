function solution(arr) {
  let occur = [];
  for (let i = 0; i < arr.length; i++) {
    if (occur[100 - arr[i]] === 1) return 1;
    occur[arr[i]] = 1;
  }
  return 0;
}

arr = [30, 24, 86, 73, 88];

console.log(solution(arr));
