import sys

n = int(sys.stdin.readline())
Q =[]

for i in range(n):
    cm = sys.stdin.readline().split()
    if cm[0] == 'push':
        Q.append(cm[1])
    elif cm[0] == 'pop':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.pop(0))
    elif cm[0] == 'size':
        print(len(Q))
    elif cm[0] == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif cm[0] == 'front':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
    elif cm[0] == 'back':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[-1])