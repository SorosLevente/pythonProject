szotar = {}

while True:
    lista = []
    szerzo = input("adjaon meg gy szerzőt")
    if szerzo == "":
        break
    else:
        while True:
            cim = input("adja meg a szerző műjét")
            if cim == "":
                break
            else:
                lista.append(cim)
                szotar[szerzo] = lista

for i, j in szotar.items():
    print(i, ":", j)
