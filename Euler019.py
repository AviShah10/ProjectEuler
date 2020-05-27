import datetime


def calcTime():
    count = 0
    for i in range(1901, 2001):
        for j in range(1, 13):
            if datetime.date(i, j, 1).weekday() == 6:
                count += 1
    return count


if __name__ == "__main__":
    print(calcTime())
