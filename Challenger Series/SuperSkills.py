#Problem        : 2016 Qualifiers - SuperSkills
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

N = int(input())
nameToLanguages = {}
for n in range(N):
    line = input().split()
    name = line[0]
    language = line[1]
    if name not in nameToLanguages:
        nameToLanguages[name] = [language]
    else:
        nameToLanguages[name].append(language)

R = int(input())
friends = {}
for r in range(R):
    amici = input().split()
    if amici[0] not in friends:
        friends[amici[0]] = {amici[1]}
    else:
        friends[amici[0]].add(amici[1])
        
    if amici[1] not in friends:
        friends[amici[1]] = {amici[0]}
    else:
        friends[amici[1]].add(amici[0])
#print(nameToLanguages)
#print(friends)
me = input()
myLang = nameToLanguages[me]
chosenFriends = []
for friend in friends[me]:
    for language in nameToLanguages[friend]:
        if language not in myLang:
            chosenFriends.append((friend, language))

langToLearn = set({})
for couple in chosenFriends:
    langToLearn.add(couple[1])
for lang in myLang:
    if lang in langToLearn:
        langToLearn.remove(lang)
#print(langToLearn)
#print(chosenFriends)

chosenNames = set([])
while not len(langToLearn) == 0:
    counter = {}
    for couple in chosenFriends:
        if couple[0] not in counter:
            counter[couple[0]] = 1
        else:
            counter[couple[0]] += 1
    maximum = -1
    nextFriend = None
    for k in counter:
        if counter[k] > maximum:
            maximum = counter[k]
            nextFriend = k
    chosenNames.add(nextFriend)

    learntLangs = set([])
    for couple in chosenFriends:
        if couple[0] == nextFriend:
            if couple[1] in langToLearn:
                learntLangs.add(couple[1])
                
    for couple in chosenFriends:
        if couple[0] == nextFriend:
            if couple[1] in learntLangs:
                langToLearn.remove(couple[1])
                
    chosenFriends = list(filter(lambda x: x[0] != nextFriend, chosenFriends))
    chosenFriends = list(filter(lambda x: x[1] in langToLearn, chosenFriends))
    
print(','.join(sorted(list(chosenNames))))

