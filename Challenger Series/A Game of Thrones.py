#Problem        : 2016 Qualifiers - A Game of Thrones
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

N = int(input())

class House:
    def __init__(self, name, sworn, b, b_names):
        self.name = name
        self.sworn = sworn
        self.b = b
        self.b_names = b_names
        self.up = None

houses = {}
for n in range(N):
    token = input().split()
    if len(token) == 3:
        house = House(token[0], int(token[1]), int(token[2]), [])
    else:
        house = House(token[0], int(token[1]), int(token[2]), token[3:])
    houses[house.name] = house

# costruisco albero con dipendenze
for name in houses:
    for b in houses[name].b_names:
        houses[b].up = houses[name]
        
# trova radice
for name in houses:
    if houses[name].up == None:
        root = houses[name]
        break

def fai_cose(houses, root):
    if root.b_names == []:
        return
    else:
        for i in range(root.b):
            fai_cose(houses, houses[root.b_names[i]])
    max_sworns, new = -1, None
    for son in root.b_names:
        h_son = houses[son]
        if h_son.sworn > max_sworns:
            max_sworns = h_son.sworn
            new = h_son
        elif h_son.sworn == max_sworns and h_son.name < new.name:
            new = h_son
    
    if max_sworns >= root.sworn + 3:
        new.up = root.up
        root.up = new
        if new.up != None:
            old_index = new.up.b_names.index(root.name)
            new.up.b_names[old_index] = new.name
        vecchi_figli_di_root = root.b_names[:]
        vecchi_figli_di_new = new.b_names[:]
        root.b_names = vecchi_figli_di_new[:]
        new.b_names = vecchi_figli_di_root[:]
        
        old_index = new.b_names.index(new.name)
        new.b_names[old_index] = root.name
        new.b = len(new.b_names)
        root.b = len(root.b_names)
        
        for son in new.b_names:
            houses[son].up = new
        for son in root.b_names:
            houses[son].up = root

fai_cose(houses, root)

levelToHouses = dict()
def DFS(houses, root, level = 0):
    if level not in levelToHouses:
        levelToHouses[level] = [root.name]
    else:
        levelToHouses[level].append(root.name)
    for b in root.b_names:
        DFS(houses, houses[b], level+1)

# trova nuova radice
for name in houses:
    if houses[name].up == None:
        root = houses[name]
        break

DFS(houses, root)
for i in sorted(levelToHouses.keys()):
    print(' '.join(sorted(levelToHouses[i])))