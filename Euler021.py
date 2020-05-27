def amicableSum():
    amicableSet = set()
    for i in range(2, 10001):
        if i == sumDivisors(sumDivisors(i)) and i != sumDivisors(i):
            amicableSet.add(i)
            amicableSet.add(sumDivisors(i))
    return sum(amicableSet)


def sumDivisors(n):
    divs = [1]
    for i in range(2, n):
        if n % i == 0:
            divs.append(i)
    return sum(divs)


if __name__ == "__main__":
    print(amicableSum())
