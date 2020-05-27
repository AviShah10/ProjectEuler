def powerFcn(n, p):
    return sum([int(i) for i in str(pow(n, p))])


if __name__ == "__main__":
    print(powerFcn(2, 1000))