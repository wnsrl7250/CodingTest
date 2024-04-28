import sys
n = int(sys.stdin.readline())
st = []
answer = []
find = True
cur = 1

for _ in range(n):
    k = int(sys.stdin.readline())
    while cur <= k :
        st.append(cur)
        answer.append("+")
        cur += 1
    if st[-1] == k:
        st.pop()
        answer.append("-")
    else:
        find= False
    
if find == False:
    print('NO')
else:
    for i in answer:
        print(i)