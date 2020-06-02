def isPalin(n):
    return str(n) == str(n)[len(str(n))::-1]


def doublePalins():
    sumNums = 0
    for i in range(1, 1000000):
        if isPalin(i) and isPalin(bin(i).replace("0b", "")):
            sumNums += i
    return sumNums


if __name__ == "__main__":
    print(doublePalins())
