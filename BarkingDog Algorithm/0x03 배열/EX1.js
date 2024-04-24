function insert(idx, num, arr) {
  for (i = arr.length; i > idx; i--) arr[i] = arr[i - 1];
  arr[idx] = num;
}

function erase(idx, arr) {
  for (i = idx; i < arr.length - 1; i++) {
    arr[i] = arr[i + 1];
  }
  arr.pop();
}

function printArr(arr) {
  console.log(...arr);
}

function insert_test() {
  console.log("***** insert_test *****");
  let arr = [10, 20, 30];
  insert(3, 40, arr); // 10 20 30 40
  printArr(arr);
  insert(1, 50, arr); // 10 50 20 30 40
  printArr(arr);
  insert(0, 15, arr); // 15 10 50 20 30 40
  printArr(arr);
}

function erase_test() {
  console.log("***** erase_test *****");
  let arr = [10, 50, 40, 30, 70, 20];
  erase(4, arr); // 10 50 40 30 20
  printArr(arr);
  erase(1, arr); // 10 40 30 20
  printArr(arr);
  erase(3, arr); // 10 40 30
  printArr(arr);
}

insert_test();
erase_test();
