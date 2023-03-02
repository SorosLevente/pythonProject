c = input("adj meg egy szót")
h = " "
for i in range(len(c)-1,-1,-1):
    h = h+c[i]

print(h)


if c == c[::-1]:
    print("ez egy palindrom")
else:
    print("Ez nem palindrom")

mondat = "az alma a fán piros "
szo = " "

for i in mondat:
    if i == " ":
        print(szo)
        szo = " "
    else:
        szo=szo+i


for i in mondat.split(" "):
    print(i)