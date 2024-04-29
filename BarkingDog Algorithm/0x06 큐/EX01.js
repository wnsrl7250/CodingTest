const MX = 1000005;
let dat = new Array(MX);
let head = 0;
let tail = 0;

function push(x) {
  dat[tail] = x;
  tail++;
}

function pop() {
  head++;
}

function front() {
  return dat[head];
}

function back() {
  return dat[tail - 1];
}

function test() {
  push(10);
  push(20);
  push(30);
  console.log(front()); // 10
  console.log(back()); // 30
  pop();
  pop();
  push(15);
  push(25);
  console.log(front()); // 30
  console.log(back()); // 25
}

test();
