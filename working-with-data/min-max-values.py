import math

def findMax(p):
    print(f"found: {p}, type:{type(p)}")
    maximum = max(p)
    print(f"max value: {maximum}")
    return maximum


if __name__ == "__main__":
    numeric = [1.2, 3.1, 4.6, 7.2, 0.1]

    # strings = ["one", "two", "three", "four", "five"]
    #
    # print("Starting: ")
    # print(f"all numeric values: {numeric} ")
    # print(f"all string values: {strings} ")
    #
    # print(f"Minimum numeric value: {min(numeric)}")
    # print(f"Minimum string value: {min(strings)}")
    #
    # print(f"Maximum numeric value: {max(numeric)}")
    # print(f"Maximum string value: {max(strings)}")
    #
    # print(f"Maximum string value (by lenth): {max(strings, key=len)}")
    # print(f"Minimum string value (by lenth): {min(strings, key=len)}")

    # numericArrays = [[1.2, 3.1, 4.3, 5], [2.3, 4.5, 5], [0.6, 1.3, 5]]
    numericArrays = [[1, 3, 4, 5], [2, 4, 5], [6, 1, 5]]
    arrayOfMax = [max(x) for x in numericArrays]
    print(f"T: {sum(arrayOfMax)/len(arrayOfMax):.2f}")



    print("Done.")

