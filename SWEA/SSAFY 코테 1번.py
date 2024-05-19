T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    newArr = []
    ans = 0
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            newArr.append([arr[i],arr[j]])

    newArr.sort()
    
    for i in range(len(newArr)):
        if i == K-1:
            ans = newArr[i][0] + newArr[i][1]

    print(f"#{tc} {ans}")