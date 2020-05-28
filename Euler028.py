def diagonalSum(n):
    total = 1
    for i in range(3, n + 1, 2):
        total += i ** 2
        total += i ** 2 - (i - 1)
        total += i ** 2 - 2 * (i - 1)
        total += i ** 2 - 3 * (i - 1)
    return total


if __name__ == "__main__":
    print(diagonalSum(1001))
