import itertools


def permute():
    return "".join(list(itertools.permutations("0123456789"))[999999])


if __name__ == "__main__":
    print(permute())
