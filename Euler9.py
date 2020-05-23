def spec_pythag():
    for i in range(1, 1000):
        for j in range(1, i):
            for k in range(1, j+1):
                if j*j + k*k == i*i and i+j+k == 1000:
                    return i*j*k


if __name__ == "__main__":
    print(spec_pythag())