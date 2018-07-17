#Problem        : 2016 Qualifiers - Travel to the West
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

N = int(input())
airToDest = {}  # il grafo, considerato NON ORIENTATO
visited = {}
for n in range(N):
    couple = input().split()
    if couple[0] not in airToDest:
        airToDest[couple[0]] = [couple[1]]
    else:
        airToDest[couple[0]].append(couple[1])
    if couple[1] not in airToDest:
        airToDest[couple[1]] = []
    visited[couple[0]] = 0
    visited[couple[1]] = 0
    
    

paths = 0
def solve(graph, currAir, N, visited):
    global paths
    visited[currAir] = 1
    if currAir ==  "SFO":
        paths += 1
        return
    for dest in airToDest[currAir]:
        if not visited[dest]:
            solve(graph, dest, N, visited.copy())  # ATTENZIONE, UNA COPIA DI VISITED?
            
solve(airToDest, "JFK", N, visited)
print(paths)
