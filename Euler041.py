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


PRIMES = sieve(10000000)


def pandigitalPrime():
    nums = "123456789"
    maxNum = 0
    for i in PRIMES:
        if "".join(sorted(str(i))) == nums[0:len(str(i))]:
            if i > maxNum:
                maxNum = i
    return maxNum


if __name__ == "__main__":
    print(pandigitalPrime())
