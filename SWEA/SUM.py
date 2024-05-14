for tc in range(1,11):
    tc_num = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    row_total_list = []
    for i in range(100):
        r_total = 0
        for j in range(100):
            r_total += arr[i][j]
        row_total_list.append(r_total)
    
    col_total_list=[]
    for i in range(100):
        c_total = 0
        for j in range(100):
            c_total += arr[j][i]
        col_total_list.append(c_total)

    l_diag_total=0
    for i in range(100):
        l_diag_total += arr[i][i]

    r_diag_total=0
    for i in range(100):
        r_diag_total += arr[99-i][i]

    find_max = [max(row_total_list), max(col_total_list), l_diag_total, r_diag_total]
    result = max(find_max)

    print(f"#{tc} {result}")