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

x = int(input())

heights = []
for n in range(x):
    heights.append(int(input()))

ordered = sorted(heights)
ans = 0
for i in range(x):
    if ordered[i] == heights[i]:
        continue
    j = i+1
    while j < x and heights[j] != ordered[i]:
        j += 1
    if j != x:
        heights[i], heights[j] = heights[j], heights[i]
        ans += 1

print(ans)
