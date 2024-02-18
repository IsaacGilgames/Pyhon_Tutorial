#Megadott évtől a megadott évig írja ki a számokat!
#Mindegy legyen a számok megadásának sorrendje!
kezdo = int(input("Adj meg egy évszámot: ")) #2023
zaro = int(input("Adj meg egy évszámot: ")) #1950
k = 0
    #2023   > 1950
if kezdo > zaro:
    k = kezdo   #2023
    kezdo = zaro    #1950
    zaro = k    #2023

for b in range(kezdo, zaro+1):
    print(b)

#Második megoldás
ev1 = int(input("Adj meg egy évszámot(1)"))
ev2 = int(input("Adj meg egy évszámot(2)"))
if ev1 < ev2:
    for i in range(ev1, ev2 +1):
        print(i)
elif ev2 < ev1:
    for i in range(ev2, ev1 +1):
        print(i)