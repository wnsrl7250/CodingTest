import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
st = []
ans = [-1]*n

for i in range(n):
    while st and arr[st[-1]] < arr[i]:
        ans[st[-1]] = arr[i]
        st.pop()
    st.append(i)

print(*ans)
        