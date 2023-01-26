lista = [10, -2, 1, 25, 22, 30, 60, -99, -1252, 3000, 2123, 16, 12]
for i in range(len(lista) - 1):
    for j in range(i + 1, len(lista)):
        print(i, j, lista, end='')
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
        print('!', lista[i], lista[j])
        print('  ', lista)
    else:
        print("mehet a zöld")
print("a legnagyobb szám:", lista[12])

for i in range(len(lista) - 1):
    for j in range(i + 1, len(lista)):
        print(i, j, lista, end='')
        if lista[i] < lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
        print('!', lista[i], lista[j])
        print('  ', lista)
    else:
        print("mehet a piros")

print("A legkisebb szám:", lista[12])
