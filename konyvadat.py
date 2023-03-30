szotar = {}
cimek = {}
mufaj = {}
lista = []
while True:
    szerzo = input("adjaon meg gy szerzőt")
    if szerzo == "":
        break
    else:
        while True:
            cim = input("adja meg a szerző műjét")
            if cim == "":
                break
            else:
                evszam = int(input("Adja meg mikor keletkezett a mű"))
                kateg = input("Adja meg a mű műfaját")
                leiras = input("Adjon leírást a műhöz")
                cimek[cim] = {"kiadási év": evszam, "Műfaja": kateg, "Leírás": leiras}
                szotar[szerzo] = cimek

for szerzo, muvek, in szotar.items():
    print("Szerző:",szerzo,)
    for cim, adatok in cimek.items():
        print("\t könyv:", cim,)
        for adat_kulcs, adat_ertek in leiras.items():
            print("\t \t")

