#Teil1

scoresPriorities = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

#Teil1
def calculatePriorityScore(inputFile):
    file = open(inputFile, 'r')
    lines = file.readlines()
    totalPriorityScore = 0

    for line in lines:
        lineValue = line.strip()


        halfLength = len(lineValue)//2
        firstCompartment = lineValue[:halfLength]
        secondCompartment = lineValue[halfLength:]

        for i in range(len(firstCompartment)):
            currentCharacter = firstCompartment[i]
            if secondCompartment.find(currentCharacter) != -1:
                priority = currentCharacter
                if priority.isupper():
                    totalPriorityScore += scoresPriorities[priority.lower()] + 26
                    break
                else:
                    totalPriorityScore += scoresPriorities[priority]
                    break

    return totalPriorityScore

#Teil2
def calculatePriorityScoreElfGroup(inputFile):
    file = open(inputFile, 'r')
    Lines = file.readlines()
    totalPriorityScoreElfGroup = 0


    for i in range(len(Lines)//3):
        lineArray = []
        for j in range(3):
            currentLine = Lines[0].strip()
            lineArray.append(currentLine)
            Lines.pop(0)
        lineArray.sort(key=len)
        for k in range(len(lineArray[0])):
            currentCharacter = lineArray[0][k]
            if (lineArray[1].find(currentCharacter) != -1) & (lineArray[2].find(currentCharacter) != -1):
                priority = currentCharacter
                if priority.isupper():
                    totalPriorityScoreElfGroup += scoresPriorities[priority.lower()] + 26
                    break
                else:
                    totalPriorityScoreElfGroup += scoresPriorities[priority]
                    break
    return totalPriorityScoreElfGroup


#Teil1
score1 = calculatePriorityScore('input day5 day3')
print("Die Gesamtpriorität beträgt: " + str(score1) + ".")

#Teil2
score2 = calculatePriorityScoreElfGroup('input day5 day3')
print("Die Gesamtgruppenpriorität beträgt: " + str(score2) + ".")