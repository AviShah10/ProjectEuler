def primeFactors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(n**(1/2)+1), 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return factors


def checkDistinct(n):
    for i in range(n, n+4):
        if len(primeFactors(i)) != 4:
            return False
    return True


def distinctRunner():
    for i in range(1000, 1000000):
        if checkDistinct(i):
            return i


if __name__ == "__main__":
    print(distinctRunner())
