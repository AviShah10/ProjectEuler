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


def primeSum():
    primes = sorted(list(sieve(1000000)))
    maxSum = []
    for i in range(5):
        tempPrimes = primes[i:]
        count = 0
        tempSum = 0
        for j in tempPrimes:
            count += 1
            tempSum += j
            if tempSum > 1000000:
                break
            if tempSum in primes:
                tempMaxSum = tempPrimes[:count]
                if len(tempMaxSum) > len(maxSum):
                    maxSum = tempMaxSum
    return sum(maxSum)


if __name__ == "__main__":
    print(primeSum())
