import math
#pitagorasz tétel
print("Add meg az a oldalt")
a = float(input())
print("Add meg a b oldalt")
b = float(input())
c = math.sqrt(a ** 2 + b ** 2)
if a==0:
    print("Te gyerek azt nem úgy kő")
elif b==0:
    print("Há ember ezt így a gyárból ki sem adják")
else:
    print("a c oldal:",c)
