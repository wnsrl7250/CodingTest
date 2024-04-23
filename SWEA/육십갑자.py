T=int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    s = list(input().split())
    t = list(input().split())
    q = int(input())
    result = []
    for _ in range(q):
        y = int(input())
        result.append(s[y % N - 1] + t[y % M -1])
        answer = ' '.join(result)
        print(f"#{tc} {answer}")
    