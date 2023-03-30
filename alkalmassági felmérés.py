def rendezo(lista):
    for i in (0, len(lista) - 1):
        for j in lista(1, len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


lista = []
with open("egysoros.txt", "r", encoding="utf-8") as file:
    for sor in file:
        lista = sor.split(";")

print(lista)

for i in lista:
    lista[0] = int(lista[0])

rendezo(lista)
print(lista)




with open("egysoros eredmény.txt.txt", "w", encoding="utf-8") as megoldas:
    for i in lista:
        megoldas.write(i,  ",")
