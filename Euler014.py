LIST = [0] * 1000001


def nextStep(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return int(n*3) + 1


def solve(n):
    steps = 0
    tempNum = n
    while tempNum != 1:
        tempNum = nextStep(tempNum)
        steps += 1
        if tempNum < 1000000:
            if LIST[tempNum] != 0:
                steps += LIST[tempNum]
                break
    return steps


def collatz():
    num = 0
    maxSteps = 0
    for i in range(2, 1000001):
        steps = solve(i)
        LIST[i] = steps
        if steps > maxSteps:
            maxSteps = steps
            num = i
    return num


if __name__ == "__main__":
    print(collatz())
