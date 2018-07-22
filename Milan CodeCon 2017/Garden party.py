#Problem        : Garden party
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

"""
WARNING: this code has been written AFTER the contest has ended. It means the solution
has not been submitted and there is no guarantee it is the actual working solution.
"""

import sys

H, W = [int(i) for i in input().split()]

grid = [[0 for w in range(W)] for h in range(H)]
# 0 vuol dire che ci puoi andare, 1 che c'e' acqua

def convert(x, y):
    global H, W
    # x = 0 implica column = 0, x = 50 implica colonna = 50
    column = x
    # y = 0 implica ultima riga H-1, se l'altezza è 10 allora y = 10 implica riga = 0
    # 0 9, 1 8, 27, 3 6, 4 5, 5 5, 6 4, 7 3, 8 2, 9 1, 10 0
    row = H-1-y
    return (row, column)

# applica l'algoritmo di flood filling in una griglia

# @param grid = la griglia da riempire sotto forma di matrice
# @param H = righe della matrice
# @param W = colonne della matrice
# @param start_i = riga di partenza del flood filling
# @param start_j = colonna di partenza del flood filling
# @param old = carattere da sostituire
# @param new = carattere nuovo da inserire
def fill(grid, H, W, start_i, start_j, old, new):
    if grid[start_i][start_j] != old:
        return

    grid[start_i][start_j] = new
    # sopra
    if start_i != 0:
        fill(grid, H, W, start_i-1, start_j, old, new)
    # alto destra
    if start_i != 0 and start_j != W-1:
        fill(grid, H, W, start_i-1, start_j+1, old, new)
    # destra
    if start_j != W-1:
        fill(grid, H, W, start_i, start_j+1, old, new)
    # basso destra
    if start_i != H-1 and start_j != W-1:
        fill(grid, H, W, start_i+1, start_j+1, old, new)
    # sotto
    if start_i != H-1:
        fill(grid, H, W, start_i+1, start_j, old, new)
    # basso sinistra
    if start_i != H-1 and start_j != 0:
        fill(grid, H, W, start_i+1, start_j-1, old, new)
    # sinistra
    if start_j != 0:
        fill(grid, H, W, start_i, start_j-1, old, new)
    # alto sinistra
    if start_j != 0 and start_i != 0:
        fill(grid, H, W, start_i-1, start_j-1, old, new)
        
        
        
N = int(input())
for n in range(N):
    x, y, r = [int(i) for i in input().split()]
    row, column = convert(x, y)
    for i in range(row-r, row+r+1):
        for j in range(column-r, column+r+1):
            try:
                if ((i-row)**2 + (j-column)**2)**0.5 <= r:
                    grid[i][j] = 1
            except:
                continue

for line in grid:
    x = list(map(str, line))
    print(' '.join(x))

for i in range(H):
    fill(grid, H, W, i, 0, 0, 2)

print()
for line in grid:
    x = list(map(str, line))
    print(' '.join(x))

posso = False
for i in range(H):
    if grid[i][W-1] == 2:
        posso = True
        break
    
if posso:
    print("CAKE")
else:
    print("NO CAKE")
            
