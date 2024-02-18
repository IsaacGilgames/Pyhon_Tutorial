#elagazasok.py
if False:
    print("Igaz")

number = int(input("Adj meg egy számot!\n"))

if number > 0: #ha ... akkor csináld
    print("A megadott szám pozitív!")
if number < 0: #ha ... akkor csináld
    print("A megadott szám negatív!")
if number == 0: #ha ... akkor csináld
    print("A megadott szám a nulla!")


if number > 0: #ha ...? akkor csináld
    print("A megadott szám pozitív!")
elif number < 0: #különbe ha ...? akkor csináld
    print("A megadott szám negatív!")
else: #minden más esetben csináld
    print("A megadott szám a nulla!")



dolgozat_eredmeny = input("Milyen lett a dolgozat eredménye?\n")
#print(type(dolgozat_eredmeny))
dolgozat_eredmeny = int(dolgozat_eredmeny)
#print(type(dolgozat_eredmeny))
if dolgozat_eredmeny >= 90:
    print("Jeles")
elif dolgozat_eredmeny >= 75:
    print("Jó")
elif dolgozat_eredmeny >= 60:
    print("Közepes")
elif dolgozat_eredmeny >= 40:
    print("Elégséges")
else:
    print("Elégtelen")


#Javított dolgozat osztályozó program, ami figyel, hogy ne írhassunk be 100-nál többet és 0-nál kevesebbet!
dolgozat_eredmeny = input("Milyen lett a dolgozat?\n")
dolgozat_eredmeny = int(dolgozat_eredmeny)
if dolgozat_eredmeny <=100 and dolgozat_eredmeny >= 0:
    if dolgozat_eredmeny >= 90:
        print("Jeles")
    elif dolgozat_eredmeny >= 75:
        print("Jó")
    elif dolgozat_eredmeny >= 60:
        print("Közepes")
    elif dolgozat_eredmeny >= 40:
        print("Elégséges")
    else:
        print("Elégtelen")
else:
    print("A dolgozatra ennyi pontot nem kaphattak!")



