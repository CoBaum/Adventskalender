#Teil1:
def arrayifyCalories(inputFile):
    file = open(inputFile, 'r')
    Lines = file.readlines()

    sumCalories = 0
    array = []

    for line in Lines:
        if line.strip() == "":
            array.append(sumCalories)
            sumCalories = 0

        else:
            line_value = int(line.strip())
            sumCalories += line_value

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
