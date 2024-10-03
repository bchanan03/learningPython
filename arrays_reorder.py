def sumAll(myArray, indexLeft, indexRight):
    sum = 0
    for i in range(indexLeft, min(indexRight, len(myArray))):
        sum += myArray[i]
    return sum


def array_reoder(myArray):
    indexCounter = 0
    incrementalCounter = 1
    size = len(myArray)
    resultArray = []

    while indexCounter < size:
        resultArray.append(sumAll(myArray, indexCounter, indexCounter + incrementalCounter))
        indexCounter += incrementalCounter
        incrementalCounter = incrementalCounter + 1

    return resultArray


if __name__ == "__main__":
    myArray = [1, 5, 3, 4, 2, 4, 1, 5, 3, 4, 2, 4]
    resultArray = array_reoder(myArray)
    print(myArray)
    print("Result:")
    print(resultArray)
