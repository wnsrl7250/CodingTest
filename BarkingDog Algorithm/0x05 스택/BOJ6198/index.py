import sys

n = int(sys.stdin.readline())
bd =[]
st= []
ans =0

for _ in range(n):
    bd.append(int(sys.stdin.readline()))

for i in bd:
    while st and st[-1] <= i:
        st.pop()
    st.append(i)
    ans += len(st) -1
print(ans)

