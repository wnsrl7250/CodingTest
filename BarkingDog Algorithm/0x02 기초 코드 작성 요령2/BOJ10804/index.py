arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for _ in range(10):
    N,M = map(int, input().split())
    for i in range((M-N+1)//2):
        arr[N+i], arr[M-i-1] = arr[M-i-1], arr[N+i]
    
for i in arr:
    print(i, end=" ")


# arr[N+i], arr[M-i-1] = arr[M-i-1], arr[N+i]  -> arr[N+i]와 arr[M-i-1]의 원소를 바꿔줌