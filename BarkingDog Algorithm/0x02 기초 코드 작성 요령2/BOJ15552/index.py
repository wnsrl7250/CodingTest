T = int(input())
arr = []

for t in range(T):
    N,M = map(int, input().split())
    arr.append(N+M)

for i in arr:
    print(i)