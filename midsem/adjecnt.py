lista = [10, 20, 30, 50, 60]
for i in range(0, len(lista) - 1, 2):
    a = lista[i]
    b= lista[i + 1]
    lista[i] = b
    lista[i + 1] = a
print(lista)