#Készíts egy mappát a Python mappádon belül "Önálló" néven
#A mappában csinálj egy python fájlt: Lotto_0123_A1.py néven

#Feladat:
#Sorsolj egy random számot 1-10 között!
#Tárold el!
#Írd ki!

import random
#randint() -> elso_szam <= random_szam <= vegso_szam
#randrange()    -> elso_szam <= random_szam < vegso_szam
#choice()
rand_number1 = random.randint(1, 10)
rand_number2 = random.randrange(1, 11)
number_list = range(1, 11)
rand_number3 = random.choice(number_list)

print(rand_number1)
print(rand_number2)
print(rand_number3)

# 5db 1-90

def lotto():
    lotto_lista = []
    while len(lotto_lista) < 5:
        rand_number = random.randrange(1, 91)
        if rand_number not in lotto_lista:
            lotto_lista.append(str(rand_number))
    return lotto_lista


print("A mai nyerő számok: ", end="")
"""
l_lista = lotto()
print(l_lista)
print(lotto())
"""
print("; ".join(lotto()))






