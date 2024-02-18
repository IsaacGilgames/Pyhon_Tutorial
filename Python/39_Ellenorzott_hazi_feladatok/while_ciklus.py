#b
#Írj egy programot, amely a beolvasott számok alapján megszámolja, hány volt pozitív és hány volt negatív szám! A nulla a kilépés legyen a ciklusból!

#Első megoldás
pozitiv_szamlalo = 0
negativ_szamlalo = 0

while True:
    szam = float(input("Kérem, adjon meg egy számot (kilépéshez írja be a 0-t): "))

    if szam == 0:
        break

    if szam > 0:
        pozitiv_szamlalo += 1
    elif szam < 0:
        negativ_szamlalo += 1

print("Pozitív számok száma:" (pozitiv_szamlalo))
print("Negatív számok száma:" (negativ_szamlalo))

#Második megoldás
a = int(input("Adj meg egy számot: "))
pozitiv = []
negativ = []
while a != 0:
    if a > 0:
        pozitiv.append(a)
    else:
        negativ.append(a)
    a = int(input("Adj meg egy számot: "))
poz_ossz = len(pozitiv)
neg_ossz = len(negativ)
print(f"Pozitív számok: {poz_ossz}")
print(f"Negatív számok: {neg_ossz}")


#Harmadik megoldás
print("✰ 〉⭒⋆")
a=int(input("adj meg egy számot:\n  "))
poz=0
neg=0
while True:
    if a<0 and a!=0:
        neg+=1
        print(f"a {a} egy negatív szám")
        print(f"eddig {neg} negatív szám volt és {poz} pozitív")
        print("⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒")
    elif a==0:
        print("okés szia")
        break
    else:
        poz+=1
        print(f"a {a} egy pozitív szám")
        print(f"eddig {neg} negatív szám volt és {poz} pozitív")
        print("⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒")
    print()
    a=int(input("adj meg még egy számot:\n"))
print("⭒✮ ✭ ✮ ✭ ✮⭒")


#Negyedik megoldás
pos_count = 0
neg_count = 0
num = int(input("Adj meg egy számot!\n"))
while num != 0:
    if num > 0:
        pos_count+=1
    elif num < 0:
        neg_count+=1
    print(f"A negatív számok száma eddig: {neg_count}, a pozitívaké: {pos_count}")
    num = int(input("Adj meg egy számot!\n"))



#Ötödik megoldás
szam = int(input("Adj meg egy számot:"))
szamok = []
negativ = 0
pozitiv = 0
while szam != 0:
    if szam not in szamok:
        szamok.append(szam)
    else:
        print("Ez a szám már volt")
    szam = int(input("Adj meg egy számot:"))
for x in szamok:
    if x < 0:
        negativ +=1
    else:
        pozitiv += 1
print(f"A listában {negativ} negatív és {pozitiv} pozitív szám van")


#Hatodik megoldás
pozitiv = 0
negativ = 0
igaz = True

while igaz:
    number = float(input("Adj meg egy számot: "))
    if number > 0:
        pozitiv += 1
        print(f"{pozitiv} pozitív egész számot adtál meg")
    elif number == 0:
        igaz = False
    else:
        negativ += 1
        print(f"{negativ} negatív egész számot adtál meg")



#Hetedik megoldás
        
szam = int(input("Adj meg egy számot:"))
szamok = []
pozitiv = 0
negativ = 0
 
while szam != 0:
    if szam not in szamok:
        szamok.append(szam)
    else:
        print("Ez a szám már volt")
    szam = int(input("Adj meg egy számot:"))
for x in szamok:
    if x < 0:
        negativ +=1
    else:
        pozitiv += 1
print(f"A listában {pozitiv} pozitív és {negativ} negatív  szám van")