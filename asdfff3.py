a = "abcde"


for i in a:
    print(i, end=" ")

print(" ")

for i in range(0,len(a),2):
    print(a[i], end=" ")

print(" ")

for i in a:
    print(ord(i), end=" ")

