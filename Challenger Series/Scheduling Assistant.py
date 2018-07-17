#Problem        : Scheduling Assistant
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

D = int(input())
N = int(input())
intervals = [0]*96
for i in range(N):
    employee = input() # a nessuno importa
    B = int(input())
    for j in range(B):
        interval = input().split()
        start = int(interval[0])
        end = int(interval[1])
        for k in range(start, end):
            intervals[k] = 1
i = 0
while True:
    while i < 96 and intervals[i] == 1:
        i += 1
    length = 0
    result = i
    while i < 96 and intervals[i] == 0:
        length += 1
        i += 1
    if length >= D:
        print(result)
        break
    if i == 96:
        print(-1)
        break

    
