#Problem        : Which Books to Read
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.8
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

"""
WARNING: this code has been written AFTER the contest has ended. It means the solution
has not been submitted and there is no guarantee it is the actual working solution.
"""

from __future__ import print_function

def indexEndG(string, G_index):
	i = G_index+1
	cont = 0
	while cont < 4:
		print('ricorsione...')
		if string[i] == 'b' or string[i] == 'w':
			cont += 1
			i += 1
		else:
			cont += 1
			i = indexEndG(string, i)
	return i

first = input()
second = input()

i = 0
j = 0
result = ""
i_limit = len(first)
j_limit = len(second)
while i < i_limit and j < j_limit:
	print('seguo')
	if (first[i] == 'b' and second[j] == 'b'):
		result += "b"
		i += 1
		j += 1
	elif (first[i] == 'g' and second[j] == 'g'):
		result += "g"
		i += 1
		j += 1
	elif (first[i] == 'w' and second[j] == 'w'):
		result += "w"
		i += 1
		j += 1
	elif (first[i] == 'b' and second[j] == 'w' or first[i] == 'w' and second[j] == 'b'):
		result += "b"
		i += 1
		j += 1
	elif (first[i] == 'b' and second[j] == 'g'):  # 
		endG = indexEndG(second, j)
		result += "b"
		i += 1
		j = endG
	elif (first[i] == 'g' and second[j] == 'b'):  # 
		endG = indexEndG(first, i)
		result += "b"
		i = endG
		j += 1
	elif (first[i] == 'w' and second[j] == 'g'):  # 
		endG = indexEndG(second, j)
		result += second[j:endG]
		i += 1
		j = endG
	elif (first[i] == 'g' and second[j] == 'w'):  # 
		endG = indexEndG(first, i)
		result += first[i:endG]
		i = endG
		j += 1
	
	if result[-5:] == 'gbbbb':
		result = result[:-5] + 'b'
	if result[-5:] == 'gwwww':
		result = result[:-5] + 'w'

print(result)
