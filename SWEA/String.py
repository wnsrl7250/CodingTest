for tc in range(1,11):
    n = int(input())
    search = input()
    str = input()

    result = str.count(search)
    print(f"#{tc} {result}")