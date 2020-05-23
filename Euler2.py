count = 0
prev = 1
curr = 2
temp = 0
while curr < 4000000:
    if curr % 2 == 0:
        count += curr
    temp = curr
    curr = temp + prev
    prev = temp
print(count)
