def pandigital():
    sumsSet = set()
    for i in range(2000):
        for j in range(100):
            if isPandigital(i, j):
                sumsSet.add((i*j))
    return sum(sumsSet)


def isPandigital(i, j):
    n = str(i) + str(j) + str(i*j)
    if len(n) != 9:
        return False
    for i in range(1, 10):
        if str(i) not in n:
            return False
    return True


if __name__ == "__main__":
    print(pandigital())
