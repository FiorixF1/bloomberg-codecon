#Problem        : Finals Spring 2015 - Matching Gloves
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

def is_palindrome(s):
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
    
N = int(input())
ans = 0
dic = dict()
for n in range(N):
    s = input()
    if not is_palindrome(s):
        if s[::-1] not in dic:
            try:
                dic[s] += 1
            except:
                dic[s] = 1
        else:
            dic[s[::-1]] -= 1
            if dic[s[::-1]] == 0:
                del dic[s[::-1]]
            ans += 1
if len(dic) != 0:
    print(-1)
else:
    print(ans)
        
        
