#Problem        : Finals Spring 2015 - Golf Course
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

N = int(input())

ans = 0

def find_next(curr):
    if curr == 1:
        return (6, 8)
    elif curr == 2:
        return (7, 9)
    elif curr == 3:
        return (4, 8)
    elif curr == 4:
        return (3, 9, 0)
    elif curr == 5:
        return None
    elif curr == 6:
        return (1, 7, 0)
    elif curr == 7:
        return (2, 6)
    elif curr == 8:
        return (1, 3)
    elif curr == 9: # ATTENZIONE
        return (2, 4)
    elif curr == 0:
        return (4, 6)

def count_path(max_moves, curr_moves, curr_pos):
    global ans
    if curr_moves == max_moves:
        if curr_pos == 9:
            ans += 1
   # elif curr_pos == 9:
   #     return
    else:
        next_move = find_next(curr_pos)
        for move in next_move:
            count_path(max_moves, curr_moves+1, move)
    
count_path(N, 0, 1)
print(ans)
