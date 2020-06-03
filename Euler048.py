def selfPowers():
    sumNums = 0
    for i in range(1, 1001):
        sumNums += i**i
    return str(sumNums)[-10:]


if __name__ == "__main__":
    print(selfPowers())