#Problem        : 2016 Qualifiers - Uncle's Super Birthday Party
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from math import ceil, floor, sqrt

INF = 10000

# Le coordinate sono intere
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __repr__(self):
        return str(self.x) + ' ' + str(self.y)

# @param tre punti p, q, r
# @return vero se il punto q giace sul segmento pr
# WARNING: la funzione assume che i tre punti siano allineati!
def onSegment(p, q, r):
    if q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y):
        return True
    return False

# @param tre punti p, q, r
# @return 0 se sono allineati, 1 se sono in senso orario, 2 se sono in senso antiorario
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

    if val == 0: return 0
    return 1 if val > 0 else 2

# @param due segmenti p1q1 e p2q2
# @return vero se i due segmenti si intersecano
def doIntersect(p1, q1, p2, q2):
    # Find the four orientations needed for general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if (o1 != o2 and o3 != o4):
        return True

    # Special Cases
    # p1, q1 and p2 are colinear and p2 lies on segment p1q1
    if (o1 == 0 and onSegment(p1, p2, q1)): return True

    # p1, q1 and q2 are colinear and q2 lies on segment p1q1
    if (o2 == 0 and onSegment(p1, q2, q1)): return True

    # p2, q2 and p1 are colinear and p1 lies on segment p2q2
    if (o3 == 0 and onSegment(p2, p1, q2)): return True

    # p2, q2 and q1 are colinear and q1 lies on segment p2q2
    if (o4 == 0 and onSegment(p2, q1, q2)): return True

    return False  # Doesn't fall in any of the above cases

# @param polygon: un poligono espresso come insieme ordinato di punti
# @param n: il numero di vertici del poligono
# @param p: il punto in questione
# @return vero se il punto e' all'interno del poligono
def isInside(polygon, n, p):
    # There must be at least 3 vertices in polygon
    if (n < 3): return False

    # Create a point for line segment from p to infinite
    extreme = Point(INF, p.y)

    # Count intersections of the above line with sides of polygon
    count = 0
    i = 0
    
    next = (i+1) % n
    # Check if the line segment from 'p' to 'extreme' intersects
    # with the line segment from 'polygon[i]' to 'polygon[next]'
    if (doIntersect(polygon[i], polygon[next], p, extreme)):
        # If the point 'p' is colinear with line segment 'i-next',
        # then check if it lies on segment. If it lies, return True,
        # otherwise count as two intersections
        if (orientation(polygon[i], p, polygon[next]) == 0):
            res = onSegment(polygon[i], p, polygon[next])
            if (res): return True
            else: count += 1
        count += 1
    i = next
    
    while (i != 0):
        next = (i+1) % n
        if (doIntersect(polygon[i], polygon[next], p, extreme)):
            if (orientation(polygon[i], p, polygon[next]) == 0):
                res = onSegment(polygon[i], p, polygon[next])
                if (res): return True
                else: count += 1
            count += 1
        i = next
    
    # Return True if count is odd, False otherwise
    return count & 1  # Same as (count % 2 == 1)

# Dato un segmento ab ed una coordinata y, dammi la x
def interpolate_x(a, b, y):
    x1 = a.x
    x2 = b.x
    y1 = a.y
    y2 = b.y

    return (y - y1)*(x2 - x1)/(y2 - y1) + x1

# Dato un segmento ab ed una coordinata x, dammi la y
def interpolate_y(a, b, x):
    x1 = a.x
    x2 = b.x
    y1 = a.y
    y2 = b.y

    return (y2 - y1)/(x2 - x1)*(x - x1) + y1

def filtra(candidates, frm, to):
    # I due punti non formano un lato in diagonale, nessun candidato viene rimosso
    if (frm.x == to.x or frm.y == to.y):
        return
    
    if (frm.y > to.y):
        frm, to = to, frm
    
    x1 = frm.x
    x2 = to.x
    y1 = frm.y
    y2 = to.y

    # Gestisco quattro casi sul lato frm-to:
    # 1) Angolo <= 45 gradi con x crescente verso destra
    # 2) Angolo > 45 gradi con x crescente verso destra
    # 3) Angolo <= 45 gradi con x crescente verso sinistra
    # 4) Angolo > 45 gradi con x crescente verso sinistra
    # La y e' sempre crescente verso l'alto
    
    # Caso 1, si possono verificare queste situazioni:
    # 1) x pari = lungo un vertice
    # 2) x dispari = nel centro di un blocco
    # 3) y intero pari = lungo un vertice
    # 4) y intero dispari oppure FP = in mezzo ad un blocco
    # Combinazioni possibili:
    # 1 + 3 -> non fare niente
    # 1 + 4 -> rimuovi blocco in x-1 e in x+1
    # 2 + 3 -> rimuovi blocco in y-1 e in y+1
    # 2 + 4 -> rimuovi blocco corrente
    
    # Caso 2: si invertono x e y dato che si itera sulle y
    # Caso 3: come il caso 1, ma il ciclo for decrementa x
    # Caso 4: come il caso 2, ma il ciclo for decrementa y
    
    if (abs(x1-x2) >= abs(y1-y2)):     # caso <= 45 gradi
        if (x1 < x2):  # caso si cresce verso destra
            for x in range(x1, x2):
                y = interpolate_y(frm, to, x)
                if x % 2 == 0:  # x pari
                    if y == int(y) and int(y) % 2 == 0:  # y intero pari
                        pass
                    else:  # y intero dispari o FP
                        coord = floor(y)
                        if coord % 2 == 0: coord += 1
                        try: candidates.remove(Point(x-1, coord))
                        except: pass
                        try: candidates.remove(Point(x+1, coord))
                        except: pass
                else:  # x dispari
                    if y == int(y) and int(y) % 2 == 0:  # y intero pari
                        try: candidates.remove(Point(x, y-1))
                        except: pass
                        try: candidates.remove(Point(x, y+1))
                        except: pass
                    else:  # y intero dispari o FP
                        coord = floor(y)
                        if coord % 2 == 0: coord += 1
                        try: candidates.remove(Point(x, coord))
                        except: pass
        else:          # caso si cresce verso sinistra
            for x in range(x1, x2, -1):
                y = interpolate_y(frm, to, x)
                if x % 2 == 0:  # x pari
                    if y == int(y) and int(y) % 2 == 0:  # y intero pari
                        pass
                    else:  # y intero dispari o FP
                        coord = floor(y)
                        if coord % 2 == 0: coord += 1
                        try: candidates.remove(Point(x-1, coord))
                        except: pass
                        try: candidates.remove(Point(x+1, coord))
                        except: pass
                else:  # x dispari
                    if y == int(y) and int(y) % 2 == 0:  # y intero pari
                        try: candidates.remove(Point(x, y-1))
                        except: pass
                        try: candidates.remove(Point(x, y+1))
                        except: pass
                    else:  # y intero dispari o FP
                        coord = floor(y)
                        if coord % 2 == 0: coord += 1
                        try: candidates.remove(Point(x, coord))
                        except: pass
    else:                              # caso > 45 gradi
        if (x1 < x2):  # caso si cresce verso destra
            for y in range(y1, y2):
                x = interpolate_x(frm, to, y)
                if y % 2 == 0:  # y pari
                    if x == int(x) and int(x) % 2 == 0:  # x intero pari
                        pass
                    else:  # x intero dispari o FP
                        coord = floor(x)
                        if coord % 2 == 0: coord += 1
                        try: candidates.remove(Point(coord, y-1))
                        except: pass
                        try: candidates.remove(Point(coord, y+1))
                        except: pass
                else:  # y dispari
                    if x == int(x) and int(x) % 2 == 0:  # x intero pari
                        try: candidates.remove(Point(x-1, y))
                        except: pass
                        try: candidates.remove(Point(x+1, y))
                        except: pass
                    else:  # x intero dispari o FP
                        coord = floor(x)
                        if coord % 2 == 0: coord += 1
                        try: candidates.remove(Point(coord, y))
                        except: pass
        else:          # caso si cresce verso sinistra
            for y in range(y1, y2, -1):
                x = interpolate_x(frm, to, y)
                if y % 2 == 0:  # y pari
                    if x == int(x) and int(x) % 2 == 0:  # x intero pari
                        pass
                    else:  # x intero dispari o FP
                        coord = floor(x)
                        if coord % 2 == 0: coord += 1
                        try: candidates.remove(Point(coord, y-1))
                        except: pass
                        try: candidates.remove(Point(coord, y+1))
                        except: pass
                else:  # y dispari
                    if x == int(x) and int(x) % 2 == 0:  # x intero pari
                        try: candidates.remove(Point(x-1, y))
                        except: pass
                        try: candidates.remove(Point(x+1, y))
                        except: pass
                    else:  # x intero dispari o FP
                        coord = floor(x)
                        if coord % 2 == 0: coord += 1
                        try: candidates.remove(Point(coord, y))
                        except: pass



N = int(input())

max_x = -1
max_y = -1
min_x = 100
min_y = 100

polygon = []
for i in range(N):
    # Salvo le coordinate raddoppiate per poter accedere facilmente ai centri dei blocchi
    x, y = [int(i)*2 for i in input().split()]
    if (x > max_x): max_x = x
    if (y > max_y): max_y = y
    if (x < min_x): min_x = x
    if (y < min_y): min_y = y
    polygon.append(Point(x, y))
    
# Trova blocchi il cui centro sta dentro il poligono
candidates = []
for i in range(min_x+1, max_x, 2):
    for j in range(min_y+1, max_y, 2):
        p = Point(i, j)
        if (isInside(polygon, N, p)):
            candidates.append(Point(i, j))

# Rimuoviamo i blocchi che non sono interamente dentro il poligono, iterando sui lati
for i in range(N-1):
    filtra(candidates, polygon[i], polygon[i+1])

# I blocchi rimasti sono quelli da contare
ans = len(candidates)
print(ans)