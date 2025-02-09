def greatcd(a, b):
    while b:
        temp = b
        b = a % b
        a = temp

    return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The GCD of {num1} and {num2} is {greatcd(num1, num2)}")