def pandigital():
    listNums = set()
    for i in range(1, 10000):
        string = ""
        for j in range(1, 10):
            string += str(i*j)
            if "".join(sorted(string)) == "123456789":
                listNums.add(int(string))
    return max(listNums)


if __name__ == "__main__":
    print(pandigital())