# oddlist = []
# primelist = []
# def is_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# for i in range(23, 87):
#     if i % 2 != 0:
#         oddlist.append(i)
#         if is_prime(i):
#             primelist.append(i)
        
# print(oddlist)
# print(primelist)
for i in range(23, 87, 2):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=', ')