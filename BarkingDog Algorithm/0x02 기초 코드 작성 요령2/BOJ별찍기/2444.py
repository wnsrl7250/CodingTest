A = int(input())

for i in range(A):
        print(" "*(A-i-1)+"*"*(2*i+1))
for i in range(A-1):
        print(" "*(i+1)+"*"*(((A-1)*2-1)-2*i))