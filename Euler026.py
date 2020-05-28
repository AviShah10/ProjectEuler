def repeating():
    num = 1
    maxCount = 1
    for i in range(3, 1000, 2):
        if i % 5 == 0:
            continue
        count = 1
        while (10**count) % i != 1:
            count += 1
        if count > maxCount:
            num = i
            maxCount = count
    return num


if __name__ == "__main__":
    print(repeating())
