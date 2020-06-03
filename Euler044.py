def pentagonal(n):
    pentagonalList = [0] * (n-1)
    for i in range(1, n):
        pentagonalList[i-1] = (int(i*((3*i)-1)/2))
    return pentagonalList


LIST = sorted(pentagonal(2500))


def checkMinimal(i, j):
    return (i+j) in LIST and (j-i) in LIST


def minimal():
    minDiff = 10000000
    for i in range(len(LIST)//3, len(LIST)-1):
        for j in range(i+1, len(LIST)):
            if checkMinimal(LIST[i], LIST[j]):
                if LIST[j]-LIST[i] < minDiff:
                    minDiff = LIST[j]-LIST[i]
                    return minDiff


if __name__ == "__main__":
    print(minimal())

