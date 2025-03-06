# Check Wheather a number is fibonacci or not
num = int(input("Enter a number: "))
if num <= 2:
    print("Fibonacci Number")
else:
    k = 1
    l = 0
    for i in range(num + 1):
        if k > num:
            print("Not a fibonacci")
            break
        elif k == num:
            print("Fibonacci number")
            break
        temp = l + k
        l = k
        k = temp