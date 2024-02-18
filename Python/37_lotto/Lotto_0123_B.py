#Lotto_0123_B.py

#Sorsolj egy random számot 1-10 között!
#Tárold el!
#Írd ki!
import random
#randint() elso_szam <= r_szam <= utolso_szam
#randrange() elso_szam <= r_szam < utolso_szam
#choices()
r_number1 = random.randint(1, 10)
r_number2 = random.randrange(1, 11)
number_lista = range(1, 11)
r_number3 = random.choice(number_lista)
print(r_number1)
print(r_number2)
print(r_number3)



# 5 db szám 1-90
def lotto():
    lottoszamok =  []
    while len(lottoszamok) < 5:
        r_number = random.randrange(1, 91)
        if r_number not in lottoszamok:
            lottoszamok.append(str(r_number))
    return lottoszamok

print("A mai nyerőszámok: ", end="")
l_lista = lotto()
s_lista = ", ".join(l_lista)
print(s_lista)




