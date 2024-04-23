T = int(input())

for t in range(1,T+1):
    A,B,C = map(int,input().split())
    answer = 0

    if B < 2 or C <  3:
        answer = -1
    
    else:
        if B >= C:
            answer += B-C+1
            B -= answer
        if A >= B:
            answer += A-B+1
    
    print(f'#{t} {answer}')