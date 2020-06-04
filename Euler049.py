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


def primePerm():
    goodPrimes = set()
    primes = sieve(10000)
    for i in primes:
        if i > 1000:
            goodPrimes.add(i)
    for start in goodPrimes:
        for diff in range(start, max(goodPrimes)//2 + 1):
            second = start + diff
            third = start + 2*diff
            if second in goodPrimes and third in goodPrimes:
                if sorted(str(start)) == sorted(str(second)) == sorted(str(third)):
                    return int(str(start) + str(second) + str(third))


if __name__ == "__main__":
    print(primePerm())
