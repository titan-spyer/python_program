def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
odd_num = []
prime_num = []
for i in range(23, 87):
    if i % 2 != 0:
        odd_num.append(i)
        if is_prime(i):
            prime_num.append(i)

print("The odd Nums are:", odd_num)
print("The prime among them are:",'\n', prime_num)
