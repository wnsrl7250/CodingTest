const MX = 1000005;
let dat = new Array(MX);
let pos = 0;

function push(x) {
  dat[pos] = x;
  pos++;
}

function pop() {
  if (pos > 0) pos--;
}

function top() {
  if (pos > 0) {
    return dat[pos - 1];
  }
  return undefined;
}

function test() {
  push(5);
  push(4);
  push(3);
  console.log(top()); // 3
  pop();
  pop();
  console.log(top()); // 5
  push(10);
  push(12);
  console.log(top()); // 12
  pop();
  console.log(top()); // 10
}

test();
