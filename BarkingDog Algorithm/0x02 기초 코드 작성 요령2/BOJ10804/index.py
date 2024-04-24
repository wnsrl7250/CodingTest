arr = list(range(1,21))
for _ in range(10):
    N,M = map(int, input().split())
    for i in range((M-N+1)//2):
        arr[N-1+i], arr[M-1-i] = arr[M-1-i], arr[N-1+i]
    
for i in arr:
    print(i, end=" ")


# arr[N+i], arr[M-i-1] = arr[M-i-1], arr[N+i]  -> arr[N+i]와 arr[M-i-1]의 원소를 바꿔줌