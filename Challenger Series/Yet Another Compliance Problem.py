#Problem        : Yet Another Compliance Problem
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.8
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from __future__ import print_function
import sys
import math

def compute_repeat(token):
    repeat = []
    for i in range(len(token)-1):
        if token[i] == '':
            continue
        counter = 1
        for j in range(i+1, len(token)):
            if token[i] == token[j]:
                token[j] = ''
                counter += 1
        repeat.append(counter/2) # ATTENZIOHNE
    total_repeat = 1
    for elem in repeat:
        elem = math.factorial(elem)
        total_repeat *= elem
    return total_repeat
    



char_set = raw_input()
palindromi = 0
lenght = len(char_set)

token = []
for ch in char_set:
    token.append(ch)

ODD = 0
for i in range(lenght-1):
    if token[i] == '':
        continue
    FOUND = 0
    for j in range(i+1, lenght):
        if token[i] == token[j]:
            token[i] = token[j] = ''
            FOUND = 1
            break
    if FOUND:
        palindromi += 1
    else:
        if lenght % 2 == 1 and ODD == 0:
            ODD = 1
            continue
        palindromi = 0
        break

if palindromi == 0:
    print(0)
else:
    token = []
    for ch in char_set:
        token.append(ch)
    total_repeat = compute_repeat(token)
    palindromi = math.factorial(palindromi)/total_repeat
    print(palindromi)
