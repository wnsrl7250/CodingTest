T = int(input())

for tc in range(1,T+1):
    N = int(input())
    K = [list(map(int, input())) for _ in range(N)]
    answer = 0
    mid = (N-1)//2
    for i in range(N):
        if i<=mid:
            answer += sum(K[i][mid-i:mid+1+i])
        else:
            answer += sum(K[i][i-mid:mid+1+(N-1-i)])
    
    print(f'#{tc} {answer}')
