from math import factorial


def calcSum(n):
    return sum([int(i) for i in str(factorial(n))])


if __name__ == "__main__":
    print(calcSum(100))
