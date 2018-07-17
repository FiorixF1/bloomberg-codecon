#Problem        : 2016 Qualifiers - Assistant to the District Hero
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from math import sqrt

def dist(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def is_ok(x1, y1, x2, y2):
    return x1 <= x2 and y1 <= y2
    
ans = 0
N = int(input())+1
coords = [[0, 0]]
for n in range(N-1):
    coord = [int(i) for i in input().split()]
    coords.append(coord)

distances = [[] for n in range(N)]

for i in range(N):
    for j in range(N):
        distances[i].append(dist(coords[i][0], coords[i][1], coords[j][0], coords[j][1]))

curr = 0
while True:
    distance = float('+inf')
    prossimo = None
    for i in range(N):
        if i != curr and distances[curr][i] < distance and is_ok(coords[curr][0], coords[curr][1], coords[i][0], coords[i][1]):
            distance = distances[curr][i]
            prossimo = i
    if prossimo == None:
        break
    curr = prossimo
    ans += 1

print(ans)
    
    
