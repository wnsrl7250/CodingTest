num = input()

ans= [0]* 10

for i in num:
    if i == '6' or i == '9':
        if ans[6] <= ans[9]:
            ans[6] += 1
        else:
            ans[9] += 1
    else:
        ans[int(i)] += 1

print(max(ans))
