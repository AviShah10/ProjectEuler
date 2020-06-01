def sumPowers():
    total = 0
    sumTotal = 0
    for i in range(2, 1000000):
        for j in str(i):
            total += int(j)**5
        if i == total:
            sumTotal += total
        total = 0
    return sumTotal


if __name__ == "__main__":
    print(sumPowers())
