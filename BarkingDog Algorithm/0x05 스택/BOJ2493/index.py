import sys

n = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
st = []
ans = [0] * n

for i in range(n):
    while st:
        if st[-1][1] > top[i]:
            ans[i] = st[-1][0] +1
            break
        else:
            st.pop()
    st.append([i, top[i]])
print(*ans)