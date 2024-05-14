T=int(input())

for tc in range(1,T+1):
    N=int(input())
    height = list(map(int, input().split()))
    result=0
    for i in range(2, N-2):
        hmax = max(height[i-2],height[i-1],height[i+1],height[i+2])
        if height[i]>hmax:
            result += (height[i] - hmax)
    print(f"#{tc} {result}")

