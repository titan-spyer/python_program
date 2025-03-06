# Defined the function calculator to do Arithmetic
def Arithmetic():
    # Taking user input while considering wrong input also
    try:
        a = int(input("Enter your first Number: "))
        b = int(input("Enter your Second Number: "))
    except ValueError:
        print("!!!Invalid input Enter a number!!!")
        Arithmetic()
    Operator = ('+', '-', '*', '/', '//', '%', '**')
    c = input("Enter a operator from (+, -, *, /, //, %, **): ")
    while c not in Operator:
        c = input("!!! Invalid Operator !!!\n Enter a valid Operator from: ")
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b
    elif c == '//':
        return a // b
    elif c == '%':
        return a % b
    else:
        return a ** b

# Define a function for calculator.
def calculator():
    # Write the loop statement to perform the calculation until user exit.
    while True:
        print("Welcome to VSSUT calculator")
        print("1. Arithmetic Operations (+, -, *, /, //, %, **)")
        print("2. Comparison Operations (>, <, ==, !=, >=, <=)")
        print("3. Logical Operations (and, or, not)")
        print("4. Membership Check (in, not in)")
        print("5. Identity Check (is, is not)")
        print("6. Exit")
        # Take the user choice to calculate.
        choice = int(input("Enter the number of your above choice: "))

        # Do the Arithmetic if user choose 1 as choice.
        if choice == 1:
            result = Arithmetic()
            print(result)
        elif choice == 6:
            print("Thankyou for using calculator.")
            break
        else:
            print("Invalid input Enter a number between '1' to '6'.")
calculator()