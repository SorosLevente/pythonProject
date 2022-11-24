listamagas = []
osztaly = 3
magassag = 0
for i in range(osztaly):
    magassag = float(input())
    listamagas.append(magassag)

legnagyobb = 0
for i in listamagas:
    if i >legnagyobb:
        legnagyobb=i

print(legnagyobb)