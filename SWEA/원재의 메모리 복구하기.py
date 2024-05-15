T=int(input())

for tc in range(1,T+1):
    n = list(input())
    arr = list(0 for _ in range(len(n)))
    result=0

    for i in range(len(arr)):
        if int(n[i]) != arr[i]:
            for j in range(i,len(arr)):
                arr[j] = int(n[i])
            result += 1
        else:
            continue
    
    print(f"#{tc} {result}")
