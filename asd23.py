homerseklet = float(input("Add meg az alap hőfokot?"))
mertekegyseg = input("Add meg a mértékegységet C=celsius F=Farenheit K=Kelvin")
valto = input("Add meg mire szeretnéd átváltami C=celsius F=farenheit K=kelvin")

if mertekegyseg == "C" and valto == "F":
    print("a Hőmérséklet farenheitben: ", homerseklet * 1.8 + 32)
elif mertekegyseg == "C" and valto == "K":
    print("a Hőmérséklet kelvinben: ", homerseklet + 273.15)
elif mertekegyseg == "C" and valto == "C":
    print("A hőmérséklet Celsiusban =",homerseklet)
elif mertekegyseg == "F" and valto == "C":
    print("a Hőmérséklet celsiusban: ", (homerseklet - 32) / 1.8)
elif mertekegyseg == "F" and valto == "K":
    print("a Hőmérséklet kelvinben: ", (homerseklet - 32) / 1.8) + 273.15
elif mertekegyseg == "F" and valto == "F":
    print("a Hőmérséklet farenheitben: ",homerseklet)
elif mertekegyseg == "K" and valto == "C":
    print("A hőmérséklet celsiusbam: ", homerseklet - 273.15)
elif mertekegyseg == "K" and valto == "F":
    print("a Hőmérséklet farenheitben: ", (homerseklet - 273.15) * 1.8 + 32)
elif mertekegyseg == "K" and valto == "K":
    print("a Hőmérséklet Kelvinben: ",homerseklet)