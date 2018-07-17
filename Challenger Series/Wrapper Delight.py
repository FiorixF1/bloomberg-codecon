#Problem        : 2016 Qualifiers - Wrapper's Delight
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

N = int(input())
text = input().split()
ans = ""

i = 0
line = ""
length = len(text)
TILDE = False
while i < length:
    word = text[i]
    if '~' in word:
        TILDE = True
        index = word.index('~')
        word_two = word[index+1:]
        word = word[:index]
    
    if len(word) > N and line == "":
        ans += word + '\n'
        i += 1
        if TILDE:
            TILDE = False
            i -= 1
            text[i] = word_two
        continue
    
    old = line
    if line == "":
        line = word
    else:
        line = line + ' ' + word
    
    if len(line) > N:
        ans += old + '\n'
        line = ""
    else:
        i += 1
        if TILDE:
            ans += line + '\n'
            line = ""
            TILDE = False
            i -= 1
            text[i] = word_two
ans += line
print(ans)
