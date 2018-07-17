#Problem        : Fake Profiles
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

N = int(input())

coords = []
for n in range(N):
    c = [int(i) for i in input().split()]
    coords.append(c)

dic = {}
for i in range(N):
    if coords[i] == '!':
        continue
    if coords[i][1] in dic:
        dic[coords[i][1]].append(coords[i])
    else:
        dic[coords[i][1]] = [coords[i]]
    coords[i] = '!'
                
#print(dic)
def avg(lista):
    somma = 0
    #print(lista)
    for elem in lista:
        somma += elem[0]
        
    return somma/len(lista)

medie = []
for k in dic:
    medie.append(avg(dic[k]))
    
primo = medie[0]
for val in medie:
    esiste = True
    if val != primo:
        esiste = False
        break
if esiste:
    print(1)
else:
    print(0)
