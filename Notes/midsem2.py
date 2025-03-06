sum = 0
count = 0
i = 0
while True:
    if count == 20:
        break
    elif i % 2 != 0:
        sum += i
        count += 1
    i += 1

print(sum)