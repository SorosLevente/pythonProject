a = str(input("adj"))
db = 0
szanok = "0123456789"
for i in a:
    if i in szanok:
        db = db+1
        print(i)

print(db)