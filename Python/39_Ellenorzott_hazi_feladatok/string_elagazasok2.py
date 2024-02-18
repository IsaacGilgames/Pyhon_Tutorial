#b
"""
Írj programot, amely egy tetszőleges szövegben megszámolja az "a" betűk számét (kis és nagybetűt egyaránt)
A program cserélje ki az "a" betűket "e" betűkre!
Itt figyelj arra, hogy a mintához hasonlóan jelenjen meg!
Pl. Attila ma almat ad Annanak!
A beírt szöveg 9 "a" betűt tartalmaz.
A kicserélt szöveg: Ettile me elmet ed Ennenenk.
"""
#Első megoldás
szoveg = input("Adjon meg egy szöveget: ")

a_betuk_szama = szoveg.lower().count('a')

modositott_szoveg = szoveg.replace('a', 'e').replace('A', 'E')

print(f'A beírt szöveg {a_betuk_szama} "a" betűt tartalmaz.')
print(f'A kicserélt szöveg: {modositott_szoveg}')

#Második megoldás
text1 = input("Adj meg egy szöveget: ")
text1.casefold()
a = text1.count("a")
b = text1.count("A")
ossz = a + b
print(f"A beírt szöveg {ossz} \"a\" betűt tartalmaz.")
for i in range(len(text1)):
    if text1[i] == "A":
        text1 = text1.replace(text1[i], "E")
    elif text1[i] == "a":
        text1 = text1.replace(text1[i], "e")
print(f"A kicserélt szöveg: {text1}")

szoveg = input("Adj meg egy szöveget!: ")


#Harmadik megoldás
a_betuk_szama = 0
kicserelt_szoveg = ""

for karakter in szoveg:
    if karakter.lower() == 'a':
        a_betuk_szama += 1
        kicserelt_szoveg += 'e'
    else:
        kicserelt_szoveg += karakter

print(f'A beírt szöveg {a_betuk_szama} "a" betűt tartalmaz.')
print(f'A kicserélt szöveg: {kicserelt_szoveg}')

