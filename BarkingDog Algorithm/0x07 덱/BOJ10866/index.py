import sys
n = int(sys.stdin.readline())
deque = []

for _ in range(n):
    cm = sys.stdin.readline().split()
    if cm[0] == 'push_front':
        deque.insert(0, cm[1])
    elif cm[0] == 'push_back':
        deque.append(cm[1])
    elif cm[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    elif cm[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif cm[0] == 'size':
        print(len(deque))
    elif cm[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif cm[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif cm[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])