from itertools import permutations as perm


def checkProperty(n):
    listNums = [2, 3, 5, 7, 11, 13, 17]
    index = 1
    for i in listNums:
        num = n[index]*100 + n[index+1]*10 + n[index+2]
        if num % i != 0:
            return False
        index += 1
    return True


def divisibility():
    sumNums = 0
    for i in perm(range(10)):
        if checkProperty(i):
            sumNums += int(''.join(map(str, i)))
    return sumNums


if __name__ == "__main__":
    print(divisibility())
