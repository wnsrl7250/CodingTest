A = int(input())

for i in range(A):
        print(" "*i+"*"*(A*2-(2*i)-1))
for i in range(A-1):
        print(" "*(A-2-i)+"*"*(2*(i+1)+1))