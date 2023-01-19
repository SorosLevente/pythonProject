homer=[]
for i in range(1, 31):
    ho = float(input())
    homer.append(ho)
atlag = sum(homer)/len(homer)
minimum = min(homer)
maxElem = homer[0]
for i in range(1, len(homer)):
    if homer[i] > maxElem:
        maxElem = homer[i]
fagy = []
for i in homer:
    if i < 0:
        fagy.append(i)
    fagy = len(fagy)

print("Az átlagos hőmérséklet: ",atlag,"C°")
print("A legkisebb hőmérésklet: ", minimum,"C°")
print("A legmelegebb hőmérséklet:",maxElem,"C°. Ezt a",homer.index(maxElem)+1,".dik napon mérték")
print(fagy, "napon fagyott.")

