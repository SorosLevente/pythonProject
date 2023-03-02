lista1 = [33, 44, 55, 66, 77, 88, 99, 32, 425, 6, 45, 6, 6, 45, 34, 523, 45, 23, 534, ]


def rendez(lista):
    a = input("Növekvő vagy Csökkenő?")
    if a == "Növekvő" or a == "növekvő":
        for i in range(len(lista), 0, -1, ):
            for j in range(0, i - 1):
                if lista[j] > lista[j + 1]:
                    b = lista[j + 1]
                    lista[j + 1] = lista[j]
                    lista[j] = b
    elif a == "Csökkenő" or a == "csökkenő":
        for i in range(len(lista), 0, -1, ):
            for j in range(0, i - 1):
                if lista[j] < lista[j + 1]:
                    b = lista[j + 1]
                    lista[j + 1] = lista[j]
                    lista[j] = b
    else:
        print(" ")

    print(lista)


rendez(lista1)
print(lista1)
