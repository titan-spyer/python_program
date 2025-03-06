lista = list(map(int, input("Enter  number Separeted by space. ").split()))
i = 0
while i < (len(lista) - 1):
    temp = lista[i]
    lista[i] = lista[i + 1]
    lista[i + 1] = temp
    i += 2
print(lista)