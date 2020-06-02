def champernowne():
    num = ""
    for i in range(1, 500000):
        num += str(i)
    return int(num[0]) * int(num[9]) * int(num[99]) * int(num[999]) * int(num[9999]) * int(num[99999]) * int(num[999999])


if __name__ == "__main__":
    print(champernowne())
