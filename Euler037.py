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


def isTruncate(n):
    num = n
    while num > 0:
        if num not in PRIMES:
            return False
        num //= 10
    string = str(n)
    while len(string) > 0:
        if int(string) not in PRIMES:
            return False
        string = string[1:]
    return True


def numTruncate():
    sumNums = 0
    for i in PRIMES:
        if isTruncate(i) and len(str(i)) > 1:
            sumNums += i
    return sumNums


if __name__ == "__main__":
    print(numTruncate())
