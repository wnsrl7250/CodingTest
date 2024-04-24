t = int(input())
a = list(map(int, input().split()))
y = m = 0
for i in a:
    y+=(i//30+1)*10
    m+=(i//60+1)*15
if m == y:
    print("Y M",m)
elif m < y:
    print("M",m)
else:
    print("Y",y) 
