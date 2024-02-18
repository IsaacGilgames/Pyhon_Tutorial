#b
#A programban  kérj be négy szöveget, majd írd ki milyen hosszú a legrövidebb és a leghosszabb szöveg.

#Első megoldás
szoveg1 = str(input("Adj meg egy szöveget! "))
szoveg2 = str(input("Adj meg egy szöveget! "))
szoveg3 = str(input("Adj meg egy szöveget! "))
szoveg4 = str(input("Adj meg egy szöveget! "))
if len(szoveg1) >= len(szoveg2) and len(szoveg1) >= len(szoveg3) and len(szoveg1) >= len(szoveg4):
    leghosszabb = szoveg1
elif len(szoveg2) >= len(szoveg3) and len(szoveg2) >= len(szoveg4):
    leghosszabb = szoveg2
elif len(szoveg3) >= len(szoveg4):
    leghosszabb = szoveg3
else:
    leghosszabb = szoveg4

if len(szoveg1) <= len(szoveg2) and len(szoveg1) <= len(szoveg3) and len(szoveg1) <= len(szoveg4):
    legrovidebb = szoveg1
elif len(szoveg2) <= len(szoveg3) and len(szoveg2) <= len(szoveg4):
    legrovidebb = szoveg2
elif len(szoveg3) <= len(szoveg4):
    legrovidebb = szoveg3
else:
    legrovidebb = szoveg4

print(f"A legrövidebb szöveg: {legrovidebb}, hossza: {len(legrovidebb)} karakter")
print(f"A leghosszabb szöveg: {leghosszabb}, hossza: {len(leghosszabb)} karakter")


#Második megoldás
szoveg1 = input("Add meg az első szöveget: ")
szoveg2 = input("Add meg a második szöveget: ")
szoveg3 = input("Add meg a harmadik szöveget: ")
szoveg4 = input("Add meg a negyedik szöveget: ")

hosszak = [len(szoveg1), len(szoveg2), len(szoveg3), len(szoveg4)]

legrovidebb_hossz = min(hosszak)
leghosszabb_hossz = max(hosszak)

print(f"A legrövidebb szöveg hossza: {legrovidebb_hossz} karakter")
print(f"A leghosszabb szöveg hossza: {leghosszabb_hossz} karakter")


#Harmadik megoldás
text1 = input("Adj meg egy szöveget: ")
text2 = input("Adj meg egy szöveget: ")
text3 = input("Adj meg egy szöveget: ")
text4 = input("Adj meg egy szöveget: ")

if len(text1) <= len(text2) and len(text1) <= len(text3) and len(text1) <= len(text4):
    lg_rovidebb = text1
elif len(text2) <= len(text1) and len(text2) <= len(text3) and len(text2) <= len(text4):
    lg_rovidebb = text2
elif len(text3) <= len(text1) and len(text3) <= len(text2) and len(text3) <= len(text4):
    lg_rovidebb = text3
else:
    lg_rovidebb = text4

if len(text1) >= len(text2) and len(text1) >= len(text3) and len(text1) >= len(text4):
    lg_hosszabb = text1
elif len(text2) >= len(text1) and len(text2) >= len(text3) and len(text2) >= len(text4):
    lg_hosszabb = text2
elif len(text3) >= len(text1) and len(text3) >= len(text2) and len(text3) >= len(text4):
    lg_hosszabb = text3
else:
    lg_hosszabb = text4

print(f"A legrövidebb szöveg hossza: {len(lg_rovidebb)} karakter.")
print(f"A leghosszabb szöveg hossza: {len(lg_hosszabb)} karakter.")


#Negyedik megoldás
words = []
for i in range(4):
    text = str(input("Adj meg egy szót!\n"))
    words.append(text)
longest = words[0]
shortest = words[0]
for x in words:
    if len(x) > len(longest):
        longest = x
    elif len(x) < len(shortest):
        shortest = x

print(f"A leghosszabb szó: {longest}, ami {len(longest)} karakter hosszú. A legrövidebb pedig {shortest}, ami {len(shortest)} karakter hosszú.")


#Ötödik megoldás
a = input("Adj meg egy szöveget: ")
b = input("Adj meg egy szöveget: ")
c = input("Adj meg egy szöveget: ")
d = input("Adj meg egy szöveget: ")
ah = len(a)
bh = len(b)
ch = len(c)
dh = len(d) 

lista = [ah,bh,ch,dh]

def maxi(lista):
    maximum = -1
    for i in range(0,len(lista)):
        if maximum < lista[i]:
            maximum = lista[i]
    return maximum

def mini(lista):
    minimum = maxi(lista)+1
    for i in range(0,len(lista)):
        if minimum > lista[i]:
            minimum = lista[i] 
    return minimum

print(f"A leghosszab szöveg hossza: {maxi(lista)}")
print(f"A legrövidebb szöveg hossza: {mini(lista)}")



