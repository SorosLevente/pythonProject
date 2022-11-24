a = int(input("Adj meg egy számot"))

logikai = True

for i in range(2,a,1):
  if a % i == 0:
        logikai = False

while logikai==True:
    a = int(input("Adj meg egy számot"))


if a%2==0:
    print("Hurrá")
elif a % 3 == 0:
        print("Három a magyar igazság")
elif a<10:
    if a == 1:
            print("I")
    elif a == 2:
            print("II")
    elif a == 3:
            print("III")
    elif a ==4 :
            print("IV")
    elif a == 5:
            print("v")
    elif a == 6:
            print("VI")
    elif a == 7:
            print("VII")
    elif a == 8:
            print("VIII")
    elif a == 9:
            print("IX")
    elif a == 10:
            print("X")
if a%2 and a%3 and a>10:
        print("Nem nyert")




















