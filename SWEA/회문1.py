for tc in range(1,11):
    n = int(input())
    arr = [list(input()) for _ in range(8)]

    result = 0

    for i in range(8):
        for j in range(8-n+1):
            A = arr[i][j:j+n]
            if A == A[::-1]:
                result += 1
    
    for i in range(8):
        for j in range(8-n+1):
            char = ''
            for k in range(j,j+n):
                char += arr[k][i]
            if char == char[::-1]:
                result += 1
    print(f"#{tc} {result}")