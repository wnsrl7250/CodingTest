def palindrome(M, arr):
    for i in range(100):
        for j in range(0, 100-M+1):
            if arr[i][j] == arr[i][j+M-1]:
                for k in range(1, M//2):
                    if arr[i][j+k] != arr[i][j+M-1-k]:
                        break
                else:
                    return True

        for j in range(0, 100-M+1):
            if arr[j][i] == arr[j+M-1][i]:
                for k in range(1, M//2):
                    if arr[j+k][i] != arr[j+M-1-k][i]:
                        break
                else:
                    return True
    return False

for tc in range(1,11):
    n = int(input())
    arr = [list(input()) for _ in range(100)]

    for M in range(100, -1, -1):
        if palindrome(M, arr):
            print(f"#{tc} {M}")
            break

    