#Problem        : Finals Spring 2015 - Galactic Exchange
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from math import sqrt

class Planet:
    def __init__(self, x, y, z, r, name):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.name = name

K = int(input())
planets = []

for k in range(K):
    curr = input().split(',')
    planet = Planet(int(curr[0]), int(curr[1]), int(curr[2]), float(curr[3]), curr[4])
    planets.append(planet)

graph = [[0 for l in range(K)] for k in range(K)]
visited = graph[0][:]

for i in range(K):
    x_1 = planets[i].x
    y_1 = planets[i].y
    z_1 = planets[i].z
    r_1 = planets[i].r
    for j in range(K):
        if i == j:
            continue
        x_2 = planets[j].x
        y_2 = planets[j].y
        z_2 = planets[j].z
        r_2 = planets[j].r
        dist = sqrt((x_1-x_2)**2 + (y_1-y_2)**2 + (z_1-z_2)**2)
        if dist <= r_1:
            graph[i][j] = 1
        if dist <= r_2:
            graph[j][i] = 1

components = []
#print(graph)

def count_components_from(graph, curr_planet, curr_set):
    global visited, K
    #if visited[curr_planet]:
    #    return
    
    curr_set.add(curr_planet)
    visited[curr_planet] = 1
    
    # per ogni figlio
    for k in range(K):
        if graph[curr_planet][k] and not visited[k]:
            count_components_from(graph, k, curr_set)
    # per ogni padre
    for k in range(K):
        if graph[k][curr_planet] and not visited[k]:
            count_components_from(graph, k, curr_set)
    
    return curr_set
    
for k in range(K):
    if not visited[k]:
        components.append(count_components_from(graph, k, set([])))
    #print(components)
        
i = -1
length = -1
ans = set([])

for j in range(len(components)):
    if len(components[j]) > length:
        ans = components[j]
        length = len(components[j])
        i = j
        
result = sorted([planets[planet].name for planet in ans])
print(','.join(result))
        

