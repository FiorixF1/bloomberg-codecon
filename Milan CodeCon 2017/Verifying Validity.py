#Problem        : Verifying Validity
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

def check(isbn):
    first = 1
    checksum = 0
    for ch in isbn:
        num = int(ch)
        checksum += num*first
        if first == 1:
            first = 3
        else:
            first = 1
    if checksum % 10 == 0:
        print("VALID")
    else:
        print("NOT VALID")
    
N = int(input())
ISBN = []

for n in range(N):
    ISBN.append(input())  # una stringa!
    
for isbn in ISBN:
    check(isbn)

