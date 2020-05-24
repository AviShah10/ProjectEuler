def sieve(x):
    primes = [True for i in range(x+1)]
    n = 2
    while n * n <= x:
        if primes[n]:
            for j in range(n * n, x+1, n):
                primes[j] = False
        n += 1
    sum = 0
    for i in range(2, x+1):
        if primes[i]:
            sum += i
    return sum


if __name__ == "__main__":
    print(sieve(2000000))

