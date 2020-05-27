ONES = ["zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

TENS = ["", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"]


def calcSum():
    count = 0
    for i in range(1, 1001):
        count += len(sumNum(i))
    return count


def sumNum(n):
    if 0 <= n < 20:
        return ONES[n]
    elif 20 <= n < 100:
        return calcTens(n)
    elif 100 <= n < 1000:
        return calcHundreds(n)
    else:
        return ONES[n//1000] + "thousand"


def calcTens(n):
    if n % 10 == 0:
        if n == 10:
            return ONES[n]
        else:
            return TENS[n//10]
    else:
        if n < 20:
            return ONES[n]
        else:
            return TENS[n//10] + ONES[n % 10]


def calcHundreds(n):
    if n % 100 == 0:
        return "hundred" + ONES[n//100]
    else:
        return "hundred" + ONES[n//100] + "and" + calcTens(n % 100)


if __name__ == "__main__":
    print(calcSum())
