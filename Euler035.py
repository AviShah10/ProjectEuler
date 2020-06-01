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


PRIMES = sieve(1000000)


def isCircular(n):
    num = str(n)
    for i in num:
        if int(num) not in PRIMES:
            return False
        num = num[-1] + num[0:-1]
    return True


def circularPrimes():
    count = 0
    for i in PRIMES:
        if isCircular(i):
            count += 1
    return count


if __name__ == "__main__":
    print(circularPrimes())
