let MX = 1000005;
let dat = Array(MX).fill(0);
let pre = Array(MX).fill(-1);
let nxt = Array(MX).fill(-1);
let unused = 1;

function insert(addr, num) {
  dat[unused] = num;
  pre[unused] = addr;
  nxt[unused] = nxt[addr];
  if (nxt[addr] != -1) pre[nxt[addr]] = unused;
  nxt[addr] = unused;
  unused++;
}

function erase(addr) {
  nxt[pre[addr]] = nxt[addr];
  if (nxt[addr] != -1) pre[nxt[addr]] = pre[addr];
}

function traverse() {
  let cur = nxt[0];
  let result = "";
  while (cur != -1) {
    result += dat[cur] + " ";
    cur = nxt[cur];
  }
  console.log(result + "\n");
}
function insert_test() {
  console.log("****** insert_test *****");
  insert(0, 10); // 10(address=1)
  traverse();
  insert(0, 30); // 30(address=2) 10
  traverse();
  insert(2, 40); // 30 40(address=3) 10
  traverse();
  insert(1, 20); // 30 40 10 20(address=4)
  traverse();
  insert(4, 70); // 30 40 10 20 70(address=5)
  traverse();
}

function erase_test() {
  console.log("****** erase_test *****");
  erase(1); // 30 40 20 70
  traverse();
  erase(2); // 40 20 70
  traverse();
  erase(4); // 40 70
  traverse();
  erase(5); // 40
  traverse();
}

insert_test();
erase_test();
