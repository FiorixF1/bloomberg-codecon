#Problem        : A Very Odd Problem
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

def OK(array):
    num_even = len(list(filter(lambda x: x % 2 == 0, array)))
    somma = sum(array)
    if num_even != 0 and num_even % 2 == 0 and somma % 2 == 0:
        return True
        
    for num in array:
        somma2 = somma - num
        even2 = num_even
        if num % 2 == 0:
            even2 -= 1
        if even2 != 0 and even2 % 2 == 0 and somma2 % 2 == 0:
            return True
            
    return False
    
N = int(input())
array = [int(i) for i in input().split()]

if OK(array):
    print("YES")
else:
    print("NO")