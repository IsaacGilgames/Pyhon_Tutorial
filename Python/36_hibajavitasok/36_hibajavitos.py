#1. feladat - Hibajavítás
#10 alkalommal akarok sorsoltatni egy random számot és elmenteni a listára!
#5 db hibát vétettem a programban!
import random #hiányzott
a = 10
b = 15
list1 = []  #list ne legyen a neve



def randomNumber(x, y):
    lista = []
    for i in range(10): #(1, 11)
        lista.append(random.randint(x, y))  #range(x, y+1)
    return lista

list1 = randomNumber(a, b) #hiányzott a feladat leírása szerint!
print(randomNumber(a, b))  #fordítot sorrend

#2. feladat! - Írj egy függvényt, amely végig megy a számokon és eldönti, mely számok  hányszor ismétlődnek!

def ismetlodes(lista):
    seged = []
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                if lista[i] not in seged:
                    seged.append(lista[i])
                    print(f"A(z) {lista[i]} {lista.count(lista[i])}x ismétlődik ")
                    