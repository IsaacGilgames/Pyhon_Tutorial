hossz = 5

szo = input("Kérek egy szót!\n")

h_szo = ""

for i in range(0, len(szo)):
    if szo[i].isalpha():
        h_szo = h_szo + szo[i]

while len(h_szo) < hossz or h_szo.isalpha()==False:
    szo = input("Kérek egy szót!\n")
    for i in range(0, len(szo)):
        if szo[i].isalpha():
            h_szo = h_szo + szo[i]


nevek = ["Vak Cina", "Abrosz Tisztakosz", "Bekre Pál"]
magassag = [187, 167, 178]


nev = input("Kinek a magassága érdekel?\n")
nincs_ilyen = True

for i in range(0, len(nevek)):
    if nevek[i] == nev:
        print(f"{nevek[i]}: {magassag[i]} cm")
        nincs_ilyen = False

if nincs_ilyen == True:
    print(f"Nem volt ilyen név a listámon! ({nev})")




