lsita = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 16]


def harommal_oszthato(lista):
    a = 0
    for i in lista:
        if i % 3 == 0:
            a = a + 1
    return a


db = harommal_oszthato(lsita)
print(db)
