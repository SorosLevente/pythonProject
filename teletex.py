
lista = [5, 3, 9, 1, 7]

for i in range(len(lista) - 1):
    for j in range(i + 1, len(lista)):
        print(i, j, lista, end='')
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
        print('!', lista[i], lista[j])
        print('  ', lista)
    else:
        print("mehet a zöld")


lista1= [6,5,7,8,1,2,4,3]
for i in range(len(lista1) - 1):
    print(lista1)
    minindex = i
    for j in range(i + 1, len(lista1)):
        if lista[j]<lista[minindex]:
            minindex=j
            print("Új minimum találat")
        else:
            print(" ")
    if i != minindex:
        lista[i],lista[minindex]=lista[minindex],lista[i]

