#Problem        : Tracing Vile Angus
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

def trasla(cyphertext, s):
    length = len(cyphertext)
    for i in range(s[0], length):
        UPPERCASE = cyphertext[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if cyphertext[i].lower() == s[2]:
            if UPPERCASE:
                cyphertext[i] = s[1].upper()
            else:
                cyphertext[i] = s[1]
        elif cyphertext[i].lower() == s[1]:
            if UPPERCASE:
                cyphertext[i] = s[2].upper()
            else:
                cyphertext[i] = s[2]
            
cyphertext = input()
N = int(input())

subst = []
for n in range(N):
    pos, first, second = input().split()
    pos = int(pos)
    subst.append((pos, first, second))
    
if N == 0:
    print(cyphertext)
else:
    cyphertext = list(cyphertext)
    for s in reversed(subst):
        trasla(cyphertext, s)
    print(''.join(cyphertext))
    