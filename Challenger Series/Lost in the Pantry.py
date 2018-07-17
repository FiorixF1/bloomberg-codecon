#Problem        : 2016 Qualifiers - Lost in the Pantry
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

R, C = [int(i) for i in input().split()]
maze = [[0 for c in range(C)] for r in range(R)]
ans = 0

for r in range(R):
    line = list(input())
    maze[r] = line

start_r, start_c = [int(i) for i in input().split()]
end_r, end_c = [int(i) for i in input().split()]
char = maze[start_r][start_c]

def find_path(maze, curr_r, curr_c):
    global ans, R, C, start_r, start_c, end_r, end_c
    if curr_r == end_r and curr_c == end_c:
        maze[curr_r][curr_c] = '-'
        ans += 1
        return True
    elif curr_r < 0 or curr_r >= R or curr_c < 0 or curr_c >= C or maze[curr_r][curr_c] != char:
        return False
    elif maze[curr_r][curr_c] == '-':
        return False
    else:
        maze[curr_r][curr_c] = '-'
        ans += 1
        if find_path(maze, curr_r-1, curr_c):
            return True
        elif find_path(maze, curr_r, curr_c+1):
            return True
        elif find_path(maze, curr_r+1, curr_c):
            return True
        elif find_path(maze, curr_r, curr_c-1):
            return True
        else:
            maze[curr_r][curr_c] = '_'
            ans -= 1
            return False
            
FOUND = find_path(maze, start_r, start_c)
print(ans)
