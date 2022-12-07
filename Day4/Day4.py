#Teil1
def calculateContainsFully(inputFile):
    file = open(inputFile, 'r')
    count = 0
    Lines = file.readlines()

    for line in Lines:
        lineValue = line.strip()
        positionComma = lineValue.index(",")
        elf1 = lineValue[:positionComma]
        elf2 = lineValue[positionComma+1:]

        elfSchedule1 = "/"
        elfSchedule2 = "/"

        elfListe = [elf1, elf2]

        for i in range(len(elfListe)):

            elf = elfListe[i]

            positionHyphen = elf.index("-")

            firstHalf = elf[:positionHyphen]
            secondHalf = elf[positionHyphen+1:]

            for k in range((int(secondHalf)-int(firstHalf))+1):
                if (i == 0):
                    elfSchedule1 += str(int(firstHalf)+k)+"/"
                else:
                    elfSchedule2 += str(int(firstHalf)+k)+"/"

        if (len(elfSchedule1) < len(elfSchedule2)):
                traverseString = elfSchedule1
                checkString = elfSchedule2
        else:
                traverseString = elfSchedule2
                checkString = elfSchedule1

        if traverseString in checkString:
                count += 1

    return count

#Teil2
def calculateContainsPartially(inputFile):
    file = open(inputFile, 'r')
    count = 0
    Lines = file.readlines()

    for line in Lines:
        lineValue = line.strip()
        positionComma = lineValue.index(",")
        elf1 = lineValue[:positionComma]
        elf2 = lineValue[positionComma+1:]

        elfSchedule1 = []
        elfSchedule2 = []

        elfListe = [elf1, elf2]

        for i in range(len(elfListe)):

            elf = elfListe[i]

            positionHyphen = elf.index("-")

            firstHalf = elf[:positionHyphen]
            secondHalf = elf[positionHyphen+1:]

            for k in range((int(secondHalf)-int(firstHalf))+1):
                if (i == 0):
                    elfSchedule1.append((int(firstHalf)+k))
                else:
                    elfSchedule2.append((int(firstHalf)+k))

        if (len(elfSchedule1) < len(elfSchedule2)):
            traverseList = elfSchedule1
            checkList = elfSchedule2
        else:
            traverseList = elfSchedule2
            checkList = elfSchedule1

        for number in traverseList:
            if number in checkList:
                count += 1
                break

    return count

#Teil1
anzahl1 = calculateContainsFully('input day5 day4')
print("Es gibt " + str(anzahl1) + " voll überlappende Gruppen.")

#Teil2
anzahl2 = calculateContainsPartially('input day5 day4')
print("Es gibt " + str(anzahl2) + " teilweise überlappende Gruppen.")

