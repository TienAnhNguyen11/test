def adjacentElementsProduct(inputArray):
    lenth = len(inputArray)
    a = []

    for i in range(lenth - 1):
        x = inputArray[i]
        y = inputArray[i + 1]
        a.append(x * y)

    return max(a)