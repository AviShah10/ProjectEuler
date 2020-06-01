from math import factorial


def sumFactorials():
    sumNums = 0
    tempSum = 0
    for i in range(3, 50000):
        for j in str(i):
            tempSum += factorial(int(j))
        if tempSum == i:
            sumNums += tempSum
        tempSum = 0
    return sumNums


if __name__ == "__main__":
    print(sumFactorials())
