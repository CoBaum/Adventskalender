#Teil1
def solveSignalPacket(inputfile):
    file = open(inputfile, 'r')
    line = file.readline()

    for i in range(len(line)):
        currentCharacters = line[i:i+4]
        count = 0
        for character in currentCharacters:
            if currentCharacters.count(character) > 1:
                break
            else:
                count += 1
                if count == 4:
                    return i+4
                else:
                    continue

#Teil2
def solveSignalMessage(inputfile):
    file = open(inputfile, 'r')
    line = file.readline()

    for i in range(len(line)):
        currentCharacters = line[i:i+14]
        count = 0
        for character in currentCharacters:
            if currentCharacters.count(character) > 1:
                break
            else:
                count += 1
                if count == 14:
                    return i+14
                else:
                    continue

#Teil1
numberOfCharactersPacket = solveSignalPacket('input day6')
print("Der Start-Of-Packet Marker wird lokalisiert, nachdem " + str(numberOfCharactersPacket) + " Zeichen analysiert wurden.")

#Teil2
numberOfCharactersMessage = solveSignalMessage('input day6')
print("Der Start-Of-Packet Marker wird lokalisiert, nachdem " + str(numberOfCharactersMessage) + " Zeichen analysiert wurden.")