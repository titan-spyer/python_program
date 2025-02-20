sentence1 = "I Love VSSUT"
lent = 0
for char in sentence1:
    if char:
        lent += 1

print(lent)
lista = []
point = 0
char = 0
while char < lent:
    if sentence1[char] == ' ':
        lista.append(sentence1[point:char])
        point = char
    char += 1
lista.append(sentence1[point:])
print(lista)

# lent = len(sentence1)
# print(lent)

# lista = sentence1.split()
# print(lista)
vcount = 0
for char in sentence1:
    if char == 'v' or char == 'V':
        vcount += 1

print(vcount)