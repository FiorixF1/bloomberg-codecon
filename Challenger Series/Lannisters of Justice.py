#Problem        : 2016 Qualifiers - Lannisters of Justice
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

operation = input()

numbers = []
operations = []
curr_n = ""

for char in operation:
    if char.isdigit():
        curr_n += char
    else:
        numbers.append(int(curr_n))
        curr_n = ""
        operations.append(char)
numbers.append(int(curr_n))

#print(numbers)
#print(operations)
i = 0
limit = len(operations)
while i < limit:
    if operations[i] == '-':
        numbers[i+1] = numbers[i]-numbers[i+1]
        del numbers[i]
        del operations[i]
        limit -= 1
    else:
        i += 1
    
i = 0
while i < limit:
    if operations[i] == '/':
        numbers[i+1] = numbers[i]//numbers[i+1]
        del numbers[i]
        del operations[i]
        limit -= 1
    else:
        i += 1
    
i = 0
while i < limit:
    if operations[i] == '+':
        numbers[i+1] = numbers[i]+numbers[i+1]
        del numbers[i]
        del operations[i]
        limit -= 1
    else:
        i += 1
    
i = 0
while i < limit:
    if operations[i] == '*':
        numbers[i+1] = numbers[i]*numbers[i+1]
        del numbers[i]
        del operations[i]
        limit -= 1
    else:
        i += 1
        
print(numbers[0])
