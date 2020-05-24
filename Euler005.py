def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


if __name__ == "__main__":
    n = 1
    for i in range(1, 21):
        n = lcm(n, i)
    print(n)

