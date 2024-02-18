#string_listak.py

text1 = "Ma január 15. van"
text2 = "Utálom a hétfőket"
text3 = "hétfő, kedd, szerda, csütörtök, péntek, szombat, vasárnap"
text4 = "somlói galuska; almás pite; pacalpörkölt, galuska"

szavak_lista = []
szavak_lista2 = []
#text2 = text2.lower()
szavak_lista = text2.lower().split()
szavak_lista2 = text1.lower().split()
#szavak_lista.append(text1.lower().split())

#print(szavak_lista2)

for e in szavak_lista2:
    if e.isalpha():
        szavak_lista.append(e)
#szavak_lista.extend(szavak_lista2)
print(szavak_lista)

lista3 = text3.split(", ")
print(lista3)
lista4 = text4.split("; ")
print(lista4[-1])

for e in lista4:
    print(e, end="; ")
print()
for i in range(0, len(lista4)):
    if i != len(lista4)-1:
        print(lista4[i], end="; ")
    else:
        print(lista4[i])

print("; ".join(lista4))


#w3schools.com strip() string method