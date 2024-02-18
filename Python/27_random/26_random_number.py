import random

#print(random.randrange(1, 10)) #random szám generálás, 
# ami 1<= szám < 10, és csak egész szám lehet

Osztaly_10A_1 = [
    "Vince",
    "Ádám",
    "Huba",
    "Ákos",
    "Marcell",
    "Lili",
    "Márton",
    "Bátor",
    "Alex",
    "Dániel"
    "Dávid",
    "R. Kevin",
    "Márton",
    "Iván",
    "Anna",
    "Júlia",
    "T. Kevin",
    "Sára",
    "Kata"
]
osztaly_letszam = len(Osztaly_10A_1)
r_number = random.randrange(0, osztaly_letszam)
print(Osztaly_10A_1[r_number])

