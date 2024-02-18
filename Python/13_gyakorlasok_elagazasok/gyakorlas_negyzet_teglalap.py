#Kérjetek be két számot!
#Ez egy négyzet
#Ez egy téglalap
a = float(input("Adj meg egy számot!\n"))
b = float(input("Adj meg egy számot!\n"))
#ne írhassak be nullát vagy negatív számot
#Számold ki a kerületét és területét is!

#Egyik változat
if a > 0 and b > 0:
    if a == b:
        print("Ez egy négyzet!")
        print(f"A négyzet kerülete: {4*a} cm")
        print(f"{a*a} cm2 a négyzet kerülete!")
    else:
        print("Ez egy téglalap!")
        print(f"A téglalap kerülete: {2*(a + b)} cm")
        print(f"{a*b} cm2 a téglalap kerülete!")
else:
    print("Ilyen érté(ke)ket nem írhatsz be!")

#Második változat
if a > 0 and b > 0:
    if a == b:
        print("Ez egy négyzet!")
        print(f"A négyzet kerülete: {4*a} cm")
        print(f"{a*a} cm2 a négyzet kerülete!")
    else:
        print("Ez egy téglalap!")
        print(f"A téglalap kerülete: {2*(a + b)} cm")
        print(f"{a*b} cm2 a téglalap kerülete!")
else:
    print("Ilyen számo(ka)t nem adhatsz meg!")
    if a == 0 or b == 0:
        print("Nullát nem adhatok meg!")
    if a < 0 or b < 0:
        print("Minusz számot nem adhatok meg!")      