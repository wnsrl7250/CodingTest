from sys import stdin

for _ in range(int(input())):
    text = list(stdin.readline())
    left = []
    right = []
    for i in text:
        if i == "<" :
            if left:
                right.append(left.pop())
        elif i == ">":
            if right:
                left.append(right.pop())
        elif i == "-":
            if left:
                left.pop()
        else :
            left.append(i)
    answer = left+right[::-1]
    print("".join(answer))   
