# F to C = (f-32)/1.8
# C to F = c*1.8+32

homerseklet = float(input("Add meg az alap hőfokot?"))
mertekegyseg = input("Add meg a mértékegységet C=celsius F=Farenheit K=Kelvin")

if mertekegyseg == "C":
    print("A hőmérséklet celsiusbam: ",homerseklet)
    print("a Hőmérséklet farenheitben: ", homerseklet*1.8+32)
    print("a Hőmérséklet kelvinben: ", homerseklet + 273.15)
elif mertekegyseg == "F":
    print("A hőmérséklet farenheitben: ", homerseklet)
    print("a Hőmérséklet celsiusban: ", (homerseklet-32)/1.8)
    print("a Hőmérséklet kelvinben: ", (homerseklet - 32) / 1.8)+273.15

elif mertekegyseg == "K":
    print("A hőmérséklet celsiusbam: ", homerseklet-273.15)
    print("a Hőmérséklet kelvinben: ", homerseklet)
    print("a Hőmérséklet farenheitben: ", (homerseklet-273.15)*1.8+32)