def sumDivisors(n):
    divs = [1]
    for i in range(2, n):
        if n % i == 0:
            divs.append(i)
    return sum(divs)


def nonAbundantSum():
    lim = 28124
    abundants = set()
    for i in range(1, lim):
        if sumDivisors(i) > i:
            abundants.add(i)

    notAbundants = [True] * lim
    for i in abundants:
        for j in abundants:
            if i + j < lim:
                notAbundants[i+j] = False
            else:
                break
    return sum(i for (i, x) in enumerate(notAbundants) if x)


if __name__ == "__main__":
    print(nonAbundantSum())
