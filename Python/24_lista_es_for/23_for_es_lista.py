#for_es_lista.py
"""
for i in range(1, 11):  # 1 <= i < 11
    print(i)

#print(" "*2 + "*"*7)
#print(" " + "*"*9)
#print("*"*11)

csillag = int(input("Mekkora legyen a karácsonyfa: "))
szokoz = csillag // 2
for i in range(1, csillag+1, 2):
    print(" "*szokoz + "*"*i)
    szokoz -= 1


for char in text:
    if char != " ":
        print(char)

print(len(text))

text = "Boldog Karácsonyt!"
for i in range(1, len(text), 2):
    print(text[i])



text = "Horváth Boldizsár"
#text = text.replace(" ", "")

text2 = ""
for char in text:
    if char != " ":
        text2 = text2 + char


for i in range(1, len(text), 2):
    print(text[i])



varosok = ["Szombathely", "Sopron", "Győr", "Budapest", "Pécs"]


for varos in varosok:
    print(varos)

#print(len(varosok))
for i in range(0, len(varosok)):
    print(varosok[i])
"""

varosok = ["Szombathely", "Sopron", "Győr", "Budapest", "Pécs"]

romai_varosnevek = ["Savaria", "Scarbantia", "Arabona", "Aquincum", "Sophiane"]

varos = input("Melyik város római nevét szeretnéd tudni!\n")


for i in range(0, len(varosok)):
    if varosok[i] == varos:
        print(romai_varosnevek[i])