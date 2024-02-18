#b
#Írj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig, amíg a felhasználó nullát nem ad be! A program az összes értéket tárolja egy listában, majd írja ki a képernyőre a lista elemeit fordított sorrendben!

#Első megoldás
lista = []
szam = int(input("Adj meg egy számot: "))

while szam != 0:
    if szam < 0:
        szam = int(input("Adj meg egy számot: "))
    else:
        lista.append(szam)
        szam = int(input("Adj meg egy számot: "))

for i in range(len(lista)-1, -1, -1):
    print(lista[i])

#Második megoldás
megadott_szamok = []

szam = int(input("Adj meg egy számot!\n"))

while szam != 0:
    megadott_szamok.append(szam)
    megadott_szamok.reverse()
    print(megadott_szamok)
    szam = int(input("Adj meg egy számot!\n"))
print("Vége.")


#Harmadik megoldás
szam = int(input("Adj meg egy számot! "))
szam_lista = []
szam_lista.append(szam)
while szam != 0:
    szam = int(input("Adj meg egy számot! "))
    if szam !=0:
        szam_lista.append(szam)
szam_lista.reverse()
print((szam_lista))


#Negyedik megoldás
numlist = []
number = None

while number != 0:
    number = int(input("Adj egy számot!\n"))
    if number != 0:
        numlist.append(number)
    print(numlist)

reverseNumlist = numlist[::-1]
print(reverseNumlist)

#Ötödik megoldás
szam = int(input("Adj meg egy számot: "))
osszes = []
while szam != 0:
    if szam > 0:
        osszes.append(szam)
    else:
        print("Csak pozitív számot adj meg!")
    szam = int(input("Adj meg egy számot: "))
osszes.reverse()
print("A megadott számok:", end=" ")
for i in range(len(osszes)):
    if i != len(osszes)-1:
        print(osszes[i], end="; ")
    else:
        print(osszes[i])


#Hatodik megoldás
print("✰ 〉⭒⋆")
nullaaaa=int(input("adj meg egy pozitív egész számot:\n  "))
dolgok=[]
print("⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒")
while True:
    if nullaaaa!=0:
        dolgok.insert(0, nullaaaa)
        nullaaaa=int(input("adj meg egy pozitív egész számot:\n  "))
    else:
        break
print("nullaaaaaaaaaa 🗣🗣🔥🔥🔥")
print("előző számaid:",dolgok)
print("⭒✮ ✭ ✮ ✭ ✮⭒")



#Hetedik megoldás
szamok = []
szam = float(input("Adj meg egy pozitív számot (0 a kilépéshez): "))
while szam > 0:
    szam = float(input("Adj meg egy pozitív számot (0 a kilépéshez): ")) #nem volt megadva, hogy egész szám legyen.
    if szam == 0:
        break
    
    szamok.append(szam)

print("A bevitt számok fordított sorrendben:")
for i in reversed(szamok):
    print(i)


#Nyolcadik megoldás
szam=int(input("Adjon meg egy szamot: "))
szamok=[]
if szam!=0:
    szamok.append(szam)
while szam!=0:
    szam=int(input("Adjon meg egy szamot: "))
    if szam!=0:
        szamok.append(szam)
for i in range(len(szamok) - 1, -1, -1):
    print(szamok[i],end=" ")



#Kilencedik megoldás
szam = int(input("Adj meg egy számot:"))
szamok = []
while szam != 0:
    if szam != 0:
        szamok.append(szam)
    szam = int(input("Adj meg egy számot:"))
szamok.reverse()
for x in szamok:
    print(x, end= "")
    if szamok[len(szamok)-1] != x:
        print(end= ", ")