def sieve():
    primes = [True for i in range(150001)]
    n = 2
    while n * n <= 150000:
        if primes[n]:
            for j in range(n * n, 150001, n):
                primes[j] = False
        n += 1
    count = 0
    for i in range(2, 150001):
        if primes[i]:
            count += 1
            if count == 10001:
                return i


if __name__ == "__main__":
    print(sieve())
