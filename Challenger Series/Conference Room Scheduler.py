#Problem        : Finals Spring 2015 - Conference Room Scheduler
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

def booking(time_table, roomID, start_time, slots):
    for i in range(start_time-1, start_time+slots-1):
        if time_table[roomID-1][i] == 1:
            return 'N'
    for i in range(start_time-1, start_time+slots-1):
        time_table[roomID-1][i] = 1
    return 'Y'

def query(time_table, start_time, slots):
    free_rooms = []
    for i in range(len(time_table)):
        FREE = True
        for j in range(start_time-1, start_time+slots-1):
            if time_table[i][j] == 1:
                FREE = False
        if FREE:
            free_rooms.append(str(i+1))
    return free_rooms

data = sys.stdin.read().splitlines()

N = int(data[0])

# ROOM 1-INDEXED IN INPUT, NOT 0!
time_table = [[0 for m in range(32)] for n in range(N)]

request = data[1:]
for r in request:
    param = r.split('-')
    #print(param)
    if len(param) == 3:
        free = booking(time_table, int(param[0]), int(param[1]), int(param[2]))
        print(free)
    elif len(param) == 2:
        free_rooms = query(time_table, int(param[0]), int(param[1]))
        if len(free_rooms) == 0:
            print('None')
        else:
            print(' '.join(free_rooms))

