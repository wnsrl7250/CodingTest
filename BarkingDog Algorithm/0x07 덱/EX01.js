const MX = 1000005;
let dat = new Array(2 * MX + 1);
let head = MX;
let tail = MX;

function push_front(x) {
  dat[--head] = x;
}

function push_back(x) {
  dat[tail++] = x;
}

function pop_front() {
  head++;
}

function pop_back() {
  tail--;
}

function front() {
  return dat[head];
}

function back() {
  return dat[tail - 1];
}

function test() {
  push_back(30); // 30
  console.log(front()) << "\n"; // 30
  console.log(back()) << "\n"; // 30
  push_front(25); // 25 30
  push_back(12); // 25 30 12
  console.log(back()) << "\n"; // 12
  push_back(62); // 25 30 12 62
  pop_front(); // 30 12 62
  console.log(front()) << "\n"; // 30
  pop_front(); // 12 62
}

test();
