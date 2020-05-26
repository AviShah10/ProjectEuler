from math import factorial


def binomial(n, k):
    return int(factorial(n)/(factorial(k) * (factorial(n-k))))


def routes():
    return str(binomial(40, 20))


if __name__ == "__main__":
    print(routes())
