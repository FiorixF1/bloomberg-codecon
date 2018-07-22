#Problem        : Laundry Day
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

"""
WARNING: this code seems legit and rational but IT DOES NOT PASS the private tests.
I don't know why. If you catch the reason, it would be kind to let us know :)
"""

import sys

data = sys.stdin.read().splitlines()

clothes = []
for line in data :
    clothes.append(line.lower())
    
clothes_counter = {}
for c in clothes:
    if c in clothes_counter:
        clothes_counter[c] += 1
    else:
        clothes_counter[c] = 1
        
# ... #

clothes = sorted(list(set(clothes)))
for c in clothes:
    if ' sock' in c:
        # ... #
        boh = clothes_counter[c]
        if boh % 2 == 0 and boh != 0:
            for i in range(boh//2):
                print(str(1) + "|" + c )
        elif boh % 2 == 1 and boh != 1:
            for i in range(boh//2):
                print(str(1) + "|" + c )
            print(str(0) + "|" + c )
        elif boh == 1:
             print(str(0) + "|" + c )
    else:
        print(str(clothes_counter[c]) + "|" + c)