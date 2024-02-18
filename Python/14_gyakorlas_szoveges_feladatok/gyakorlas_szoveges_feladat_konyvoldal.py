#Készíts egy programot a következő elvárások betartásával!
#A felhasználó egy új könyvet olvas! A felhasználó fogja megadni az oldalak számát!
#Feltételezhetjük, hogy a felhasználó csak pozitív egész számokat fog megadni!
#A megadott adat alapján kell meghatároznotok:
#   1. Döntsük el, hogy a beírt oldalszám tényleg könyvhöz tartozik-e:
#       a) Ha kevesebb, mint 20 oldal a könyv:
#           pl 12 oldal esetén
#           "Nem könyvet olvasol, mert 12 oldalnyi hosszú könyv nincs."
#       b) Ha több mint 20, de maximum csak 50 oldalból áll, írja ki: 
#           pl. 34 oldal esetén
#           "Biztos, hogy könyvet olvasol, mert 34 oldal kicsit rövid nekem. Olvasd el még ma délután!"
#       c) Ha maximum 100 oldalból áll, írja ki: 
#           pl. 84 oldal esetén
#           "Kicsit rövid ez a könyv, hiszen csak 84 oldalas. Ne húzd vele az időt!"
#       d) Ha 100 oldalnál több oldalból áll, akkor írja ki, hogy hány nap alatt végzek a könyvel!
#   2. A felhasználó naponta 20 oldalt szeretne elolvasni, ha 100 oldalnál hosszabb a könyv!
#       a) Ha a könyv kiolvasható úgy, hogy minden nap 20 oldalt olvas el, akkor irja ki a program:
#           pl. 280 oldal esetén
#           "A könyv, amely 280 oldalas 14 nap alatt elolvasható számomra."
#       b) Ha utolsó nap max 10 oldalam maradna:
#           pl. 267 oldal esetén
#           "A köny, amely 267 oldalas 13 nap alatt elolvasható számomra, de utolsó nap 27 oldalt kell elolvasnom!"
#       c) Ha utolsó nap több mint 10 oldalam maradna:
#           pl. 274 oldal esetén
#           "A köny, amely 274 oldalas 14 nap alatt elolvasható számomra, de utolsó nap 14 oldalt  kell elolvasnom!"


oldalszam = int(input("Add meg az oldalak számát!\n"))
if oldalszam < 20:
    print(f"Nem könyvet olvasol, mert {oldalszam} oldalnyi hosszú könyv nincs.")
elif oldalszam >= 20 or oldalszam <= 50:
    print(f"Biztos, hogy könyvet olvasol, mert {oldalszam} oldal kicsit rövid nekem. Olvasd el még ma délután!")
elif oldalszam <= 100:
    print(f"Kicsit rövid ez a könyv, hiszen csak {oldalszam} oldalas. Ne húzd vele az időt!")
else:
    if oldalszam % 20 == 0:
        print(f"A könyv, amely {oldalszam} oldalas 14 nap alatt elolvasható számomra.")
    elif oldalszam % 20 <= 10:
        print(f"A köny, amely {oldalszam} oldalas {oldalszam//20} nap alatt elolvasható számomra, de utolsó nap {oldalszam%20+20} oldalt kell elolvasnom!")
    else:
        print(f"A köny, amely {oldalszam} oldalas {oldalszam//20+1} nap alatt elolvasható számomra, de utolsó nap {oldalszam%20} oldalt kell elolvasnom!")