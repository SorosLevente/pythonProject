lista = []
st =""
with open("egysoros.txt", "r", encoding="utf-8") as file:
    for sor in file:
        lista = sor.strip().split(";")

print(lista)

for i in range(len(lista)):
    lista[i] = int(lista[i])




def rendezo(lista):
    for i in range(0,len(lista)-1):
        for j in range(i,len(lista)):
            if lista[i] < lista[j]:
                lista[i],lista[j] = lista[j],lista[i]
    return lista


rendezo(lista)
print(lista)

for i in lista:
    st = st+str(i)+","


with open("egysoros eredmény.txt.txt", "w", encoding="utf-8") as megoldas:
    megoldas.write(st)

