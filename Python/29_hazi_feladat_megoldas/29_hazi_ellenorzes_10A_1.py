"""
1. Feladat: 
Írja ki az első 20 számból a) párosakat b) páratlanokat! (Válaszható a nehézségi szint)
A) Könnyeb változat: egyesével végig megyünk a számokon, majd mindegyik mellé oda írjuk, hogy páros vagy páratlan)
pl. 
1 páratlan
2 páros
3 páratlan
..."""
"""
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} páros")
    else:
        print(f"{i} páratlan")


paros = []
paratlan = []
for i in range(1, 21):
    if i % 2 == 0:
        paros.append(i)
    else:
        paratlan.append(i)

print(f"Páros számok {paros}")
print(f"Páratlan számok {paratlan}")


a = int(input("Adj meg egy számot!"))
b = int(input("Adj meg egy számot!"))
osszeg = 0
atlag = 0
db = 0

while a <= b:
    osszeg += a
    db += 1
    a += 1

print(osszeg)

if db > 0:
    atlag = osszeg / db
    print(atlag)

ev1 = int(input("Adj meg egy évet!"))
ev2 = int(input("Adj meg egy évet!"))


if ev2 < ev1:
    temp = ev1
    ev2 = ev1
    ev1 = temp
szokoevek = []
for ev in range(ev1, ev2+1):
    if (ev % 400 == 0) or (ev % 4 == 0 and ev % 100 != 0):
        szokoevek.append(ev)

print("Szököévek:", end=" ")

for i in range(0, len(szokoevek)):
    if i == len(szokoevek)-1:
        print(szokoevek[i], end="\n")
    else:
        print(szokoevek[i], end="; ")


"""

number = int(input("Adj meg egy számot!"))
i = 1
oszto = []
while i <= number:
    if number % i == 0:
        oszto.append(i)
    i+=1






