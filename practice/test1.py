for i in range(23, 87, 2):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, "is prime")