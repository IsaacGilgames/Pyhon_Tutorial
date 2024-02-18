#hazi_javitas
lista1=[2, 4, 5, 9, 12, 3, 9, 4]

def osszeg(lista, y):
    ossz = 0
    for x in lista:
        if x % 2 == y:
            ossz += x
    return ossz

print("Az első lista páros számainak összege:", 
osszeg(lista1, 0))
print("Az első lista páratlan számainak összege:", 
osszeg(lista1, 1))


def megszamol(lista, y):
    db = 0
    for x in lista:
        if x % 2 == y:
            db += 1
    return db

print("Az első lista páros számainak db száma:", 
osszeg(lista1, 0))
print("Az első lista páratlan számainak db száma:", 
osszeg(lista1, 1))
