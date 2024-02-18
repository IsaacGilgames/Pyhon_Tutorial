#Lotto_0123_A12.py

#Sorsolj egy random számot 1-10 között!
#Tárold el!
#Írd ki!

import random
#randint()  -> kezdo_szam <= random_szam <= vegso_szam
#randrange() -> kezdo_szam <= random_szam < vegso_szam
#choice()
rand_number = random.randrange(1, 11)
number_list = range(1, 11)
rand_number2 = random.choice(number_list)

print(rand_number)
print(rand_number2)

#5db 1-90
def lotto():
    lottoszamok = []
    while len(lottoszamok) < 5:
        r_number = random.randrange(1, 91)
        if r_number not in lottoszamok:
            lottoszamok.append(str(r_number))
    return lottoszamok

#print(lotto())
print("A nyerő számok: ", end="")
print("; ".join(lotto()))
