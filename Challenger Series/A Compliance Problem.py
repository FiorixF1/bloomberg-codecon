#Problem        : A Compliance Problem
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

def is_palindrome(word):
    i = 0
    j = len(word)-1
    while (i < j):
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

def can_pass(word):
    PALINDROME = is_palindrome(word)
    if PALINDROME:
        return True
    
    letters = list(word)
    qualcosa = len(letters)
    for i in range(qualcosa):
        if letters[i] != None:
            for j in range(qualcosa):
                if i != j and letters[i] == letters[j]:
                    letters[i] = letters[j] = None
                    break
    
    not_found = 0
    for char in letters:
        if char != None:
            not_found += 1
    
    if not_found > 1:
        return False
    if not_found == 0:
        return True
    if qualcosa % 2 == 0:
        return False
    return True

word = input()
ok = can_pass(word)
if ok:
    print("yes")
else:
    print("no")
 
