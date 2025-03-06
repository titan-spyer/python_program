# String reversed.
# college = "IIT Bombay"
# def reverse(s):
#     return s[::-1]
# Pailndrome check.
# def palindrome(s):
#     if s == "":
#         return True
#     return s[0] == s[-1] and palindrome(s[1:-1])
# print(palindrome("madam"))
# def palindromes(s):
#     return s[::-1] == s
# print(palindromes("madam"))
# Armonstrong number using Itration.
# def armonstrong(x):
#     length = len(str(x))
#     sum = 0
#     temp = x
#     while temp > 0:   
#         digit = temp % 10
#         sum += digit ** length
#         temp //= 10
#     return sum
# print(armonstrong(153))
# Armonstrong number using Recursion.
# def armonstrong(x, length):
#     if x == 0:
#         return 0
#     return (x % 10) ** length + armonstrong(x // 10, length)
# print(armonstrong(153, 3))
