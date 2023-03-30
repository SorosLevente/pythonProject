import math as m

a = float(input("A:"))
b = float(input("B:"))
c = float(input("C:"))

x1 = (-1 * b + m.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
x2 = (-1 * b - m.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

print("Az x1 =", x1)
print("Az x2 =", x2)