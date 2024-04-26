N,K = map(int,input().split())
pre = {}
nxt = {}

v = []
for i in range(1,N+1): 
    if i == 1:
        pre[i] = N
    else:
        pre[i] = i-1
    if i == N:
        nxt[i] = 1
    else: nxt[i] = i+1

cur = 1
length = N

while length != 0:
    for _ in range(K-1):
        cur = nxt[cur]
    v.append(cur)
    nxt[pre[cur]] = nxt[cur]
    pre[nxt[cur]] = pre[cur]
    cur = nxt[cur]
    length -= 1

print("<", end="")
for i in range(len(v)):
    if i == len(v) - 1:
        print(v[i], end="")
    else:
        print(f"{v[i]}, ", end="")
print(">")