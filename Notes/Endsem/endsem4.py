firstnum = int(input("Enter first Number: "))
secondnum = int(input("Enter Second Number: "))
lista = []
# Program to find GCD
for i in range(1, firstnum):
    if firstnum % i == 0:
        if secondnum % i == 0:
            lista.append(i)
print(f"GCD is: {max(lista)}")
# program to find LCM
lcm = (firstnum * secondnum) // max(lista)
print(f"LCM is: {lcm}")