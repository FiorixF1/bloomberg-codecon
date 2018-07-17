#Problem        : Messed-up Manuscript
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

N = int(input())
pages = [int(i) for i in input().split()]

# parte crescente
primo = []
secondo = []
flag = False
curr = float('-inf')
for i in range(N):
    if not flag and pages[i] >= curr:
        primo.append(pages[i])
        curr = pages[i]
    else:
        flag = True
        secondo.append(pages[i])
        curr = pages[i]
unione = secondo + primo
ordinato = sorted(unione)
if unione == ordinato and flag:
    print(1)
else:
    # parte decrescente
    primo = []
    secondo = []
    flag = False
    curr = float('+inf')
    for i in range(N):
        if not flag and pages[i] <= curr:
            primo.append(pages[i])
            curr = pages[i]
        else:
            flag = True
            secondo.append(pages[i])
            curr = pages[i]
    unione = secondo + primo
    ordinato = sorted(unione)[::-1]
    if unione == ordinato and flag:
        print(1)
    else: # parte di tutti uguali
        uguali = True
        first = pages[0]
        for p in pages:
            if p != first:
                uguali = False
                break
        if uguali:
            print(1)
        else:
            print(0)
