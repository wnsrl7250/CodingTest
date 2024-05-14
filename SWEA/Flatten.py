for tc in range(1,11):
    N = int(input())
    K = list(map(int,input().split()))

    for i in range(N):
        maxVal = max(K)
        minVal = min(K)
        minIdx = K.index(minVal)
        maxIdx = K.index(maxVal)
        K[minIdx] += 1
        K[maxIdx] -= 1
    result = max(K) - min(K)
    print(f"#{tc} {result}")