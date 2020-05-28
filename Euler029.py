def distinctPowers(n):
    nums = set()
    for i in range(2, n+1):
        for j in range(2, n+1):
            nums.add(i**j)
    return len(nums)


if __name__ == "__main__":
    print(distinctPowers(100))
