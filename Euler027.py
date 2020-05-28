def sieve(n):
    primes = [True for i in range(n+1)]
    primeList = set()
    num = 2
    while num * num <= n:
        if primes[num]:
            for j in range(num * num, n+1, num):
                primes[j] = False
        num += 1
    for i in range(2, n+1):
        if primes[i]:
            primeList.add(i)
    return primeList


def quadPrimes():
    opt = 0
    coordinate = [0, 0]
    primes = sieve(110000)

    for i in range(-999, 1000):
        for j in range(-999, 1000):
            n = 0
            while abs(n**2 + i*n + j) in primes:
                n += 1
            if n > opt:
                opt = n
                coordinate = [i, j]
    return coordinate[0] * coordinate[1]


if __name__ == "__main__":
    print(quadPrimes())
