a = 24140
b = 16762
lista = []
for i in range(1, b):
    if b % i == 0:
        if a % i == 0:
            lista.append(i)
        
lista.sort()
print(max(lista))
