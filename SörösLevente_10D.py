import math
for i in range(1,6,1):
    print("Adjon meg egy számot")
    a = float(input())

    if a == 0:
        print("a kör opciót választotta adja meg a kör sugarát")
        r = float(input())
        terulet = r ** 2 * 3.14
        kerulet = 2 * r * 3.14
        print("A kör sugara:", r, "A kör területe:", terulet, "A kör kerülete:", kerulet)
    elif a % 2 == 0:
        print("Ön a négyzet opciót választotta a megfelelő szám", a, "páros szám.Négyzete:", a ** 2, )
    else:
        print("Nincs ilyen opció")































