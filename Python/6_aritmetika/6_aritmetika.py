#1. aritmetikai műveletek
print(2+2) #összeadás
print(6-3) #kivonás
print(2*3) #szorzás

print(6/3) #osztás, amelynek az eredénye float típusu
print(8/3)

print(6//3) #osztás, amelynek az eredénye integer típusu
print(8//3) #osztás, amelynek az eredénye integer típusu

#325s
print("Perc:")
print(325//60)  #hányszor van meg benne a 60
print("Másodperc:")
print(325%60) #maradékos osztás, ha elosztom 60-nal, mennyi a maradék

print(3**2) #hatványozás

#hozzárendelési operátorok
number = 3
print("Értéke: ", number)
number = number + 3
#a number új értéke a régi érték + 3 lesz
print("Értéke: ", number)
number += 3
print("Értéke: ", number)
number -= 5
print("Értéke: ", number)
number *= 2
print("Értéke: ", number)
number //= 4
print("Értéke: ", number)
number /= 2
print("Értéke: ", number)
number **= 4
print("Értéke: ", number)
