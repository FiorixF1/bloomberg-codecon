#Problem        : Chuck
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

k = int(input())
C = ['0']
i = 1
while i <= k:
    index = i % 4
    if index == 1 or index == 3:
        C.append(str(i) + '2')
    elif index == 2:
        C.append(str(i) + '0')
    elif index == 0:
        C.append(str(i))
    i += 1
S = ''.join(C)
print(S[k])
