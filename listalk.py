lista1 = [23, 54, 33, -6, -8]
lista2 = [23, 66, 77, 8, 9, -4]
lista3 = [2, -6, 8, 33, 89, -33]

minimumok = []
def minKeres(lista):
    minimum = lista[0]
    for i in lista:
        if i < minimum:
            minimum = i
    print(minimum)
    return minimum
for i in lista3:
    minimumok.append(minKeres(i))
