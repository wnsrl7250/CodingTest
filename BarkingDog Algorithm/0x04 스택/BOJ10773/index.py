import sys
n = int(sys.stdin.readline())
st = []

for _ in range(n):
    k = int(sys.stdin.readline())
    if k == 0:
        st.pop()
    else:
        st.append(k)

print(sum(st))