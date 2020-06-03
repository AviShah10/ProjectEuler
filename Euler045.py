def pentagonal(n):
    pentagonalList = set()
    for i in range(1, n):
        pentagonalList.add(int(i*((3*i)-1)/2))
    return pentagonalList


def triangular(n):
    triangularList = set()
    for i in range(1, n):
        triangularList.add(int(i*(i+1)/2))
    return triangularList


def hexagonal(n):
    hexagonalList = set()
    for i in range(1, n):
        hexagonalList.add(int(i*(2*i-1)))
    return hexagonalList


def intersection():
    triList = triangular(100000)
    pentList = pentagonal(100000)
    hexList = hexagonal(100000)
    intList = list(triList & pentList & hexList)
    return intList[-1]


if __name__ == "__main__":
    print(intersection())