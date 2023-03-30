eu = []
with open("EU.txt","r",encoding= "utf-8") as file:
    for sor in file:
        eu.append(sor.strip().split(" "))

for i in range (len(eu)):
    eu[i][1] = int(eu[i][1])

min = eu[0][1]
for i in eu:
    if i[1] < min:
        min = i[1]


dbe = 0
dbb = 0
db6 = 0
legrövh = len(eu[0][0])
legrövn = eu[0][0]
for i in eu:
    if i[0][0] == "b":
        dbb = dbb+1
    if len(i[0]) > 6:
        db6 = db6+1
    if len(i[0]) < legrövh:
        legrövh = len(i[0])
        legrövh = i[0]
    if i[1] == min:
        dbe = dbe+1

print(dbe)
print(dbb)
print(db6)
print(legrövh)
print(legrövn)