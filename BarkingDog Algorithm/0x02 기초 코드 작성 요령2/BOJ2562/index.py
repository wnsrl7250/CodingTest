arr = []

for i in range(9):
    N = int(input())
    arr.append(N)

print(max(arr))
print(arr.index(max(arr))+1)