#Teil1
crates1 = {1: ['C', 'Q', 'B'], 2: ['Z', 'W', 'Q', 'R'], 3: ['V', 'L', 'R', 'M', 'B'], 4: ['W', 'T', 'V', 'H', 'Z', 'C'],
          5: ['G', 'V', 'N', 'B', 'H', 'Z', 'D'], 6: ['Q', 'V', 'F', 'J', 'C', 'P', 'N', 'H'], 7: ['S', 'Z', 'W', 'R', 'T', 'G', 'D'],
          8: ['P', 'Z', 'W', 'B', 'N', 'M', 'G', 'C'], 9: ['P', 'F', 'Q', 'W', 'M', 'B', 'J', 'N']}

#Teil2
crates2 = {1: ['C', 'Q', 'B'], 2: ['Z', 'W', 'Q', 'R'], 3: ['V', 'L', 'R', 'M', 'B'], 4: ['W', 'T', 'V', 'H', 'Z', 'C'],
           5: ['G', 'V', 'N', 'B', 'H', 'Z', 'D'], 6: ['Q', 'V', 'F', 'J', 'C', 'P', 'N', 'H'], 7: ['S', 'Z', 'W', 'R', 'T', 'G', 'D'],
           8: ['P', 'Z', 'W', 'B', 'N', 'M', 'G', 'C'], 9: ['P', 'F', 'Q', 'W', 'M', 'B', 'J', 'N']}

#Teil1
def crateranking1(inputfile):
    file = open(inputfile, 'r')
    finalRanking = ""
    lines = file.readlines()

    for line in lines[10:]:
        lineValue = line.strip()
        numbers = ""

        for character in lineValue:
            if character.isdigit():
                numbers += character

        if len(numbers) == 3:
            numberOfCrates = numbers[0]
            origin = numbers[1]
            destination = numbers[2]
        else:
            numberOfCrates = numbers[0:2]
            origin = numbers[2]
            destination = numbers[3]


        for i in range(int(numberOfCrates)):
            crates1[int(destination)].insert(0, crates1[int(origin)][0])
            crates1[int(origin)].pop(0)

    for k in range(9):
        finalRanking += crates1[k+1][0]


    return finalRanking



#Teil2
def crateranking2(inputfile):
    file = open(inputfile, 'r')
    finalRanking = ""
    Lines = file.readlines()

    for line in Lines[10:]:
        lineValue = line.strip()
        numbers = ""

        for character in lineValue:
            if character.isdigit():
                numbers += character

        if len(numbers) == 3:
            numberOfCrates = numbers[0]
            origin = numbers[1]
            destination = numbers[2]
        else:
            numberOfCrates = numbers[0:2]
            origin = numbers[2]
            destination = numbers[3]
        l = 1
        for i in range(int(numberOfCrates)):
            crates2[int(destination)].insert(0, crates2[int(origin)][int(numberOfCrates) - l])
            crates2[int(origin)].pop(int(numberOfCrates) - l)
            l += 1


    for k in range(9):
        finalRanking += crates2[k+1][0]


    return finalRanking





#Teil1
result1 = crateranking1('input day5')
print("Der Code mit dem alten Modell lautet: " + result1 + ".")

#Teil2
result2 = crateranking2('input day5')
print("Der Code mit dem neuen Modell lautet: " + result2 + ".")

