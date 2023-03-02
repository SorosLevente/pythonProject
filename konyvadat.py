szotar = {}


while True:
    szerzo = input("adjaon meg gy szerzőt")
    if szerzo == "":
        break
    else:
        cim = input("adja meg a szerző műjét")
        szotar[szerzo] = cim

for i in szotar:
    print(i, ":", szotar[i])
