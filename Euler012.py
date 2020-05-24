def numDivisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n%i == 0:
            if n/i == i:
                count += 1
            else:
                count += 2
    return count


def divisors(n):
    count = 0
    triNum = 1
    while count < n:
        count = numDivisors((triNum * (triNum+1) / 2))
        triNum += 1
    return int((triNum-1) * triNum / 2)


if __name__ == "__main__":
    print(divisors(500))
