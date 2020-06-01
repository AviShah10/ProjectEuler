LIST = [1, 2, 5, 10, 20, 50, 100, 200]


def changeSum(maxNum, len):
    if maxNum == 0:
        return 1
    elif maxNum <= 0 or len == 0:
        return 0
    else:
        return changeSum(maxNum, len - 1) + changeSum(maxNum - LIST[len-1], len)


if __name__ == "__main__":
    print(changeSum(200, 8))
