def intTriangles():
    listNums = [0] * 1001
    for a in range(1, 1000):
        for b in range(1, 500):
            c = (a**2 + b**2)**(1/2)
            perimeter = a + b + int(c)
            if c == int(c) and perimeter <= 1000:
                listNums[perimeter] = listNums[perimeter] + 1
    return listNums.index(max(listNums))


if __name__ == "__main__":
    print(intTriangles())
