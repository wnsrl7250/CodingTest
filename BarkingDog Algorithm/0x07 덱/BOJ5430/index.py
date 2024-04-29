from collections import deque
import sys
input = sys.stdin.readline
t= int(input())

for _ in range(t):
    cm = list(input())
    n = int(input())
    dq = deque(input().rstrip()[1:-1].split(','))
    flag = 1

    if n == 0:
        dq = deque()

    r = 0
    for i in cm:
        if i =='R':
            r += 1
        elif i == 'D':
            if len(dq) == 0:
                print('error')
                flag = 0
                break
            else:
                if r % 2 ==0:
                    dq.popleft()
                else:
                    dq.pop()
    if flag == 1:
        if r % 2 == 0:
            print("[" + ",".join(dq) + "]")
        else:
            dq.reverse()
            print("[" + ",".join(dq) + "]")

        

