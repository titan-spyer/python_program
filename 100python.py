# Write a program to find all numbers divisible by 7 but not a multiple of 5, between 2000 and 3200 (both included). Print the numbers in a comma-separated sequence.
def divby7not5():
    for i in range(2000, 3200):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=', ')
# print()
# divby7not5()
# Write a program to compute the factorial of a given number.
def factorial():
    a = 5
    fact = 1
    for i in range(1, a + 1):
        fact *= i
    print(fact)
# factorial()
# Generate a dictionary where keys are numbers between 1 and n (inclusive), and values are the square of the keys.
def dictionar1():
    mathg = dict()
    n = int(input("Enter a number: "))
    for i in range(1, n+1):
        mathg[i] = i ** 2
    print(mathg)
# dictionar1()
# Accept a sequence of comma-separated numbers and generate a list and a tuple.
def listandtuple():
    list1 = list(map(int, input("Enter comma separated value to make a list: ").split()))
    tuple1 = tuple(map(int, input("Enter comma separated value: ").split()))
    print(tuple1)
    print(list1)
# listandtuple()
# Define a class with two methods: getString to get a string from console input and printString to print the string in uppercase.
def classme1():
    print("Out of syllabus")
# classme1()
# Calculate the value of Q = Square root of [(2 * C * D)/H] where C=50, H=30, and D is a comma-separated input.
from math import sqrt
def calccoma():
    c = 50
    h = 30
    nums = list(map(int, input("Enter comma separated input: ").split(',')))
    answers = list()
    for d in nums:
        answers.append(int(sqrt((2 * c * d)/h)))
    print(answers)
# calccoma()
# Generate a 2D array where the element at the i-th row and j-th column is i*j.
def twodarray():
    num = int(input("Enter the number: "))
    list1= list()
    for i in range(num+1):
        list1.append(i)
        list1[i] = list()
        for j in range(i):
            list1[i].append(i*j)
    print(list1)
# twodarray()
# Accept a comma-separated sequence of words and print them in sorted order.
def sortwords():
    words = input("Enter comma separated words: ").split(',')
    words.sort()
    print(words)
# sortwords()
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
def sequense1():
    lines = list()
    while True:
        line = input()
        if line:
            lines.append(line.upper())
        else:
            break
    for line in lines:
        print(line)
# sequense1()
# Accept a sequence of whitespace-separated words, remove duplicates, and print them in alphanumeric order
def sequense2():
    words = input("Enter whitespace separated words: ").split(' ')
    words = list(set(words))
    words.sort()
    print(words)
# sequense2()
# Accept a sequence of comma-separated 4-digit binary numbers and print those divisible by 5.
def sequense3():
    nums = list(map(int, input("Enter comma separated 4-digit binary numbers: ").split(',')))
    for num in nums:
        if num % 5 == 0:
            print(num, end=', ')
# sequense3()
# Find all numbers between 1000 and 3000 where each digit is even.
def allnumber():
    for i in range(1000, 3000):
        num = str(i)
        if (int(num[0]) % 2 == 0) and (int(num[1]) % 2 == 0) and (int(num[2]) % 2 == 0) and (int(num[3]) % 2 == 0):
            print(i)
# allnumber()
# Calculate the number of letters and digits in a given sentence.
def digalpha():
    dict1 = {'Letters': 0, 'Digit': 0}
    word = input("Enter name: ")
    for i in word:
        if i.isalpha():
            dict1["Letters"] += 1
        if i.isdigit():
            dict1["Digit"] += 1
    print(dict1)
# digalpha()
# Calculate the number of uppercase and lowercase letters in a given sentence.
def calupplow():
    word = input("Enter word: ")
    dict1 = {'uppercase': 0, 'Lowercase': 0}
    for i in word:
        if i.isupper():
            dict1["uppercase"] += 1
        elif i.islower():
            dict1["Lowercase"] += 1
    print(dict1)
# calupplow()
# Compute the value of a + aa + aaa + aaaa where a is a given digit.
def compvalue():
    a = input("Enter a number: ")
    n1 = int("%s" % a)
    n2 = int("%s%s" % (a, a))
    n3 = int("%s%s%s" % (a, a, a))
    n4 = int("%s%s%s%s" % (a, a, a, a))
    print(n1+n2+n3+n4)
