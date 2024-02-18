"""
1. Feladat: 
Írja ki az első 20 számból a) párosakat b) páratlanokat! (Válaszható a nehézségi szint)
A) Könnyeb változat: egyesével végig megyünk a számokon, majd mindegyik mellé oda írjuk, hogy páros vagy páratlan)
pl. 
1 páratlan
2 páros
3 páratlan
..."""

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


"""
Számítsd ki a felhasználó által 
megadott a-tól b-ig terjedő számok összegét, átlagát!
A számítást for/while ciklus, változók és aritmetikai 
műveletek használatával old meg!
"""

a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg egy számot: "))
osszeg = 0
atlag = 0

temp = None
if b < a:
    #temp = b
    #b = a
    #a = temp
    a, b = b, a

i = a
db = 0
while i <= b:
    db += 1
    osszeg += i
    i+=1
print(osszeg)
print(osszeg/db)





