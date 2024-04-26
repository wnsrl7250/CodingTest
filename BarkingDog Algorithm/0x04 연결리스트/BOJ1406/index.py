from sys import stdin


left = list(input())
right = []

for _ in range(int(input())):
    cm = list(stdin.readline().split())
    if cm[0] == "P":
        left.append(cm[1])
    elif cm[0] == "L" and left:
        right.append(left.pop())
    elif cm[0] =="D" and right:
        left.append(right.pop())
    elif cm[0] == "B" and left:
        left.pop()
    
answer = left + right[::-1]
print(''.join(answer))
