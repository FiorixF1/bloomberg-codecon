#Problem        : Base Arithmetic
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.8
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from __future__ import print_function
import sys

def base(num):
    for c in num:
        if c == 'F':
            return 16
    for c in num:
        if c == 'E':
            return 15
    for c in num:
        if c == 'D':
            return 14
    for c in num:
        if c == 'C':
            return 13
    for c in num:
        if c == 'B':
            return 12
    for c in num:
        if c == 'A':
            return 11
    for c in num:
        if c == '9':
            return 10
    for c in num:
        if c == '8':
            return 9
    for c in num:
        if c == '7':
            return 8
    for c in num:
        if c == '6':
            return 7
    for c in num:
        if c == '5':
            return 6
    for c in num:
        if c == '4':
            return 5
    for c in num:
        if c == '3':
            return 4
    for c in num:
        if c == '2':
            return 3
    for c in num:
        if c == '1':
            return 2

def convert_to_10(num, base):
    lenght = len(num)-1
    result = 0
    power = 0
    while lenght >= 0:
        try:
            digit = int(num[lenght])
        except:
            if num[lenght] == 'A':
                digit = 10
            elif num[lenght] == 'B':
                digit = 11
            elif num[lenght] == 'C':
                digit = 12
            elif num[lenght] == 'D':
                digit = 13
            elif num[lenght] == 'E':
                digit = 14
            elif num[lenght] == 'F':
                digit = 15
        finally:
            result = result + digit*base**power
            power += 1
            lenght -= 1
    return result

X = raw_input()
Y = raw_input()

X = X.upper()
Y = Y.upper()

base_x = base(X)
base_y = base(Y)

X_10 = convert_to_10(X, base_x)
Y_10 = convert_to_10(Y, base_y)

print(X_10+Y_10)
