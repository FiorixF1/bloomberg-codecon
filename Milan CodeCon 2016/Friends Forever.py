#Problem        : Friends Forever
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

N = int(input())

words = []
for n in range(N):
    words.append(input().upper())
    
def complementary(a, b):
    for letter1 in a:
        for letter2 in b:
            if letter1 == letter2:
                return False
    return True
    
ans = 0
for i in range(N):
    for j in range(i, N):
        if i != j and complementary(words[i], words[j]):
            ans += 1
            
print(ans)
