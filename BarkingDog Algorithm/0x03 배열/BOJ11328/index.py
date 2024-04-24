N = int(input())


for _ in range(N):
    a, b = map(str,input().split())
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    if len(a) != len(b):
        print("Impossible")
        continue
    for i in range(len(a)):
        if a[i] != b[i]:
            answer = "false"
            break
        else:
            answer = "true"
    if answer == "false":
        print("Impossible")
    else:
        print("Possible")
