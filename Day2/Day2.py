#Teil1
scoresShape = {"X": 1, "Y": 2, "Z": 3}
scoresOutcome = {"loss": 0, "win": 6, "draw": 3}
#Teil2
outcomeDecider = {"X": "loss", "Y": "draw", "Z": "win"}

#Teil1
def calculateScore1(inputFile):
    file = open(inputFile, 'r')
    totalScore = 0
    Lines = file.readlines()

    for line in Lines:
        line_value = line.strip()
        myChoice = line_value[2]
        opChoice = line_value[0]

        if ((myChoice == "X" and opChoice == "A") or (myChoice == "Y" and opChoice == "B") or (myChoice == "Z" and opChoice == "C")):
            outcome = "draw"

        elif ((myChoice == "X" and opChoice == "B") or (myChoice == "Y" and opChoice == "C") or (myChoice == "Z" and opChoice == "A")):
            outcome = "loss"

        else:
            outcome = "win"

        totalScore += scoresShape[myChoice] + scoresOutcome[outcome]

    return totalScore

#Teil2
def calculateScore2(inputFile):
    file = open(inputFile, 'r')
    totalScore = 0
    Lines = file.readlines()

    for line in Lines:
        line_value = line.strip()
        opChoice = line_value[0]
        outcomeKey = line_value[2]

        if ((outcomeKey == "X" and opChoice == "B") or (outcomeKey == "Y" and opChoice == "A") or (outcomeKey == "Z" and opChoice == "C")):
            myChoice = "X"

        elif ((outcomeKey == "X" and opChoice == "C") or (outcomeKey == "Y" and opChoice == "B") or (outcomeKey == "Z" and opChoice == "A")):
            myChoice = "Y"

        else:
            myChoice = "Z"

        thisOutcome = outcomeDecider[outcomeKey]
        totalScore += scoresShape[myChoice] + scoresOutcome[thisOutcome]


    return totalScore

#Teil1
score1 = calculateScore1('input day5 day2')
print("\n" + "Nach dem alten Guide komme ich auf eine Punktzahl von insgesamt: " + str(score1) + ".")

#Teil2
score2 = calculateScore2('input day5 day2')
print("\n" + "Nach dem neuen Guide komme ich auf eine Punktzahl von insgesamt: " + str(score2) + ".")
