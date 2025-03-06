import datetime

name = "School".replace("h", "H")
print(name)

def find_greatest(a, b, c):
    if a > b:
        if a > c:
            return "a is greater"
        else:
            return "c is greater"
    else:
        if b > c:
            return "b is greater"
        else:
            return "c is greater"

a = 10
b = 30
c = 20
print(find_greatest(a, b, c))

# Show the current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1

    return lcm

num1 = 12
num2 = 15
print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))