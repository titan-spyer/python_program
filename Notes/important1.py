# Cheak whather a number is armonstrong or Not.
a = int(input("Enter a number to check wheather it's a armonstrong or not: "))
lista = []
# Do the operation to separate number.
while a != 0:
    i = a % 10
    a = a // 10
    lista.append(i)
sum = 0
# Reverse the list.
lista.reverse()
# Find it's addition and multification value.
for i in range(len(lista)):
    sum += (lista[i] ** len(lista))
# Check the o/p value by it's i/p value.
if sum == a:
    print("The number is Armonstrong.")
else:
    print("The number is not Armonstrong")
