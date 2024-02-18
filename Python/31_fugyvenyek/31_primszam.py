#fuggveny_prim.py

number = 23
osztok = []
def oszto(x):
    for i in range(1, x+1):
        if x % i == 0:
            osztok.append(i)
oszto(number)
print(osztok)
pr = True
def primszam(x):
    pr = True               #másik esetben nem kell
    for i in range(2, x):
        if x % i == 0:
            pr = False      #másik esetben nem kell
            return pr       #működne a False
    return pr               #működne a True

print(primszam(number))
#1. változat
pr = primszam(number)
if pr == True:
    print("A számom prímszám!")

#2. változat
pr = primszam(number)
if pr:
    print("A számom prímszám!")
"""
if not pr:
    print("A számom nem prímszám!")
"""
#3. változat!
if primszam(number):
    print("A számom prímszám!")


number2 = 12
number3 = 24
number4 = 11

def ellenoriz(x):
    if primszam(x):
        print(f"Primszám {x}")
    else:
        print(f"Nem primszám {x}")

ellenoriz(number2)
ellenoriz(number3)
ellenoriz(number4)



