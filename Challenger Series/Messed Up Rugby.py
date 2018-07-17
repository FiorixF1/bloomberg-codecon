#Problem        : Messed up Rugby
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.8
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from __future__ import print_function
import sys

input = input()
CONVERTION = 7
TRY = 3
KICK = 2

entries = []

for i in range(33):
    for j in range(75):
        for k in range(112):
            if i*CONVERTION + j*TRY + k*KICK == input:
                elem = str(i) + " " + str(j) + " " + str(k)
                entries.append(elem)

for elem in entries:
    print(elem)
