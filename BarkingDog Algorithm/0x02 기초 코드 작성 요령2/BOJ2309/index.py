arr = []
for i in range(9):
    arr.append(int(input()))
arr.sort()

sumM = sum(arr) - 100
a=0
b= 0
for i in range(8):
    for j in range(i+1,9):
        if(arr[i] + arr[j] == sumM):
            a = i
            b = j
for i in range(9):
    if(i == a or i== b):
        continue
    print(arr[i])