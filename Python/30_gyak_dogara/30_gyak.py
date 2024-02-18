for i in range(99, 0, -1):
    print(i, end=" ")


for i in range(99, 1-1, -1):
    print(i, end=" ")


a = 99
b = 1
for i in range(a, b-1, -1):
    print(i, end=" ")


hossz = 5

#öt, vagy annál több a betűk száma
#csak betűkből álljon!
#ha van benne nem betű, azt törölje

print()
print("2. feladat")
szo = input("Adj meg egy szót!\n")

h_szo = ""

for i in range(0, len(szo)):
    if szo[i].isalpha():
        h_szo = h_szo + szo[i]
#print(h_szo)
while len(h_szo) < hossz or h_szo.isalpha() == False:
    szo = input("Adj meg egy szót!\n")
    for i in range(0, len(szo)):
        if szo[i].isalpha():
            h_szo = h_szo + szo[i]


nevek = ["Vak Cina", "Abrosz Tisztakosz", "Bekre Pál"]
magassag = [187, 167, 178]
nev = input("Kinek a magasságára vagy kíváncsi?\n")
for i in range(0, len(nevek)):
    if nevek[i] == nev:
        print(f"{nevek[i]}: {magassag[i]} cm")
        










