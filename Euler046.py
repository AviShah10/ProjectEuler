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


PRIMES = sieve(100000)


def check(n):
    temp = 0
    while True:
        temp += 1
        checkPrime = n - 2 * temp**2
        if checkPrime < 0:
            return False
        elif checkPrime in PRIMES:
            return True


def goldbach():
    ODDS = set()
    for i in range(3, 100000, 2):
        ODDS.add(i)
    ODDCOMPS = list(ODDS ^ PRIMES)
    ODDCOMPS.pop(0)
    ODDCOMPS = set(ODDCOMPS)
    for i in ODDCOMPS:
        if not check(i):
            return i


if __name__ == "__main__":
    print(goldbach())
