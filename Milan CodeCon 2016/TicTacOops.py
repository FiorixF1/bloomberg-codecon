#Problem        : TicTacOops
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

N = int(input())

grid = [None, None, None, None, None, None, None, None, None]
turn = True  # true e' turno di X, false e' turno di O
X_moves = []
O_moves = []
for n in range(N):
    move = int(input())
    if turn and move != -1:
        grid[move] = 'X'
        turn = False
        X_moves.append(move)
    elif not turn and move != -1:
        grid[move] = 'O'
        turn = True
        O_moves.append(move)
    elif move == -1:
        if turn:  # se e' X devi togliere O
            back = O_moves.pop()
            grid[back] = None
            turn = False
        else:
            back = X_moves.pop()
            grid[back] = None
            turn = True
        
def winner(grid):
    niente = True
    for elem in grid:
        if elem != None:
            niente = False
    if niente:
        print('D')
        return
    if grid[0] == grid[1] and grid[1] == grid[2]:
        print(grid[0])
    elif grid[3] == grid[4] and grid[4] == grid[5]:
        print(grid[3])
    elif grid[6] == grid[7] and grid[7] == grid[8]:
        print(grid[6])
    elif grid[0] == grid[3] and grid[3] == grid[6]:
        print(grid[0])
    elif grid[1] == grid[4] and grid[4] == grid[7]:
        print(grid[1])
    elif grid[2] == grid[5] and grid[5] == grid[8]:
        print(grid[2])
    elif grid[0] == grid[4] and grid[4] == grid[8]:
        print(grid[0])
    elif grid[2] == grid[4] and grid[4] == grid[6]:
        print(grid[2])
    else:
        print('D')

winner(grid)
