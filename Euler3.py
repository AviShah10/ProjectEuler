def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


num = 600851475143
for x in range(2, num+1):
    if is_prime(x) and num % x == 0:
        print(x)
