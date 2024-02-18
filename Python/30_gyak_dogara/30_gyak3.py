
meddig = int(input("Meddig számoljak vissza 100-ról?\n"))

for i in range(100, meddig-1, -1):
    print(i, end=" ")


hossz = 5
print()
szo = input("Adj meg egy szót!\n")

while len(szo) < hossz or szo.isalpha() == False:
    szo = input("Adj meg egy szót!\n")

nevek = ["Vak Cina", "Abrosz Tisztakosz", "Bekre Pál"]
magassag = [187, 167, 178]

nev = input("Kinek a magassága érdekel?")
nincs_ilyen = True
for i in range(0, len(nevek)):
    if nevek[i] == nev:
        print(f"{nevek[i]}: {magassag[i]} cm")
        nincs_ilyen = False
if nincs_ilyen == True:
    print("Nem szerepelt ilyen név a listámon!")

