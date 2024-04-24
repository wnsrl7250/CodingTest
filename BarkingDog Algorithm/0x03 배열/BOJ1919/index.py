a = list(input())
b = list(input())

li = [[0]*26 for _ in range(2)]
result = 0
for i in a:
    li[0][ord(i)-ord('a')] += 1
for i in b:
    li[1][ord(i)-ord('a')] += 1
for i in range(26):
    result += abs(li[0][i] - li[1][i])
print(result)