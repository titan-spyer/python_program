# # To find the factorial using recursion
def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)
a = 5
print(factorial(a))

# a = int(input("Enter a number to print factorial: "))

# Factorial using itreation.
# a = int(input("Enter a number: "))
# # a = 5
# i = 1
# fact = 1
# while i <= a:
#     if i == 1:
#         fact *= i
#     else:
#         fact = i * fact
#     i += 1
# print(fact)