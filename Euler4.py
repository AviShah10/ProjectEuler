def is_palin():
    num = 0
    for i in range(1, 1000):
        for j in range(1, 1000):
            if str(i*j) == str(i*j)[len(str(i*j))::-1] and (i*j) > num:
                num = i*j
    return num


if __name__ == "__main__":
    print(is_palin())
