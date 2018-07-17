#Problem        : Mystery Message
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

strings = input().split()
alfabeto1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabeto2 = 'abcdefghijklmnopqrstuvwxyz'
letteraCrittata = strings[0][0]
letteraGiusta = strings[-1][0]

if letteraCrittata in alfabeto1:
    indiceCritto = alfabeto1.index(letteraCrittata)
    indiceGiusto = alfabeto1.index(letteraGiusta)
    alfabeto = alfabeto1
else:
    indiceCritto = alfabeto2.index(letteraCrittata)
    indiceGiusto = alfabeto2.index(letteraGiusta)
    alfabeto = alfabeto2
    
walker = indiceGiusto
ans = 0
while alfabeto[walker] != letteraCrittata:
    ans += 1
    walker += 1
    walker = walker % 26
    
print(ans)
