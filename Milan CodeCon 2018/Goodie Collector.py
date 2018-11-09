#Problem        : Goodie Collector
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

"""
WARNING: this code has been written AFTER the contest has ended. It means the solution
has not been submitted and there is no guarantee it is the actual working solution.
"""

ans = 0

def greedy(goods, presi, posizione):
    global ans
    
    if posizione >= n:
        ans = max(ans, len(set(presi)))
        return
    
    elemento = goods[posizione]
    for nuova_posizione in range(posizione+d, n+d):
        presi.append(elemento)
        greedy(goods, presi[:], nuova_posizione)
        presi.remove(elemento)
       
# n numero di tavoli
# k numero di cose da prendere
# distanza minima
n, k, d = [int(i) for i in input().split()]
goods = [int(i) for i in input().split()]

#print(goods)
for partenza in range(0, n-d):
    greedy(goods, [], partenza)

print(ans)