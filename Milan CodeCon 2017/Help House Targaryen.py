#Problem        : Help House Targaryen !
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

N = int(input())
string = input()

if "010" not in string:
    print("0")
else:
    newString = string
    del string
    ans = 0
    for i in range(N-2):
        if newString[i:i+3] == "010":
            #print(newString[i:i+3]) # DEBUG
            newString = newString[:i] + "011" + newString[i+3:]
            ans += 1
    print(ans)
