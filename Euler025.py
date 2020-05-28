def fib():
    f = [1] * 1000000
    index = 2
    temp = 2
    while len(str(temp)) < 1000:
        f[index] = f[index-1] + f[index-2]
        temp = f[index]
        index += 1
    return index


if __name__ == "__main__":
    print(fib())
