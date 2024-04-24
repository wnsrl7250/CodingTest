A = int(input())

for i in range(A):
        print("*"*(i+1)+" "*(A*2-(i+1)*2)+"*"*(i+1))
for i in range(A-1):
        print("*"*(A-1-i)+" "*((i+1)*2)+"*"*(A-1-i))