#Teil1:
def arrayifyCalories(inputFile):
    file = open(inputFile, 'r')
    lines = file.readlines()

    sumCalories = 0
    array = []

    for line in lines:
        if line.strip() == "":
            array.append(sumCalories)
            sumCalories = 0

        else:
            lineValue = int(line.strip())
            sumCalories += lineValue

    return array

#Teil2:
def sumOfHighestThree(array):
    array.sort(reverse=True)
    i = 0
    sumOfCalories = 0

    for i in range(3):
        sumOfCalories += array[i]

    return sumOfCalories

#Teil1:
datalist = arrayifyCalories('input day5 day1')
print(datalist)
maximum = max(datalist)
index = datalist.index(maximum)
print("\n" + "Der " + (str(index+1)) + "te Elf ist die richtige Wahl. Er trägt " + str(maximum) + " Kalorien mit sich.")

#Teil2:
summe = sumOfHighestThree(datalist)
print("\n" + "Die drei \"reichsten\" Elfen stemmen insgesamt " + str(summe) + " Kalorien.")
