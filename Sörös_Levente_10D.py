lista1 = []


def vegez(szam):
    if szam == -1:
        return True
    else:
        return False


def legnagyob(lista):
    for i in lista:
        legnagyobb = lista[0]
        if i > legnagyobb:
            legnagyobb = i
    return legnagyobb







def novekvo(lista):
    for i in range(len(lista) -1):
        for j in range(i+1, len(lista)):
            if lista[j] < lista[i]:
                lista[j],lista[i] =lista[i],lista[j]
    return lista




while True:
    szam = int(input("Adja meg a számokat"))
    if vegez(szam):
        break
    else:
        lista1.append(szam)

print("az eredeti lista:", lista1)
print("a rendezett lista:", novekvo(lista1))
print("A legnagyobb szám:",legnagyob(lista1))
