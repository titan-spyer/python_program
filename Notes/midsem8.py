try:
    a = int(input("Enter A number to find it's binnary value: "))
    print(bin(a))
except ValueError:
    print("Not a number")