ember = {"név": "Géza",
         "születési_év": 1999,
         "lakhely": "Makkoshotyyka",
         "Foglalkozás": "szarvasmarha-tenyésztő",
         "szemei száma": "2",
         "kedvenc lottószámok": [1, 2, 3, 4, 5]}

print(ember.keys())
print(ember.values())

for i in ember.keys():
    print(i, ":", ember[i])

print(ember["név"])

ember["kutya"] = "bodri"
ember.pop("szemei száma")
ember["születési_év"] = 1980
print(ember)
