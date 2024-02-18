import random

#print(random.randrange(1, 10))
#random szám generálása
# 1 <= number < 10


osztaly_10B = [
    "A. Ármin",
    "Patrik",
    "Bertalan",
    "Gábor",
    "Kevin",
    "Márton",
    "Richárd",
    "Szabolcs",
    "Dominik",
    "Alex",
    "N. Ármin",
    "Miklós",
    "Dávid",
    "Bálint",
    "Ádám",
    "Mátyás"
]

osztaly_letszam = len(osztaly_10B)
random_szam = random.randrange(0, osztaly_letszam)
print(osztaly_10B[random_szam])