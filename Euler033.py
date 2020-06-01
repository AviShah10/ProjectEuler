def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def fractions():
    numerator = 1
    denominator = 1
    for i in range(10, 100):
        for j in range(i+1, 100):
            nTens = i // 10
            dTens = j // 10
            nOnes = i % 10
            dOnes = j % 10
            if nTens == dOnes and (j*nOnes == i*dTens):
                numerator *= i
                denominator *= j
                # print(str(i) + "/" + str(j))
            if nOnes == dTens and (j*nTens == i*dOnes):
                numerator *= i
                denominator *= j
                # print(str(i) + "/" + str(j))
    return denominator // gcd(numerator, denominator)


if __name__ == "__main__":
    print(fractions())

