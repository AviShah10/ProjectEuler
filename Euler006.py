def sum_of_squares(n):
    return n*(n + 1)*(2*n + 1) / 6


def sum_arith(n):
    return (n+1)*n/2


if __name__ == "__main__":
    print(sum_arith(100) * sum_arith(100) - sum_of_squares(100))