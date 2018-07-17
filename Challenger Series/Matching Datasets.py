#Problem        : Matching Datasets
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

K = int(input())
original_sets = []
new_sets = []

for i in range(K):
    row = input().split(',')
    for i in range(len(row)):
        row[i] = float(row[i])
    original_sets.append(row)

for i in range(K):
    row = input().split(',')
    for i in range(len(row)):
        row[i] = float(row[i])
    new_sets.append(row)

indexes = []

for i in range(K):
    try:
        x = new_sets.index(original_sets[i])
    except:
        differences = [] # inserisco le differenze con ogni new_set
        for j in range(K): # per ogni new_set
            diff = 0
            for k in range(len(original_sets[0])): # per ogni valore nel set
                diff += original_sets[i][k] - new_sets[j][k]
            differences.append(abs(diff))
        x = differences.index(min(differences))
    finally:
        indexes.append(x)

for i in range(K):
    print(str(i) + ',' + str(indexes[i]))

