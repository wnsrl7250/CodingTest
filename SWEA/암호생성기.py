for tc in range(1,11):
    N = int(input())
    arr = list(map(int, input().split()))

    cycle = True
    while cycle:
        for i in range(1,6):
            if arr[0]-i >0:
                arr.append(arr[0]-i)
                arr.pop(0)
            else:
                arr.append(0)
                arr.pop(0)
                cycle =False
                break
    
    print(f"#{N}",*arr)