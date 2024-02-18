#Írj egy Python programot, amely bekér három számot a 
# felhasználótól és kiírja a képernyőre, hogy
#a számok közül bármelyik kettőnek 
# az összege egyenlő-e a harmadik számmal!

a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg egy számot: "))
c = int(input("Adj meg egy számot: "))

if a + b == c:
    print(f"A(z) {a} + {b} = {c}")
elif a + c == b:
    print(f"A(z) {a} + {c} = {b}")
elif c + b == a:
    print(f"A(z) {c} + {b} = {a}")
else:
    print("Nincs olyan két szám a megadottak közül, aminek az összege egyenlő a harmadik számmal!")

#Kérj be két számot!
#Írd ki, hogy az egyik szám az kétszerese-e 
# a másik számnak!
#Írd ki, hogy az egyik szám a másiknak a fele-e!

x = int(input("Adj meg egy számot: "))
y = int(input("Adj meg egy számot: "))


if x == y / 2:
    print(f"{x} fele a(z) {y}-nak")
elif y == x / 2:
    print(f"{y} fele a(z) {x}-nak")
else:
    print("Egyik se a fele a másiknak!")

#Második megoldás

if x == y * 2:
    print(f"{y} fele a(z) {x}-nak")
elif y == x * 2:
    print(f"{x} fele a(z) {y}-nak")
else:
    print("Egyik se a fele a másiknak!")



#9-től 49-ig 5-vel lépkedve írjuk ki a számokat egy sorba!

for i in range(9, 49+1, 5):
    if i < 49:
        print(i, end=", ")
    else:
        print(i)


tol = int(input("Adj meg egy számot: "))
ig = int(input("Adj meg egy számot: "))


for i in range(tol, ig+1): 
    print(i, end="; ")

#Ha a végén nem szeretnék vesszőt!
a = 14
b = 420
for i in range(a, b+1, 50):
    if i == a:
        print(i, end="")
    else:
        print(", ", end="")
        print(i, end="")

#ket_lista

varosok = ["Szombathely", "Sopron", "Győr", 
"Budapest", "Pécs"]

romai_varosnevek = ["Savaria", "Scarbantia", "Arabona", 
"Aquincum", "Sophiane"]

varos = input("Add meg a város nevét!\n")

for i in range(0, len(varosok)):
    if varosok[i] == varos:
        print(romai_varosnevek[i])
else:
    print("Nincs ilyen városnév a listámban!")


