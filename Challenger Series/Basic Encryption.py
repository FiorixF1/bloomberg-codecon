#Problem        : Basic Encryption
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

N = int(input())
E = []
for i in range(N):
    E.append(int(input()))

A = [E[0]]
for i in range(N-1):
    item = E[i] - E[i+1]
    A.append(A[-1] + item)
    
first = sum(A) - A[0]
if N == 1 and A[0] != 0:
    print('NO SOLUTION')
elif first == 0:
    print('MULTIPLE SOLUTIONS')
else:
    diff = int((first - A[0])/(N-1))
    EXIST = True
    for i in range(N):
        A[i] -= diff
        if A[i] < 0 or A[i] > 255:
            EXIST = False
    if EXIST:
        for elem in A:
            print(elem)
    else:
        print('NO SOLUTION')
