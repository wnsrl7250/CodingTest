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

# 9개 다 더해서 100을 빼고 남음 수와 배열원소 두개를 더한 수가 같으면 나머지의 합이 100