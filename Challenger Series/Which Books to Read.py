#Problem        : Which Books to Read
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.8
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from __future__ import print_function
import sys

data = sys.stdin.read().splitlines()

user = data[0]
D = int(data[1])
N = int(data[2])
M = int(data[3])

network = [[0]]  # grafo che indica una relazione tra utenti
namesToID = {}  # ad ogni nome utente associa un ID, indice di network
namesToID[user] = 0
ID = 1
for n in data[4:4+N]:
    names = n.split('|')
    name1 = names[0]
    name2 = names[1]
    if name1 not in namesToID:
        namesToID[name1] = ID
        ID += 1
        for sublist in network:
            sublist.append(0)
        network.append(network[0][:])
    if name2 not in namesToID:
        namesToID[name2] = ID
        ID += 1
        for sublist in network:
            sublist.append(0)
        network.append(network[0][:])
    network[namesToID[name1]][namesToID[name2]] = network[namesToID[name2]][namesToID[name1]] = 1
    
IDToBooks = {}  # ad ogni utente (col suo ID) associa un set di libri
for boh in range(ID):
    IDToBooks[boh] = set([])  # persone che non hanno letto libri
for m in data[4+N:4+N+M]:
    books = m.split('|')
    index = namesToID[books[0]]
    IDToBooks[index] = set(books[1:])

# cerca grado separazione per ogni utente con Dijkstra
def find_next(D, visited):
    ans = -1
    d_min = float('+inf')
    for i in range(N):
        if D[i] < d_min and not visited[i]:
            ans = i
            d_min = D[i]
    return ans

def Dijkstra(graph, start, N, visited):
    D = []
    for dist in graph[start]:
        if dist == 0:
            D.append(float('+inf'))
        else:
            D.append(dist)
    D[start] = 0
    for i in range(N):
        curr = find_next(D, visited)
        if curr == -1:
            return D
        visited[curr] = 1
        for j in range(N):
            if graph[curr][j]:
                if D[j] > (D[curr] + graph[curr][j]):
                    D[j] = D[curr] + graph[curr][j]
    return D

visited = [0 for i in range(len(network[0]))]   
gradiSeparazione = Dijkstra(network, namesToID[user], len(network[0]), visited)

ans = 0
libriUser = set(IDToBooks[namesToID[user]])

for i in range(len(network[0])):
    if gradiSeparazione[i] <= D and gradiSeparazione[i] != 0:
        for book in IDToBooks[i]:
            if book not in libriUser:
                libriUser.add(book)
                ans += 1
                
print(ans)
