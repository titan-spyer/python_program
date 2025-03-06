# # Fibonacci using recursion.
def fib(n):
    if n <= 1:
        return n
    return fib(n - 2) +  fib(n - 1)
# num = int(input("Enter a number: "))
num = 5
print(fib(num + 1))
# # Find the n th fibonacci number using iteration.
# def fib(n):
#     a = 0
#     b = 1
#     for i in range(2, n + 1):
#         c = a + b
#         a = b
#         b = c
#     return b
# num = int(input("Enter a number: "))
# print(fib(num))
# Find the fibonacci series upto n terms.
# def fib(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         print(a, end = " ")
#         c = a + b
#         a = b
#         b = c
# num = int(input("Enter a number: "))
# fib(num)
# # Find the fibonacci series upto n terms using recursion.
# def fib(n, a = 0, b = 1):
#     if n == 0:
#         return n
#     # print(a, end = " ")
#     return n + fib(n - 1, b, a + b)
# num = int(input("Enter a number: "))
# print(fib(num))