#Kérj be három egész számot!
#A megadott számok közül, döntsd el, melyik a legkisebb!
szam1 = int(input("Adj meg egy számot:"))
szam2 = int(input("Adj meg egy számot:"))
szam3 = int(input("Adj meg egy számot:"))
min = 0

if szam1 > szam2:
    if szam2 > szam3:
        min = szam3
    else:
        min = szam2
else:
    if szam1 > szam3:
        min = szam3
    else:
        min = szam1
        
print(f"A legkisebb szám a(z) {min}")

