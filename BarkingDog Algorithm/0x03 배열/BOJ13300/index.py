N , k = map(int, input().split()) 

arr = [[0,0,0,0,0,0],[0,0,0,0,0,0]]
count = 0
for i in range(N):
    s, g = map(int, input().split())
    arr[s][g-1] += 1

for i in arr:
    for j in i:
        if j % k ==0:
            count += j//k
        else:
            count += j//k + 1
print(count)