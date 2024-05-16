for tc in range(1,11):
    n= int(input())
    data = list(map(int,input().split()))
    k = int(input())
    order = list(input().split())

    for i in range(len(order)):
        if order[i] == 'I':
            idx = int(order[i+1])
            nums = int(order[i+2])
            for j in range(nums):
                data.insert(idx+j, int(order[i+2+(j+1)]))
        else:
            continue

    print(f'#{tc}',' '.join(map(str,data[:10])))
