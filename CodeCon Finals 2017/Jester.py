#Problem        : Jester
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

"""
WARNING: this code has been written AFTER the contest has ended. It means the solution
has not been submitted and there is no guarantee it is the actual working solution.
"""

import sys

faceToPoints = {"J": 11, "Q": 12, "K": 13, "A": 14}

def calculatePoints(cards):
    faceCounter = {"J": 0, "Q": 0, "K": 0, "A": 0}
    for card in cards:
        if card != "Joker":
            faceCounter[card[0]] += 1

    maximumFace = None
    maxFaceCounter = -1
    for face in faceCounter:
        if faceCounter[face] > maxFaceCounter:
            maximumFace = face
            maxFaceCounter = faceCounter[face]

    # se ci sono carte che compaion lo stesso numero di volte, prendi la migliore
    if len(list(faceCounter.values())) != len(set(faceCounter.values())):
        if maxFaceCounter == faceCounter["A"]:
            maximumFace = "A"
        elif maxFaceCounter == faceCounter["K"]:
            maximumFace = "K"
        elif maxFaceCounter == faceCounter["Q"]:
            maximumFace = "Q"
        elif maxFaceCounter == faceCounter["J"]:
            maximumFace = "J"
    if "Joker" in cards:
        maxFaceCounter += 1
            
    pointsOfFaces = 0
    strongestValue = 0   # serve al joker
    for face in faceCounter:
        if face == maximumFace:
            strongestValue = max(strongestValue, faceToPoints[face]*faceCounter[face]*maxFaceCounter)
            pointsOfFaces += faceToPoints[face]*faceCounter[face]*maxFaceCounter
        else:
            strongestValue = max(strongestValue, faceToPoints[face]*faceCounter[face])
            pointsOfFaces += faceToPoints[face]*faceCounter[face]
    if "Joker" in cards:
        pointsOfFaces += strongestValue

    suitCounter = {"h": 0, "d": 0, "s": 0, "c": 0}
    for card in cards:
        if card != "Joker":
            suitCounter[card[1]] += 1
    maxCounter = 0
    for k in suitCounter:
        maxCounter = max(maxCounter, suitCounter[k])
    if "Joker" in cards:
        maxCounter += 1

    return pointsOfFaces*maxCounter



N = int(input())   # 2 o 3
cards = input().split()

playerPoints = [0 for i in range(N)]
playerCards = [[] for i in range(N)]

for i in range(5*N):
    playerCards[i % N].append(cards[i])

for i in range(N):
    playerPoints[i] = calculatePoints(playerCards[i])

if len(playerPoints) != len(set(playerPoints)):   # ci sono giocatori con stesso punteggio
    print("tie", max(playerPoints))
else:
    print(playerPoints.index(max(playerPoints))+1, max(playerPoints))
